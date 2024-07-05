# Copyright (c) 2021 Hewlett-Packard Enterprise Development LP.
# All Rights Reserved.
#
# This software is the confidential and proprietary information of
# Hewlett-Packard Enterprise Development LP.
#
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from enum import Flag, auto
import logging


def min_status(*statuses):
    """Return a list of statuses to ignore for filtering by minimum status.
    We include inactive and unknown status in the list to reject them on the min status filtering.
    There should be only one element in statuses, but if there are several,
    all ignored statuses are aggregated, which means the actual minimum status
    will be the most advanced of all statuses.
    """
    return list({
        e
        for s in statuses
        for e in Status.create(s).before_me(include_inactive=True, include_unknown=True).elements()
    })


def max_status(*statuses):
    """Return a list of statuses to include for filtering by maximum status.
    There should be only one element in statuses, but if there are several,
    all included statuses are aggregated, which means the actual maximum status
    will be the most advanced of all statuses.
    """
    return list({
        e
        for s in statuses
        for e in Status.create(s).before_me(include_me=True).elements()
    })


def previous_status(*statuses):
    """Create a list of Status which could lead to one of the given statuses."""
    return list({
        p
        for s in statuses
        for p in Status.create(s).previous()
    })


class Status(Flag):
    """State-machine for the life of a product.
    Possible States of a Solution/Product/Component, with possible state changes.
    Start with :
    status = Status.INIT.start()
    Create with either:
    status = Status.create("Status Name")
    status = Status.STATUS_NAME
    """
    # The states
    # states with names like CAN_XXX are groups of flags used to control the validity of an action.
    UNKNOWN = auto()  # Unknown status at creation
    FAIL = auto()  # Used as flag for FAILED statuses, not directly
    INIT = auto()  # Initial state
    # Status for Solution/Product/Component
    CT_READY = auto()  # Check of Component
    FT_READY = auto()  # Upon Build success of a product to enter FT
    IT_READY = auto()  # Upon FT success of a product to enter IT
    VAL_READY = auto()  # Upon IT success of a product to enter Validation
    QA_READY = auto()  # Upon Validation success
    RC = auto()  # Upon Promoting to RC
    # When Released
    CA_RELEASED = auto()
    GA_RELEASED = auto()
    # Post-release and final states
    BLACKLISTED = auto()
    DEPRECATED = auto()
    DISCONTINUED = auto()
    DISCARDED = auto()
    ARCHIVED = auto()

    # Status for Test/Result
    FAILED = auto()
    PASSED = auto()

    # Status for Caas
    PRESENT = auto()
    ABSENT = auto()

    # Processing error
    ERROR = auto()

    # Status for failures
    CT_FAILED = CT_READY | FAIL
    FT_FAILED = FT_READY | FAIL
    IT_FAILED = IT_READY | FAIL
    VAL_FAILED = VAL_READY | FAIL
    QA_FAILED = QA_READY | FAIL

    # Group of statuses for action
    CAN_BE_FT_READY = CT_READY
    CAN_BE_IT_READY = CT_READY | FT_READY
    CAN_BE_VAL_READY = IT_READY
    CAN_BE_QA_READY = VAL_READY | VAL_FAILED
    CAN_BE_RC = QA_READY | RC | QA_FAILED
    CAN_BE_ARCHIVED = RC
    CAN_BE_RELEASED = RC | CA_RELEASED
    CAN_BE_GA_RELEASED = CAN_BE_RELEASED
    CAN_BE_CA_RELEASED = CAN_BE_RELEASED
    CAN_BE_BLACKLISTED = GA_RELEASED
    CAN_BE_DEPRECATED = GA_RELEASED | CA_RELEASED
    CAN_BE_DISCONTINUED = DEPRECATED
    CAN_BE_DISCARDED = (
        INIT | UNKNOWN | PASSED | FAILED | FAIL |
        CT_FAILED | FT_FAILED | IT_FAILED | VAL_FAILED | QA_FAILED |
        CT_READY | FT_READY | IT_READY | VAL_READY | QA_READY | RC | BLACKLISTED
    )
    CAN_BE_DELETED = DISCONTINUED | DISCARDED | ARCHIVED

    # Status has already passed, but Artefact is not yet at end-of-life
    ALREADY_DISCARDED = ARCHIVED  # Allows Discarding of Products of an Archived Solution
    ALREADY_BLACKLISTED = DISCARDED
    ALREADY_DEPRECATED = DISCONTINUED
    ALREADY_RELEASED = GA_RELEASED | CA_RELEASED
    ALREADY_QUALIFIED = ALREADY_RELEASED | RC
    ALREADY_VALIDATED = ALREADY_QUALIFIED | QA_READY | QA_FAILED
    ALREADY_INTEGRATED = ALREADY_VALIDATED | VAL_READY | VAL_FAILED
    ALREADY_CHECKED = ALREADY_INTEGRATED | IT_READY | IT_FAILED
    ALREADY_CTCHECKED = ALREADY_CHECKED | FT_READY | FT_FAILED

    # Aliases for backward compatibility
    # For example: Status.QA_CANDIDATE.name == 'VAL_READY'
    COMPONENT_READY = CT_READY
    QA_CANDIDATE = VAL_READY
    SCAN_READY = VAL_READY
    SCAN_FAILED = VAL_FAILED
    RELEASED = GA_RELEASED

    INACTIVE = BLACKLISTED | DEPRECATED | DISCONTINUED | DISCARDED

    def fail_transition(self, call, **kwargs):
        if kwargs.get("test", True):
            # Testing the transition : no failure or error messages
            return False
        msg = "'{}' transition invoked on solution in state '{}'".format(call, self.name)
        logging.error(msg)
        return msg

    @staticmethod
    def create(name):
        try:
            return Status[str(name).upper().replace(" ", "_")]
        except KeyError:
            return Status.UNKNOWN

    def __str__(self):
        """Convert status to string: QA_READY => 'QA Ready', DEPRECATE => 'Deprecate', etc."""
        return Status.str(self.name)

    @staticmethod
    def str(name):
        return " ".join(
            word if len(word) == 2 else word.capitalize()
            for word in name.split("_")
        )

    def __format__(self, key):
        return ("{:" + key + "}").format(str(self))

    def start(self, isComponent=False, needsTests=True, **kwargs):
        """Starting point of an artefact life.
        This function might not be useful:
        it could be easier to simply assign the first status directly.
        """
        if self is not Status.INIT:
            return self.fail_transition("Create")
        if not needsTests:
            # This product does not requires build, functional or internal testing, or validation
            # Useful for external dependencies.
            # Still needs to be qualified though.
            return Status.QA_READY
        if isComponent:
            # This is a component, which requires component testing
            return Status.CT_READY
        return Status.FT_READY

    def before_me(self, include_me=False, include_failed=True, include_inactive=False, include_unknown=False):
        """Returns statuses which happened before self, including it or not"""
        r = {
            Status.CT_READY: Status.INIT,
            Status.FT_READY: Status.INIT | Status.CT_READY,
            Status.IT_READY: Status.INIT | Status.CT_READY | Status.FT_READY,
            Status.VAL_READY: Status.INIT | Status.CT_READY | Status.FT_READY | Status.IT_READY,
            Status.QA_READY: Status.INIT | Status.CT_READY | Status.FT_READY | Status.IT_READY | Status.VAL_READY,
            Status.RC: Status.INIT | Status.CT_READY | Status.FT_READY | Status.IT_READY | Status.VAL_READY | Status.QA_READY,
            Status.GA_RELEASED: Status.INIT | Status.CT_READY | Status.FT_READY | Status.IT_READY | Status.VAL_READY | Status.QA_READY | Status.RC,
        }.get(self, Status.INIT)
        if include_failed:
            r = r | Status.FAIL | Status.FAILED
        if include_inactive:
            r = r | Status.INACTIVE
        if include_unknown:
            r = r | Status.UNKNOWN
        if include_me:
            return r | self
        return r

    def elements(self):
        """Returns all statuses which are in self as string
        For example Status.CT_FAILED.elements() == {"CT Ready", "Fail", "CT Failed"}
        Includes aliases hence :
        Status.VAL_READY.elements() == {"Val Ready", "QA Candidate", "Scan Ready"}
        """
        return list({
            Status.str(x)
            for x in Status.__dict__.keys()
            if not x.startswith('CAN_')
            and not x.startswith('ALREADY_')
            and isinstance(getattr(Status, x), Status)
            and getattr(Status, x) in self
        })

    def previous(self):
        """
        Tries to return all Status which could lead to self
        Based on the assumption that to allow a Status to progress to a new one,
        it needs to be in the CAN_BE_{NEWT_STATUS} alias.
        For example all statuses which can lead to DISCARDED are elements of CAN_BE_DISCARDED
        """
        can_be_self = self.create(f"CAN_BE_{self}")
        return can_be_self.elements() if can_be_self != self.UNKNOWN else []

    # Actions.
    # Those functions allow for extra but unused arguments, for generalization purposes
    def action(self, action, **kwargs):
        return getattr(self, action)(**kwargs)

    def ct_check(self, isOk=True, **kwargs):
        """Component test"""
        if self in Status.CAN_BE_FT_READY or self == Status.CT_FAILED:
            if not isOk:
                return Status.CT_FAILED
            return Status.FT_READY
        if self in Status.ALREADY_CTCHECKED:
            return self
        return self.fail_transition("CT Check", **kwargs)

    def check(self, isOk=True, **kwargs):
        """Functional Tests"""
        if self in Status.CAN_BE_IT_READY or self == Status.FT_FAILED:
            if not isOk:
                return Status.FT_FAILED
            return Status.IT_READY
        if self in Status.ALREADY_CHECKED:
            return self
        return self.fail_transition("Check", **kwargs)

    def integrate(self, isOk=True, **kwargs):
        """Integration Tests"""
        if self in Status.CAN_BE_VAL_READY or self == Status.IT_FAILED:
            if not isOk:
                return Status.IT_FAILED
            return Status.VAL_READY
        if self in Status.ALREADY_INTEGRATED:
            return self
        return self.fail_transition("Integrate", **kwargs)

    def validate(self, isOk=True, **kwargs):
        """Product malware scan, and other validations"""
        if self in Status.CAN_BE_QA_READY:
            if not isOk:
                return Status.VAL_FAILED
            return Status.QA_READY
        if self in Status.ALREADY_VALIDATED:
            return self
        return self.fail_transition("Validate", **kwargs)

    def qualify(self, isOk=True, **kwargs):
        """Manual qualification of the solution/product"""
        if self in Status.CAN_BE_RC:
            if not isOk:
                return Status.QA_FAILED
            return Status.RC
        if self in Status.ALREADY_QUALIFIED:
            return self
        return self.fail_transition("Qualify", **kwargs)

    def archive(self, **kwargs):
        """Archiving Solutions containing Released Products"""
        if self in Status.CAN_BE_ARCHIVED:
            return Status.ARCHIVED
        return self.fail_transition("Archive", **kwargs)

    def release(self, isGA=True, **kwargs):
        if self in Status.CAN_BE_RELEASED:
            if isGA:
                return Status.GA_RELEASED
            return Status.CA_RELEASED
        if self in Status.ALREADY_RELEASED:
            return self
        return self.fail_transition("Release", **kwargs)

    def blacklist(self, **kwargs):
        if self in Status.CAN_BE_BLACKLISTED:
            return Status.BLACKLISTED
        if self in Status.ALREADY_BLACKLISTED:
            return self
        return self.fail_transition("Blacklist", **kwargs)

    def discard(self, **kwargs):
        if self in Status.CAN_BE_DISCARDED:
            return Status.DISCARDED
        return self.fail_transition("Discard", **kwargs)

    def deprecate(self, **kwargs):
        if self in Status.CAN_BE_DEPRECATED:
            return Status.DEPRECATED
        if self in Status.ALREADY_DEPRECATED:
            return self
        return self.fail_transition("Deprecate", **kwargs)

    def discontinue(self, **kwargs):
        if self in Status.CAN_BE_DISCONTINUED:
            return Status.DISCONTINUED
        return self.fail_transition("Discontinue", **kwargs)

    def delete(self, **kwargs):
        """End of the line, out unto the void"""
        if self in Status.CAN_BE_DELETED:
            return None
        return self.fail_transition("Delete", **kwargs)
