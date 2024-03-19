from reprlib import repr as limitedRepr


import enum
try:
    from ansible.module_utils.schema.definitions import *
except ImportError:
    from module_utils.schema.definitions import *


try:
    from ansible.module_utils.schema.metainfobase import MetainfoBase
except ImportError:
    from module_utils.schema.metainfobase import MetainfoBase

class QualitySchema(MetainfoBase):
    """
    The root schema is the schema that comprises the entire JSON document.
    """
    class _mcscan:
            class _summary:



                    _types_map = {
                        'Clean': {'type': int, 'subtype': None},
                        'Not_Scanned': {'type': int, 'subtype': None},
                        'Objects_Possibly_Infected': {'type': int, 'subtype': None},
                        'Possibly_Infected': {'type': int, 'subtype': None},
                        'Total_Objects': {'type': int, 'subtype': None},
                        'Total_files': {'type': int, 'subtype': None},
                    }
                    _formats_map = {
                    }
                    _validations_map = {
                        'Clean': { 'required': False,},
                        'Not_Scanned': { 'required': False,},
                        'Objects_Possibly_Infected': { 'required': False,},
                        'Possibly_Infected': { 'required': False,},
                        'Total_Objects': { 'required': False,},
                        'Total_files': { 'required': False,},
                    }

                    def __init__(self
                            , Clean=None
                            , Not_Scanned=None
                            , Objects_Possibly_Infected=None
                            , Possibly_Infected=None
                            , Total_Objects=None
                            , Total_files=None
                            ):
                        self.__Clean = Clean
                        self.__Not_Scanned = Not_Scanned
                        self.__Objects_Possibly_Infected = Objects_Possibly_Infected
                        self.__Possibly_Infected = Possibly_Infected
                        self.__Total_Objects = Total_Objects
                        self.__Total_files = Total_files
                        pass

                    def _get_Clean(self):
                        return self.__Clean
                    def _set_Clean(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("Clean must be int")

                        self.__Clean = value
                    Clean = property(_get_Clean, _set_Clean)

                    def _get_Not_Scanned(self):
                        return self.__Not_Scanned
                    def _set_Not_Scanned(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("Not_Scanned must be int")

                        self.__Not_Scanned = value
                    Not_Scanned = property(_get_Not_Scanned, _set_Not_Scanned)

                    def _get_Objects_Possibly_Infected(self):
                        return self.__Objects_Possibly_Infected
                    def _set_Objects_Possibly_Infected(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("Objects_Possibly_Infected must be int")

                        self.__Objects_Possibly_Infected = value
                    Objects_Possibly_Infected = property(_get_Objects_Possibly_Infected, _set_Objects_Possibly_Infected)

                    def _get_Possibly_Infected(self):
                        return self.__Possibly_Infected
                    def _set_Possibly_Infected(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("Possibly_Infected must be int")

                        self.__Possibly_Infected = value
                    Possibly_Infected = property(_get_Possibly_Infected, _set_Possibly_Infected)

                    def _get_Total_Objects(self):
                        return self.__Total_Objects
                    def _set_Total_Objects(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("Total_Objects must be int")

                        self.__Total_Objects = value
                    Total_Objects = property(_get_Total_Objects, _set_Total_Objects)

                    def _get_Total_files(self):
                        return self.__Total_files
                    def _set_Total_files(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("Total_files must be int")

                        self.__Total_files = value
                    Total_files = property(_get_Total_files, _set_Total_files)


                    @staticmethod
                    def from_dict(d):
                        v = {}
                        if "Clean" in d:
                            v["Clean"] = int.from_dict(d["Clean"]) if hasattr(int, 'from_dict') else d["Clean"]
                        if "Not-Scanned" in d:
                            v["Not_Scanned"] = int.from_dict(d["Not-Scanned"]) if hasattr(int, 'from_dict') else d["Not-Scanned"]
                        if "Objects-Possibly-Infected" in d:
                            v["Objects_Possibly_Infected"] = int.from_dict(d["Objects-Possibly-Infected"]) if hasattr(int, 'from_dict') else d["Objects-Possibly-Infected"]
                        if "Possibly-Infected" in d:
                            v["Possibly_Infected"] = int.from_dict(d["Possibly-Infected"]) if hasattr(int, 'from_dict') else d["Possibly-Infected"]
                        if "Total-Objects" in d:
                            v["Total_Objects"] = int.from_dict(d["Total-Objects"]) if hasattr(int, 'from_dict') else d["Total-Objects"]
                        if "Total-files" in d:
                            v["Total_files"] = int.from_dict(d["Total-files"]) if hasattr(int, 'from_dict') else d["Total-files"]
                        return QualitySchema._mcscan._summary(**v)


                    def as_dict(self):
                        d = {}
                        if self.__Clean is not None:
                            d['Clean'] = self.__Clean.as_dict() if hasattr(self.__Clean, 'as_dict') else self.__Clean
                        if self.__Not_Scanned is not None:
                            d['Not-Scanned'] = self.__Not_Scanned.as_dict() if hasattr(self.__Not_Scanned, 'as_dict') else self.__Not_Scanned
                        if self.__Objects_Possibly_Infected is not None:
                            d['Objects-Possibly-Infected'] = self.__Objects_Possibly_Infected.as_dict() if hasattr(self.__Objects_Possibly_Infected, 'as_dict') else self.__Objects_Possibly_Infected
                        if self.__Possibly_Infected is not None:
                            d['Possibly-Infected'] = self.__Possibly_Infected.as_dict() if hasattr(self.__Possibly_Infected, 'as_dict') else self.__Possibly_Infected
                        if self.__Total_Objects is not None:
                            d['Total-Objects'] = self.__Total_Objects.as_dict() if hasattr(self.__Total_Objects, 'as_dict') else self.__Total_Objects
                        if self.__Total_files is not None:
                            d['Total-files'] = self.__Total_files.as_dict() if hasattr(self.__Total_files, 'as_dict') else self.__Total_files
                        return d

                    def __repr__(self):
                        return "<Class _summary. Clean: {}, Not_Scanned: {}, Objects_Possibly_Infected: {}, Possibly_Infected: {}, Total_Objects: {}, Total_files: {}>".format(limitedRepr(self.__Clean[:20] if isinstance(self.__Clean, bytes) else self.__Clean), limitedRepr(self.__Not_Scanned[:20] if isinstance(self.__Not_Scanned, bytes) else self.__Not_Scanned), limitedRepr(self.__Objects_Possibly_Infected[:20] if isinstance(self.__Objects_Possibly_Infected, bytes) else self.__Objects_Possibly_Infected), limitedRepr(self.__Possibly_Infected[:20] if isinstance(self.__Possibly_Infected, bytes) else self.__Possibly_Infected), limitedRepr(self.__Total_Objects[:20] if isinstance(self.__Total_Objects, bytes) else self.__Total_Objects), limitedRepr(self.__Total_files[:20] if isinstance(self.__Total_files, bytes) else self.__Total_files))




            _types_map = {
                'summary': {'type': _summary, 'subtype': None},
            }
            _formats_map = {
            }
            _validations_map = {
                'summary': { 'required': False,},
            }

            def __init__(self
                    , summary=None
                    ):
                self.__summary = summary
                pass

            def _get_summary(self):
                return self.__summary
            def _set_summary(self, value):
                if value is not None and  not isinstance(value, QualitySchema._mcscan._summary):
                    raise TypeError("summary must be QualitySchema._mcscan._summary")

                self.__summary = value
            summary = property(_get_summary, _set_summary)


            @staticmethod
            def from_dict(d):
                v = {}
                if "summary" in d:
                    v["summary"] = QualitySchema._mcscan._summary.from_dict(d["summary"]) if hasattr(QualitySchema._mcscan._summary, 'from_dict') else d["summary"]
                return QualitySchema._mcscan(**v)


            def as_dict(self):
                d = {}
                if self.__summary is not None:
                    d['summary'] = self.__summary.as_dict() if hasattr(self.__summary, 'as_dict') else self.__summary
                return d

            def __repr__(self):
                return "<Class _mcscan. summary: {}>".format(limitedRepr(self.__summary[:20] if isinstance(self.__summary, bytes) else self.__summary))

    class _sonar:
            class _complexity:



                    _types_map = {
                        'complexity': {'type': int, 'subtype': None},
                        'file_complexity': {'type': int, 'subtype': None},
                        'complexity_in_classes': {'type': int, 'subtype': None},
                        'class_complexity': {'type': int, 'subtype': None},
                        'complexity_in_functions': {'type': int, 'subtype': None},
                        'function_complexity': {'type': int, 'subtype': None},
                        'cognitive_complexity': {'type': int, 'subtype': None},
                    }
                    _formats_map = {
                    }
                    _validations_map = {
                        'complexity': { 'required': False,},
                        'file_complexity': { 'required': False,},
                        'complexity_in_classes': { 'required': False,},
                        'class_complexity': { 'required': False,},
                        'complexity_in_functions': { 'required': False,},
                        'function_complexity': { 'required': False,},
                        'cognitive_complexity': { 'required': False,},
                    }

                    def __init__(self
                            , complexity=None
                            , file_complexity=None
                            , complexity_in_classes=None
                            , class_complexity=None
                            , complexity_in_functions=None
                            , function_complexity=None
                            , cognitive_complexity=None
                            ):
                        """
                        :param complexity: Cyclomatic complexity
                        :param file_complexity: Complexity average by file
                        :param complexity_in_classes: Cyclomatic complexity in classes
                        :param class_complexity: Complexity average by class
                        :param complexity_in_functions: Cyclomatic complexity in functions
                        :param function_complexity: Complexity average by function
                        """
                        self.__complexity = complexity
                        self.__file_complexity = file_complexity
                        self.__complexity_in_classes = complexity_in_classes
                        self.__class_complexity = class_complexity
                        self.__complexity_in_functions = complexity_in_functions
                        self.__function_complexity = function_complexity
                        self.__cognitive_complexity = cognitive_complexity
                        pass

                    def _get_complexity(self):
                        return self.__complexity
                    def _set_complexity(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("complexity must be int")

                        self.__complexity = value
                    complexity = property(_get_complexity, _set_complexity)
                    """
                    Cyclomatic complexity
                    """

                    def _get_file_complexity(self):
                        return self.__file_complexity
                    def _set_file_complexity(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("file_complexity must be int")

                        self.__file_complexity = value
                    file_complexity = property(_get_file_complexity, _set_file_complexity)
                    """
                    Complexity average by file
                    """

                    def _get_complexity_in_classes(self):
                        return self.__complexity_in_classes
                    def _set_complexity_in_classes(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("complexity_in_classes must be int")

                        self.__complexity_in_classes = value
                    complexity_in_classes = property(_get_complexity_in_classes, _set_complexity_in_classes)
                    """
                    Cyclomatic complexity in classes
                    """

                    def _get_class_complexity(self):
                        return self.__class_complexity
                    def _set_class_complexity(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("class_complexity must be int")

                        self.__class_complexity = value
                    class_complexity = property(_get_class_complexity, _set_class_complexity)
                    """
                    Complexity average by class
                    """

                    def _get_complexity_in_functions(self):
                        return self.__complexity_in_functions
                    def _set_complexity_in_functions(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("complexity_in_functions must be int")

                        self.__complexity_in_functions = value
                    complexity_in_functions = property(_get_complexity_in_functions, _set_complexity_in_functions)
                    """
                    Cyclomatic complexity in functions
                    """

                    def _get_function_complexity(self):
                        return self.__function_complexity
                    def _set_function_complexity(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("function_complexity must be int")

                        self.__function_complexity = value
                    function_complexity = property(_get_function_complexity, _set_function_complexity)
                    """
                    Complexity average by function
                    """

                    def _get_cognitive_complexity(self):
                        return self.__cognitive_complexity
                    def _set_cognitive_complexity(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("cognitive_complexity must be int")

                        self.__cognitive_complexity = value
                    cognitive_complexity = property(_get_cognitive_complexity, _set_cognitive_complexity)


                    @staticmethod
                    def from_dict(d):
                        v = {}
                        if "complexity" in d:
                            v["complexity"] = int.from_dict(d["complexity"]) if hasattr(int, 'from_dict') else d["complexity"]
                        if "file_complexity" in d:
                            v["file_complexity"] = int.from_dict(d["file_complexity"]) if hasattr(int, 'from_dict') else d["file_complexity"]
                        if "complexity_in_classes" in d:
                            v["complexity_in_classes"] = int.from_dict(d["complexity_in_classes"]) if hasattr(int, 'from_dict') else d["complexity_in_classes"]
                        if "class_complexity" in d:
                            v["class_complexity"] = int.from_dict(d["class_complexity"]) if hasattr(int, 'from_dict') else d["class_complexity"]
                        if "complexity_in_functions" in d:
                            v["complexity_in_functions"] = int.from_dict(d["complexity_in_functions"]) if hasattr(int, 'from_dict') else d["complexity_in_functions"]
                        if "function_complexity" in d:
                            v["function_complexity"] = int.from_dict(d["function_complexity"]) if hasattr(int, 'from_dict') else d["function_complexity"]
                        if "cognitive_complexity" in d:
                            v["cognitive_complexity"] = int.from_dict(d["cognitive_complexity"]) if hasattr(int, 'from_dict') else d["cognitive_complexity"]
                        return QualitySchema._sonar._complexity(**v)


                    def as_dict(self):
                        d = {}
                        if self.__complexity is not None:
                            d['complexity'] = self.__complexity.as_dict() if hasattr(self.__complexity, 'as_dict') else self.__complexity
                        if self.__file_complexity is not None:
                            d['file_complexity'] = self.__file_complexity.as_dict() if hasattr(self.__file_complexity, 'as_dict') else self.__file_complexity
                        if self.__complexity_in_classes is not None:
                            d['complexity_in_classes'] = self.__complexity_in_classes.as_dict() if hasattr(self.__complexity_in_classes, 'as_dict') else self.__complexity_in_classes
                        if self.__class_complexity is not None:
                            d['class_complexity'] = self.__class_complexity.as_dict() if hasattr(self.__class_complexity, 'as_dict') else self.__class_complexity
                        if self.__complexity_in_functions is not None:
                            d['complexity_in_functions'] = self.__complexity_in_functions.as_dict() if hasattr(self.__complexity_in_functions, 'as_dict') else self.__complexity_in_functions
                        if self.__function_complexity is not None:
                            d['function_complexity'] = self.__function_complexity.as_dict() if hasattr(self.__function_complexity, 'as_dict') else self.__function_complexity
                        if self.__cognitive_complexity is not None:
                            d['cognitive_complexity'] = self.__cognitive_complexity.as_dict() if hasattr(self.__cognitive_complexity, 'as_dict') else self.__cognitive_complexity
                        return d

                    def __repr__(self):
                        return "<Class _complexity. complexity: {}, file_complexity: {}, complexity_in_classes: {}, class_complexity: {}, complexity_in_functions: {}, function_complexity: {}, cognitive_complexity: {}>".format(limitedRepr(self.__complexity[:20] if isinstance(self.__complexity, bytes) else self.__complexity), limitedRepr(self.__file_complexity[:20] if isinstance(self.__file_complexity, bytes) else self.__file_complexity), limitedRepr(self.__complexity_in_classes[:20] if isinstance(self.__complexity_in_classes, bytes) else self.__complexity_in_classes), limitedRepr(self.__class_complexity[:20] if isinstance(self.__class_complexity, bytes) else self.__class_complexity), limitedRepr(self.__complexity_in_functions[:20] if isinstance(self.__complexity_in_functions, bytes) else self.__complexity_in_functions), limitedRepr(self.__function_complexity[:20] if isinstance(self.__function_complexity, bytes) else self.__function_complexity), limitedRepr(self.__cognitive_complexity[:20] if isinstance(self.__cognitive_complexity, bytes) else self.__cognitive_complexity))

            class _coverage:



                    _types_map = {
                        'tests': {'type': int, 'subtype': None},
                        'test_execution_time': {'type': int, 'subtype': None},
                        'test_errors': {'type': int, 'subtype': None},
                        'skipped_tests': {'type': int, 'subtype': None},
                        'test_failures': {'type': int, 'subtype': None},
                        'coverage': {'type': float, 'subtype': None},
                        'lines_to_cover': {'type': int, 'subtype': None},
                        'uncovered_lines': {'type': int, 'subtype': None},
                        'line_coverage': {'type': float, 'subtype': None},
                        'conditions_to_cover': {'type': int, 'subtype': None},
                        'uncovered_conditions': {'type': int, 'subtype': None},
                        'branch_coverage': {'type': int, 'subtype': None},
                    }
                    _formats_map = {
                    }
                    _validations_map = {
                        'tests': { 'required': False,},
                        'test_execution_time': { 'required': False,},
                        'test_errors': { 'required': False,},
                        'skipped_tests': { 'required': False,},
                        'test_failures': { 'required': False,},
                        'coverage': { 'required': False,},
                        'lines_to_cover': { 'required': False,},
                        'uncovered_lines': { 'required': False,},
                        'line_coverage': { 'required': False,},
                        'conditions_to_cover': { 'required': False,},
                        'uncovered_conditions': { 'required': False,},
                        'branch_coverage': { 'required': False,},
                    }

                    def __init__(self
                            , tests=None
                            , test_execution_time=None
                            , test_errors=None
                            , skipped_tests=None
                            , test_failures=None
                            , coverage=None
                            , lines_to_cover=None
                            , uncovered_lines=None
                            , line_coverage=None
                            , conditions_to_cover=None
                            , uncovered_conditions=None
                            , branch_coverage=None
                            ):
                        """
                        :param tests: Number of unit tests
                        :param test_execution_time: Execution duration of unit tests
                        :param test_errors: Number of unit test errors
                        :param skipped_tests: Number of skipped unit tests
                        :param test_failures: Number of unit test failures
                        :param coverage: Coverage by tests
                        :param lines_to_cover: Lines to cover
                        :param uncovered_lines: Uncovered lines
                        :param line_coverage: Line coverage
                        :param conditions_to_cover: Conditions to cover
                        :param uncovered_conditions: Uncovered conditions
                        :param branch_coverage: Condition coverage
                        """
                        self.__tests = tests
                        self.__test_execution_time = test_execution_time
                        self.__test_errors = test_errors
                        self.__skipped_tests = skipped_tests
                        self.__test_failures = test_failures
                        self.__coverage = coverage
                        self.__lines_to_cover = lines_to_cover
                        self.__uncovered_lines = uncovered_lines
                        self.__line_coverage = line_coverage
                        self.__conditions_to_cover = conditions_to_cover
                        self.__uncovered_conditions = uncovered_conditions
                        self.__branch_coverage = branch_coverage
                        pass

                    def _get_tests(self):
                        return self.__tests
                    def _set_tests(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("tests must be int")

                        self.__tests = value
                    tests = property(_get_tests, _set_tests)
                    """
                    Number of unit tests
                    """

                    def _get_test_execution_time(self):
                        return self.__test_execution_time
                    def _set_test_execution_time(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("test_execution_time must be int")

                        self.__test_execution_time = value
                    test_execution_time = property(_get_test_execution_time, _set_test_execution_time)
                    """
                    Execution duration of unit tests
                    """

                    def _get_test_errors(self):
                        return self.__test_errors
                    def _set_test_errors(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("test_errors must be int")

                        self.__test_errors = value
                    test_errors = property(_get_test_errors, _set_test_errors)
                    """
                    Number of unit test errors
                    """

                    def _get_skipped_tests(self):
                        return self.__skipped_tests
                    def _set_skipped_tests(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("skipped_tests must be int")

                        self.__skipped_tests = value
                    skipped_tests = property(_get_skipped_tests, _set_skipped_tests)
                    """
                    Number of skipped unit tests
                    """

                    def _get_test_failures(self):
                        return self.__test_failures
                    def _set_test_failures(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("test_failures must be int")

                        self.__test_failures = value
                    test_failures = property(_get_test_failures, _set_test_failures)
                    """
                    Number of unit test failures
                    """

                    def _get_coverage(self):
                        return self.__coverage
                    def _set_coverage(self, value):
                        if value is not None and  not isinstance(value, float):
                            raise TypeError("coverage must be float")

                        self.__coverage = value
                    coverage = property(_get_coverage, _set_coverage)
                    """
                    Coverage by tests
                    """

                    def _get_lines_to_cover(self):
                        return self.__lines_to_cover
                    def _set_lines_to_cover(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("lines_to_cover must be int")

                        self.__lines_to_cover = value
                    lines_to_cover = property(_get_lines_to_cover, _set_lines_to_cover)
                    """
                    Lines to cover
                    """

                    def _get_uncovered_lines(self):
                        return self.__uncovered_lines
                    def _set_uncovered_lines(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("uncovered_lines must be int")

                        self.__uncovered_lines = value
                    uncovered_lines = property(_get_uncovered_lines, _set_uncovered_lines)
                    """
                    Uncovered lines
                    """

                    def _get_line_coverage(self):
                        return self.__line_coverage
                    def _set_line_coverage(self, value):
                        if value is not None and  not isinstance(value, float):
                            raise TypeError("line_coverage must be float")

                        self.__line_coverage = value
                    line_coverage = property(_get_line_coverage, _set_line_coverage)
                    """
                    Line coverage
                    """

                    def _get_conditions_to_cover(self):
                        return self.__conditions_to_cover
                    def _set_conditions_to_cover(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("conditions_to_cover must be int")

                        self.__conditions_to_cover = value
                    conditions_to_cover = property(_get_conditions_to_cover, _set_conditions_to_cover)
                    """
                    Conditions to cover
                    """

                    def _get_uncovered_conditions(self):
                        return self.__uncovered_conditions
                    def _set_uncovered_conditions(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("uncovered_conditions must be int")

                        self.__uncovered_conditions = value
                    uncovered_conditions = property(_get_uncovered_conditions, _set_uncovered_conditions)
                    """
                    Uncovered conditions
                    """

                    def _get_branch_coverage(self):
                        return self.__branch_coverage
                    def _set_branch_coverage(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("branch_coverage must be int")

                        self.__branch_coverage = value
                    branch_coverage = property(_get_branch_coverage, _set_branch_coverage)
                    """
                    Condition coverage
                    """


                    @staticmethod
                    def from_dict(d):
                        v = {}
                        if "tests" in d:
                            v["tests"] = int.from_dict(d["tests"]) if hasattr(int, 'from_dict') else d["tests"]
                        if "test_execution_time" in d:
                            v["test_execution_time"] = int.from_dict(d["test_execution_time"]) if hasattr(int, 'from_dict') else d["test_execution_time"]
                        if "test_errors" in d:
                            v["test_errors"] = int.from_dict(d["test_errors"]) if hasattr(int, 'from_dict') else d["test_errors"]
                        if "skipped_tests" in d:
                            v["skipped_tests"] = int.from_dict(d["skipped_tests"]) if hasattr(int, 'from_dict') else d["skipped_tests"]
                        if "test_failures" in d:
                            v["test_failures"] = int.from_dict(d["test_failures"]) if hasattr(int, 'from_dict') else d["test_failures"]
                        if "coverage" in d:
                            v["coverage"] = float.from_dict(d["coverage"]) if hasattr(float, 'from_dict') else d["coverage"]
                        if "lines_to_cover" in d:
                            v["lines_to_cover"] = int.from_dict(d["lines_to_cover"]) if hasattr(int, 'from_dict') else d["lines_to_cover"]
                        if "uncovered_lines" in d:
                            v["uncovered_lines"] = int.from_dict(d["uncovered_lines"]) if hasattr(int, 'from_dict') else d["uncovered_lines"]
                        if "line_coverage" in d:
                            v["line_coverage"] = float.from_dict(d["line_coverage"]) if hasattr(float, 'from_dict') else d["line_coverage"]
                        if "conditions_to_cover" in d:
                            v["conditions_to_cover"] = int.from_dict(d["conditions_to_cover"]) if hasattr(int, 'from_dict') else d["conditions_to_cover"]
                        if "uncovered_conditions" in d:
                            v["uncovered_conditions"] = int.from_dict(d["uncovered_conditions"]) if hasattr(int, 'from_dict') else d["uncovered_conditions"]
                        if "branch_coverage" in d:
                            v["branch_coverage"] = int.from_dict(d["branch_coverage"]) if hasattr(int, 'from_dict') else d["branch_coverage"]
                        return QualitySchema._sonar._coverage(**v)


                    def as_dict(self):
                        d = {}
                        if self.__tests is not None:
                            d['tests'] = self.__tests.as_dict() if hasattr(self.__tests, 'as_dict') else self.__tests
                        if self.__test_execution_time is not None:
                            d['test_execution_time'] = self.__test_execution_time.as_dict() if hasattr(self.__test_execution_time, 'as_dict') else self.__test_execution_time
                        if self.__test_errors is not None:
                            d['test_errors'] = self.__test_errors.as_dict() if hasattr(self.__test_errors, 'as_dict') else self.__test_errors
                        if self.__skipped_tests is not None:
                            d['skipped_tests'] = self.__skipped_tests.as_dict() if hasattr(self.__skipped_tests, 'as_dict') else self.__skipped_tests
                        if self.__test_failures is not None:
                            d['test_failures'] = self.__test_failures.as_dict() if hasattr(self.__test_failures, 'as_dict') else self.__test_failures
                        if self.__coverage is not None:
                            d['coverage'] = self.__coverage.as_dict() if hasattr(self.__coverage, 'as_dict') else self.__coverage
                        if self.__lines_to_cover is not None:
                            d['lines_to_cover'] = self.__lines_to_cover.as_dict() if hasattr(self.__lines_to_cover, 'as_dict') else self.__lines_to_cover
                        if self.__uncovered_lines is not None:
                            d['uncovered_lines'] = self.__uncovered_lines.as_dict() if hasattr(self.__uncovered_lines, 'as_dict') else self.__uncovered_lines
                        if self.__line_coverage is not None:
                            d['line_coverage'] = self.__line_coverage.as_dict() if hasattr(self.__line_coverage, 'as_dict') else self.__line_coverage
                        if self.__conditions_to_cover is not None:
                            d['conditions_to_cover'] = self.__conditions_to_cover.as_dict() if hasattr(self.__conditions_to_cover, 'as_dict') else self.__conditions_to_cover
                        if self.__uncovered_conditions is not None:
                            d['uncovered_conditions'] = self.__uncovered_conditions.as_dict() if hasattr(self.__uncovered_conditions, 'as_dict') else self.__uncovered_conditions
                        if self.__branch_coverage is not None:
                            d['branch_coverage'] = self.__branch_coverage.as_dict() if hasattr(self.__branch_coverage, 'as_dict') else self.__branch_coverage
                        return d

                    def __repr__(self):
                        return "<Class _coverage. tests: {}, test_execution_time: {}, test_errors: {}, skipped_tests: {}, test_failures: {}, coverage: {}, lines_to_cover: {}, uncovered_lines: {}, line_coverage: {}, conditions_to_cover: {}, uncovered_conditions: {}, branch_coverage: {}>".format(limitedRepr(self.__tests[:20] if isinstance(self.__tests, bytes) else self.__tests), limitedRepr(self.__test_execution_time[:20] if isinstance(self.__test_execution_time, bytes) else self.__test_execution_time), limitedRepr(self.__test_errors[:20] if isinstance(self.__test_errors, bytes) else self.__test_errors), limitedRepr(self.__skipped_tests[:20] if isinstance(self.__skipped_tests, bytes) else self.__skipped_tests), limitedRepr(self.__test_failures[:20] if isinstance(self.__test_failures, bytes) else self.__test_failures), limitedRepr(self.__coverage[:20] if isinstance(self.__coverage, bytes) else self.__coverage), limitedRepr(self.__lines_to_cover[:20] if isinstance(self.__lines_to_cover, bytes) else self.__lines_to_cover), limitedRepr(self.__uncovered_lines[:20] if isinstance(self.__uncovered_lines, bytes) else self.__uncovered_lines), limitedRepr(self.__line_coverage[:20] if isinstance(self.__line_coverage, bytes) else self.__line_coverage), limitedRepr(self.__conditions_to_cover[:20] if isinstance(self.__conditions_to_cover, bytes) else self.__conditions_to_cover), limitedRepr(self.__uncovered_conditions[:20] if isinstance(self.__uncovered_conditions, bytes) else self.__uncovered_conditions), limitedRepr(self.__branch_coverage[:20] if isinstance(self.__branch_coverage, bytes) else self.__branch_coverage))

            class _documentation:



                    _types_map = {
                        'public_api': {'type': int, 'subtype': None},
                        'public_undocumented_api': {'type': int, 'subtype': None},
                    }
                    _formats_map = {
                    }
                    _validations_map = {
                        'public_api': { 'required': False,},
                        'public_undocumented_api': { 'required': False,},
                    }

                    def __init__(self
                            , public_api=None
                            , public_undocumented_api=None
                            ):
                        """
                        :param public_api: Public API
                        :param public_undocumented_api: Public undocumented classes, functions and variables
                        """
                        self.__public_api = public_api
                        self.__public_undocumented_api = public_undocumented_api
                        pass

                    def _get_public_api(self):
                        return self.__public_api
                    def _set_public_api(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("public_api must be int")

                        self.__public_api = value
                    public_api = property(_get_public_api, _set_public_api)
                    """
                    Public API
                    """

                    def _get_public_undocumented_api(self):
                        return self.__public_undocumented_api
                    def _set_public_undocumented_api(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("public_undocumented_api must be int")

                        self.__public_undocumented_api = value
                    public_undocumented_api = property(_get_public_undocumented_api, _set_public_undocumented_api)
                    """
                    Public undocumented classes, functions and variables
                    """


                    @staticmethod
                    def from_dict(d):
                        v = {}
                        if "public_api" in d:
                            v["public_api"] = int.from_dict(d["public_api"]) if hasattr(int, 'from_dict') else d["public_api"]
                        if "public_undocumented_api" in d:
                            v["public_undocumented_api"] = int.from_dict(d["public_undocumented_api"]) if hasattr(int, 'from_dict') else d["public_undocumented_api"]
                        return QualitySchema._sonar._documentation(**v)


                    def as_dict(self):
                        d = {}
                        if self.__public_api is not None:
                            d['public_api'] = self.__public_api.as_dict() if hasattr(self.__public_api, 'as_dict') else self.__public_api
                        if self.__public_undocumented_api is not None:
                            d['public_undocumented_api'] = self.__public_undocumented_api.as_dict() if hasattr(self.__public_undocumented_api, 'as_dict') else self.__public_undocumented_api
                        return d

                    def __repr__(self):
                        return "<Class _documentation. public_api: {}, public_undocumented_api: {}>".format(limitedRepr(self.__public_api[:20] if isinstance(self.__public_api, bytes) else self.__public_api), limitedRepr(self.__public_undocumented_api[:20] if isinstance(self.__public_undocumented_api, bytes) else self.__public_undocumented_api))

            class _duplications:



                    _types_map = {
                        'duplicated_lines': {'type': int, 'subtype': None},
                        'duplicated_blocks': {'type': int, 'subtype': None},
                        'duplicated_files': {'type': int, 'subtype': None},
                    }
                    _formats_map = {
                    }
                    _validations_map = {
                        'duplicated_lines': { 'required': False,},
                        'duplicated_blocks': { 'required': False,},
                        'duplicated_files': { 'required': False,},
                    }

                    def __init__(self
                            , duplicated_lines=None
                            , duplicated_blocks=None
                            , duplicated_files=None
                            ):
                        """
                        :param duplicated_lines: Duplicated lines
                        :param duplicated_blocks: Duplicated blocks
                        :param duplicated_files: Duplicated files
                        """
                        self.__duplicated_lines = duplicated_lines
                        self.__duplicated_blocks = duplicated_blocks
                        self.__duplicated_files = duplicated_files
                        pass

                    def _get_duplicated_lines(self):
                        return self.__duplicated_lines
                    def _set_duplicated_lines(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("duplicated_lines must be int")

                        self.__duplicated_lines = value
                    duplicated_lines = property(_get_duplicated_lines, _set_duplicated_lines)
                    """
                    Duplicated lines
                    """

                    def _get_duplicated_blocks(self):
                        return self.__duplicated_blocks
                    def _set_duplicated_blocks(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("duplicated_blocks must be int")

                        self.__duplicated_blocks = value
                    duplicated_blocks = property(_get_duplicated_blocks, _set_duplicated_blocks)
                    """
                    Duplicated blocks
                    """

                    def _get_duplicated_files(self):
                        return self.__duplicated_files
                    def _set_duplicated_files(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("duplicated_files must be int")

                        self.__duplicated_files = value
                    duplicated_files = property(_get_duplicated_files, _set_duplicated_files)
                    """
                    Duplicated files
                    """


                    @staticmethod
                    def from_dict(d):
                        v = {}
                        if "duplicated_lines" in d:
                            v["duplicated_lines"] = int.from_dict(d["duplicated_lines"]) if hasattr(int, 'from_dict') else d["duplicated_lines"]
                        if "duplicated_blocks" in d:
                            v["duplicated_blocks"] = int.from_dict(d["duplicated_blocks"]) if hasattr(int, 'from_dict') else d["duplicated_blocks"]
                        if "duplicated_files" in d:
                            v["duplicated_files"] = int.from_dict(d["duplicated_files"]) if hasattr(int, 'from_dict') else d["duplicated_files"]
                        return QualitySchema._sonar._duplications(**v)


                    def as_dict(self):
                        d = {}
                        if self.__duplicated_lines is not None:
                            d['duplicated_lines'] = self.__duplicated_lines.as_dict() if hasattr(self.__duplicated_lines, 'as_dict') else self.__duplicated_lines
                        if self.__duplicated_blocks is not None:
                            d['duplicated_blocks'] = self.__duplicated_blocks.as_dict() if hasattr(self.__duplicated_blocks, 'as_dict') else self.__duplicated_blocks
                        if self.__duplicated_files is not None:
                            d['duplicated_files'] = self.__duplicated_files.as_dict() if hasattr(self.__duplicated_files, 'as_dict') else self.__duplicated_files
                        return d

                    def __repr__(self):
                        return "<Class _duplications. duplicated_lines: {}, duplicated_blocks: {}, duplicated_files: {}>".format(limitedRepr(self.__duplicated_lines[:20] if isinstance(self.__duplicated_lines, bytes) else self.__duplicated_lines), limitedRepr(self.__duplicated_blocks[:20] if isinstance(self.__duplicated_blocks, bytes) else self.__duplicated_blocks), limitedRepr(self.__duplicated_files[:20] if isinstance(self.__duplicated_files, bytes) else self.__duplicated_files))

            class _general:



                    _types_map = {
                        'quality_gate_details': {'type': str, 'subtype': None},
                        'quality_profiles': {'type': str, 'subtype': None},
                    }
                    _formats_map = {
                    }
                    _validations_map = {
                        'quality_gate_details': { 'required': False,},
                        'quality_profiles': { 'required': False,},
                    }

                    def __init__(self
                            , quality_gate_details=None
                            , quality_profiles=None
                            ):
                        self.__quality_gate_details = quality_gate_details
                        self.__quality_profiles = quality_profiles
                        pass

                    def _get_quality_gate_details(self):
                        return self.__quality_gate_details
                    def _set_quality_gate_details(self, value):
                        if value is not None and  not isinstance(value, str):
                            raise TypeError("quality_gate_details must be str")

                        self.__quality_gate_details = value
                    quality_gate_details = property(_get_quality_gate_details, _set_quality_gate_details)

                    def _get_quality_profiles(self):
                        return self.__quality_profiles
                    def _set_quality_profiles(self, value):
                        if value is not None and  not isinstance(value, str):
                            raise TypeError("quality_profiles must be str")

                        self.__quality_profiles = value
                    quality_profiles = property(_get_quality_profiles, _set_quality_profiles)


                    @staticmethod
                    def from_dict(d):
                        v = {}
                        if "quality_gate_details" in d:
                            v["quality_gate_details"] = str.from_dict(d["quality_gate_details"]) if hasattr(str, 'from_dict') else d["quality_gate_details"]
                        if "quality_profiles" in d:
                            v["quality_profiles"] = str.from_dict(d["quality_profiles"]) if hasattr(str, 'from_dict') else d["quality_profiles"]
                        return QualitySchema._sonar._general(**v)


                    def as_dict(self):
                        d = {}
                        if self.__quality_gate_details is not None:
                            d['quality_gate_details'] = self.__quality_gate_details.as_dict() if hasattr(self.__quality_gate_details, 'as_dict') else self.__quality_gate_details
                        if self.__quality_profiles is not None:
                            d['quality_profiles'] = self.__quality_profiles.as_dict() if hasattr(self.__quality_profiles, 'as_dict') else self.__quality_profiles
                        return d

                    def __repr__(self):
                        return "<Class _general. quality_gate_details: {}, quality_profiles: {}>".format(limitedRepr(self.__quality_gate_details[:20] if isinstance(self.__quality_gate_details, bytes) else self.__quality_gate_details), limitedRepr(self.__quality_profiles[:20] if isinstance(self.__quality_profiles, bytes) else self.__quality_profiles))

            class _issues:



                    _types_map = {
                        'violations': {'type': int, 'subtype': None},
                        'blocker_violations': {'type': int, 'subtype': None},
                        'critical_violations': {'type': int, 'subtype': None},
                        'major_violations': {'type': int, 'subtype': None},
                        'minor_violations': {'type': int, 'subtype': None},
                        'info_violations': {'type': int, 'subtype': None},
                        'false_positive_issues': {'type': int, 'subtype': None},
                        'wont_fix_issues': {'type': int, 'subtype': None},
                        'open_issues': {'type': int, 'subtype': None},
                        'reopened_issues': {'type': int, 'subtype': None},
                        'confirmed_issues': {'type': int, 'subtype': None},
                    }
                    _formats_map = {
                    }
                    _validations_map = {
                        'violations': { 'required': False,},
                        'blocker_violations': { 'required': False,},
                        'critical_violations': { 'required': False,},
                        'major_violations': { 'required': False,},
                        'minor_violations': { 'required': False,},
                        'info_violations': { 'required': False,},
                        'false_positive_issues': { 'required': False,},
                        'wont_fix_issues': { 'required': False,},
                        'open_issues': { 'required': False,},
                        'reopened_issues': { 'required': False,},
                        'confirmed_issues': { 'required': False,},
                    }

                    def __init__(self
                            , violations=None
                            , blocker_violations=None
                            , critical_violations=None
                            , major_violations=None
                            , minor_violations=None
                            , info_violations=None
                            , false_positive_issues=None
                            , wont_fix_issues=None
                            , open_issues=None
                            , reopened_issues=None
                            , confirmed_issues=None
                            ):
                        """
                        :param violations: Issues
                        :param blocker_violations: Blocker issues
                        :param critical_violations: Critical issues
                        :param major_violations: Major issues
                        :param minor_violations: Minor issues
                        :param info_violations: Info issues
                        :param false_positive_issues: False positive issues
                        :param wont_fix_issues: Won't fix issues
                        :param open_issues: Open issues
                        :param reopened_issues: Reopened issues
                        :param confirmed_issues: Confirmed issues
                        """
                        self.__violations = violations
                        self.__blocker_violations = blocker_violations
                        self.__critical_violations = critical_violations
                        self.__major_violations = major_violations
                        self.__minor_violations = minor_violations
                        self.__info_violations = info_violations
                        self.__false_positive_issues = false_positive_issues
                        self.__wont_fix_issues = wont_fix_issues
                        self.__open_issues = open_issues
                        self.__reopened_issues = reopened_issues
                        self.__confirmed_issues = confirmed_issues
                        pass

                    def _get_violations(self):
                        return self.__violations
                    def _set_violations(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("violations must be int")

                        self.__violations = value
                    violations = property(_get_violations, _set_violations)
                    """
                    Issues
                    """

                    def _get_blocker_violations(self):
                        return self.__blocker_violations
                    def _set_blocker_violations(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("blocker_violations must be int")

                        self.__blocker_violations = value
                    blocker_violations = property(_get_blocker_violations, _set_blocker_violations)
                    """
                    Blocker issues
                    """

                    def _get_critical_violations(self):
                        return self.__critical_violations
                    def _set_critical_violations(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("critical_violations must be int")

                        self.__critical_violations = value
                    critical_violations = property(_get_critical_violations, _set_critical_violations)
                    """
                    Critical issues
                    """

                    def _get_major_violations(self):
                        return self.__major_violations
                    def _set_major_violations(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("major_violations must be int")

                        self.__major_violations = value
                    major_violations = property(_get_major_violations, _set_major_violations)
                    """
                    Major issues
                    """

                    def _get_minor_violations(self):
                        return self.__minor_violations
                    def _set_minor_violations(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("minor_violations must be int")

                        self.__minor_violations = value
                    minor_violations = property(_get_minor_violations, _set_minor_violations)
                    """
                    Minor issues
                    """

                    def _get_info_violations(self):
                        return self.__info_violations
                    def _set_info_violations(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("info_violations must be int")

                        self.__info_violations = value
                    info_violations = property(_get_info_violations, _set_info_violations)
                    """
                    Info issues
                    """

                    def _get_false_positive_issues(self):
                        return self.__false_positive_issues
                    def _set_false_positive_issues(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("false_positive_issues must be int")

                        self.__false_positive_issues = value
                    false_positive_issues = property(_get_false_positive_issues, _set_false_positive_issues)
                    """
                    False positive issues
                    """

                    def _get_wont_fix_issues(self):
                        return self.__wont_fix_issues
                    def _set_wont_fix_issues(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("wont_fix_issues must be int")

                        self.__wont_fix_issues = value
                    wont_fix_issues = property(_get_wont_fix_issues, _set_wont_fix_issues)
                    """
                    Won't fix issues
                    """

                    def _get_open_issues(self):
                        return self.__open_issues
                    def _set_open_issues(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("open_issues must be int")

                        self.__open_issues = value
                    open_issues = property(_get_open_issues, _set_open_issues)
                    """
                    Open issues
                    """

                    def _get_reopened_issues(self):
                        return self.__reopened_issues
                    def _set_reopened_issues(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("reopened_issues must be int")

                        self.__reopened_issues = value
                    reopened_issues = property(_get_reopened_issues, _set_reopened_issues)
                    """
                    Reopened issues
                    """

                    def _get_confirmed_issues(self):
                        return self.__confirmed_issues
                    def _set_confirmed_issues(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("confirmed_issues must be int")

                        self.__confirmed_issues = value
                    confirmed_issues = property(_get_confirmed_issues, _set_confirmed_issues)
                    """
                    Confirmed issues
                    """


                    @staticmethod
                    def from_dict(d):
                        v = {}
                        if "violations" in d:
                            v["violations"] = int.from_dict(d["violations"]) if hasattr(int, 'from_dict') else d["violations"]
                        if "blocker_violations" in d:
                            v["blocker_violations"] = int.from_dict(d["blocker_violations"]) if hasattr(int, 'from_dict') else d["blocker_violations"]
                        if "critical_violations" in d:
                            v["critical_violations"] = int.from_dict(d["critical_violations"]) if hasattr(int, 'from_dict') else d["critical_violations"]
                        if "major_violations" in d:
                            v["major_violations"] = int.from_dict(d["major_violations"]) if hasattr(int, 'from_dict') else d["major_violations"]
                        if "minor_violations" in d:
                            v["minor_violations"] = int.from_dict(d["minor_violations"]) if hasattr(int, 'from_dict') else d["minor_violations"]
                        if "info_violations" in d:
                            v["info_violations"] = int.from_dict(d["info_violations"]) if hasattr(int, 'from_dict') else d["info_violations"]
                        if "false_positive_issues" in d:
                            v["false_positive_issues"] = int.from_dict(d["false_positive_issues"]) if hasattr(int, 'from_dict') else d["false_positive_issues"]
                        if "wont_fix_issues" in d:
                            v["wont_fix_issues"] = int.from_dict(d["wont_fix_issues"]) if hasattr(int, 'from_dict') else d["wont_fix_issues"]
                        if "open_issues" in d:
                            v["open_issues"] = int.from_dict(d["open_issues"]) if hasattr(int, 'from_dict') else d["open_issues"]
                        if "reopened_issues" in d:
                            v["reopened_issues"] = int.from_dict(d["reopened_issues"]) if hasattr(int, 'from_dict') else d["reopened_issues"]
                        if "confirmed_issues" in d:
                            v["confirmed_issues"] = int.from_dict(d["confirmed_issues"]) if hasattr(int, 'from_dict') else d["confirmed_issues"]
                        return QualitySchema._sonar._issues(**v)


                    def as_dict(self):
                        d = {}
                        if self.__violations is not None:
                            d['violations'] = self.__violations.as_dict() if hasattr(self.__violations, 'as_dict') else self.__violations
                        if self.__blocker_violations is not None:
                            d['blocker_violations'] = self.__blocker_violations.as_dict() if hasattr(self.__blocker_violations, 'as_dict') else self.__blocker_violations
                        if self.__critical_violations is not None:
                            d['critical_violations'] = self.__critical_violations.as_dict() if hasattr(self.__critical_violations, 'as_dict') else self.__critical_violations
                        if self.__major_violations is not None:
                            d['major_violations'] = self.__major_violations.as_dict() if hasattr(self.__major_violations, 'as_dict') else self.__major_violations
                        if self.__minor_violations is not None:
                            d['minor_violations'] = self.__minor_violations.as_dict() if hasattr(self.__minor_violations, 'as_dict') else self.__minor_violations
                        if self.__info_violations is not None:
                            d['info_violations'] = self.__info_violations.as_dict() if hasattr(self.__info_violations, 'as_dict') else self.__info_violations
                        if self.__false_positive_issues is not None:
                            d['false_positive_issues'] = self.__false_positive_issues.as_dict() if hasattr(self.__false_positive_issues, 'as_dict') else self.__false_positive_issues
                        if self.__wont_fix_issues is not None:
                            d['wont_fix_issues'] = self.__wont_fix_issues.as_dict() if hasattr(self.__wont_fix_issues, 'as_dict') else self.__wont_fix_issues
                        if self.__open_issues is not None:
                            d['open_issues'] = self.__open_issues.as_dict() if hasattr(self.__open_issues, 'as_dict') else self.__open_issues
                        if self.__reopened_issues is not None:
                            d['reopened_issues'] = self.__reopened_issues.as_dict() if hasattr(self.__reopened_issues, 'as_dict') else self.__reopened_issues
                        if self.__confirmed_issues is not None:
                            d['confirmed_issues'] = self.__confirmed_issues.as_dict() if hasattr(self.__confirmed_issues, 'as_dict') else self.__confirmed_issues
                        return d

                    def __repr__(self):
                        return "<Class _issues. violations: {}, blocker_violations: {}, critical_violations: {}, major_violations: {}, minor_violations: {}, info_violations: {}, false_positive_issues: {}, wont_fix_issues: {}, open_issues: {}, reopened_issues: {}, confirmed_issues: {}>".format(limitedRepr(self.__violations[:20] if isinstance(self.__violations, bytes) else self.__violations), limitedRepr(self.__blocker_violations[:20] if isinstance(self.__blocker_violations, bytes) else self.__blocker_violations), limitedRepr(self.__critical_violations[:20] if isinstance(self.__critical_violations, bytes) else self.__critical_violations), limitedRepr(self.__major_violations[:20] if isinstance(self.__major_violations, bytes) else self.__major_violations), limitedRepr(self.__minor_violations[:20] if isinstance(self.__minor_violations, bytes) else self.__minor_violations), limitedRepr(self.__info_violations[:20] if isinstance(self.__info_violations, bytes) else self.__info_violations), limitedRepr(self.__false_positive_issues[:20] if isinstance(self.__false_positive_issues, bytes) else self.__false_positive_issues), limitedRepr(self.__wont_fix_issues[:20] if isinstance(self.__wont_fix_issues, bytes) else self.__wont_fix_issues), limitedRepr(self.__open_issues[:20] if isinstance(self.__open_issues, bytes) else self.__open_issues), limitedRepr(self.__reopened_issues[:20] if isinstance(self.__reopened_issues, bytes) else self.__reopened_issues), limitedRepr(self.__confirmed_issues[:20] if isinstance(self.__confirmed_issues, bytes) else self.__confirmed_issues))

            class _maintainability:



                    _types_map = {
                        'code_smells': {'type': int, 'subtype': None},
                        'sqale_index': {'type': int, 'subtype': None},
                        'sqale_rating': {'type': float, 'subtype': None},
                        'development_cost': {'type': int, 'subtype': None},
                        'sqale_debt_ratio': {'type': float, 'subtype': None},
                        'effort_to_reach_maintainability_rating_a': {'type': int, 'subtype': None},
                    }
                    _formats_map = {
                    }
                    _validations_map = {
                        'code_smells': { 'required': False,},
                        'sqale_index': { 'required': False,},
                        'sqale_rating': { 'required': False,},
                        'development_cost': { 'required': False,},
                        'sqale_debt_ratio': { 'required': False,},
                        'effort_to_reach_maintainability_rating_a': { 'required': False,},
                    }

                    def __init__(self
                            , code_smells=None
                            , sqale_index=None
                            , sqale_rating=None
                            , development_cost=None
                            , sqale_debt_ratio=None
                            , effort_to_reach_maintainability_rating_a=None
                            ):
                        """
                        :param code_smells: Code Smells
                        :param sqale_index: Total effort (in hours) to fix all the issues on the component and therefore to comply to all the requirements.
                        :param sqale_rating: A-to-E rating based on the technical debt ratio
                        :param development_cost: Development cost
                        :param sqale_debt_ratio: Ratio of the actual technical debt compared to the estimated cost to develop the whole source code from scratch
                        :param effort_to_reach_maintainability_rating_a: Effort to reach maintainability rating A
                        """
                        self.__code_smells = code_smells
                        self.__sqale_index = sqale_index
                        self.__sqale_rating = sqale_rating
                        self.__development_cost = development_cost
                        self.__sqale_debt_ratio = sqale_debt_ratio
                        self.__effort_to_reach_maintainability_rating_a = effort_to_reach_maintainability_rating_a
                        pass

                    def _get_code_smells(self):
                        return self.__code_smells
                    def _set_code_smells(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("code_smells must be int")

                        self.__code_smells = value
                    code_smells = property(_get_code_smells, _set_code_smells)
                    """
                    Code Smells
                    """

                    def _get_sqale_index(self):
                        return self.__sqale_index
                    def _set_sqale_index(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("sqale_index must be int")

                        self.__sqale_index = value
                    sqale_index = property(_get_sqale_index, _set_sqale_index)
                    """
                    Total effort (in hours) to fix all the issues on the component and therefore to comply to all the requirements.
                    """

                    def _get_sqale_rating(self):
                        return self.__sqale_rating
                    def _set_sqale_rating(self, value):
                        if value is not None and  not isinstance(value, float):
                            raise TypeError("sqale_rating must be float")

                        self.__sqale_rating = value
                    sqale_rating = property(_get_sqale_rating, _set_sqale_rating)
                    """
                    A-to-E rating based on the technical debt ratio
                    """

                    def _get_development_cost(self):
                        return self.__development_cost
                    def _set_development_cost(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("development_cost must be int")

                        self.__development_cost = value
                    development_cost = property(_get_development_cost, _set_development_cost)
                    """
                    Development cost
                    """

                    def _get_sqale_debt_ratio(self):
                        return self.__sqale_debt_ratio
                    def _set_sqale_debt_ratio(self, value):
                        if value is not None and  not isinstance(value, float):
                            raise TypeError("sqale_debt_ratio must be float")

                        self.__sqale_debt_ratio = value
                    sqale_debt_ratio = property(_get_sqale_debt_ratio, _set_sqale_debt_ratio)
                    """
                    Ratio of the actual technical debt compared to the estimated cost to develop the whole source code from scratch
                    """

                    def _get_effort_to_reach_maintainability_rating_a(self):
                        return self.__effort_to_reach_maintainability_rating_a
                    def _set_effort_to_reach_maintainability_rating_a(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("effort_to_reach_maintainability_rating_a must be int")

                        self.__effort_to_reach_maintainability_rating_a = value
                    effort_to_reach_maintainability_rating_a = property(_get_effort_to_reach_maintainability_rating_a, _set_effort_to_reach_maintainability_rating_a)
                    """
                    Effort to reach maintainability rating A
                    """


                    @staticmethod
                    def from_dict(d):
                        v = {}
                        if "code_smells" in d:
                            v["code_smells"] = int.from_dict(d["code_smells"]) if hasattr(int, 'from_dict') else d["code_smells"]
                        if "sqale_index" in d:
                            v["sqale_index"] = int.from_dict(d["sqale_index"]) if hasattr(int, 'from_dict') else d["sqale_index"]
                        if "sqale_rating" in d:
                            v["sqale_rating"] = float.from_dict(d["sqale_rating"]) if hasattr(float, 'from_dict') else d["sqale_rating"]
                        if "development_cost" in d:
                            v["development_cost"] = int.from_dict(d["development_cost"]) if hasattr(int, 'from_dict') else d["development_cost"]
                        if "sqale_debt_ratio" in d:
                            v["sqale_debt_ratio"] = float.from_dict(d["sqale_debt_ratio"]) if hasattr(float, 'from_dict') else d["sqale_debt_ratio"]
                        if "effort_to_reach_maintainability_rating_a" in d:
                            v["effort_to_reach_maintainability_rating_a"] = int.from_dict(d["effort_to_reach_maintainability_rating_a"]) if hasattr(int, 'from_dict') else d["effort_to_reach_maintainability_rating_a"]
                        return QualitySchema._sonar._maintainability(**v)


                    def as_dict(self):
                        d = {}
                        if self.__code_smells is not None:
                            d['code_smells'] = self.__code_smells.as_dict() if hasattr(self.__code_smells, 'as_dict') else self.__code_smells
                        if self.__sqale_index is not None:
                            d['sqale_index'] = self.__sqale_index.as_dict() if hasattr(self.__sqale_index, 'as_dict') else self.__sqale_index
                        if self.__sqale_rating is not None:
                            d['sqale_rating'] = self.__sqale_rating.as_dict() if hasattr(self.__sqale_rating, 'as_dict') else self.__sqale_rating
                        if self.__development_cost is not None:
                            d['development_cost'] = self.__development_cost.as_dict() if hasattr(self.__development_cost, 'as_dict') else self.__development_cost
                        if self.__sqale_debt_ratio is not None:
                            d['sqale_debt_ratio'] = self.__sqale_debt_ratio.as_dict() if hasattr(self.__sqale_debt_ratio, 'as_dict') else self.__sqale_debt_ratio
                        if self.__effort_to_reach_maintainability_rating_a is not None:
                            d['effort_to_reach_maintainability_rating_a'] = self.__effort_to_reach_maintainability_rating_a.as_dict() if hasattr(self.__effort_to_reach_maintainability_rating_a, 'as_dict') else self.__effort_to_reach_maintainability_rating_a
                        return d

                    def __repr__(self):
                        return "<Class _maintainability. code_smells: {}, sqale_index: {}, sqale_rating: {}, development_cost: {}, sqale_debt_ratio: {}, effort_to_reach_maintainability_rating_a: {}>".format(limitedRepr(self.__code_smells[:20] if isinstance(self.__code_smells, bytes) else self.__code_smells), limitedRepr(self.__sqale_index[:20] if isinstance(self.__sqale_index, bytes) else self.__sqale_index), limitedRepr(self.__sqale_rating[:20] if isinstance(self.__sqale_rating, bytes) else self.__sqale_rating), limitedRepr(self.__development_cost[:20] if isinstance(self.__development_cost, bytes) else self.__development_cost), limitedRepr(self.__sqale_debt_ratio[:20] if isinstance(self.__sqale_debt_ratio, bytes) else self.__sqale_debt_ratio), limitedRepr(self.__effort_to_reach_maintainability_rating_a[:20] if isinstance(self.__effort_to_reach_maintainability_rating_a, bytes) else self.__effort_to_reach_maintainability_rating_a))

            class _owasp_dependency_check:



                    _types_map = {
                        'inherited_risk_score': {'type': int, 'subtype': None},
                        'vulnerable_component_ratio': {'type': float, 'subtype': None},
                        'critical_severity_vulns': {'type': int, 'subtype': None},
                        'high_severity_vulns': {'type': int, 'subtype': None},
                        'medium_severity_vulns': {'type': int, 'subtype': None},
                        'low_severity_vulns': {'type': int, 'subtype': None},
                        'total_dependencies': {'type': int, 'subtype': None},
                        'vulnerable_dependencies': {'type': int, 'subtype': None},
                        'total_vulnerabilities': {'type': int, 'subtype': None},
                    }
                    _formats_map = {
                    }
                    _validations_map = {
                        'inherited_risk_score': { 'required': False,},
                        'vulnerable_component_ratio': { 'required': False,},
                        'critical_severity_vulns': { 'required': False,},
                        'high_severity_vulns': { 'required': False,},
                        'medium_severity_vulns': { 'required': False,},
                        'low_severity_vulns': { 'required': False,},
                        'total_dependencies': { 'required': False,},
                        'vulnerable_dependencies': { 'required': False,},
                        'total_vulnerabilities': { 'required': False,},
                    }

                    def __init__(self
                            , inherited_risk_score=None
                            , vulnerable_component_ratio=None
                            , critical_severity_vulns=None
                            , high_severity_vulns=None
                            , medium_severity_vulns=None
                            , low_severity_vulns=None
                            , total_dependencies=None
                            , vulnerable_dependencies=None
                            , total_vulnerabilities=None
                            ):
                        """
                        :param inherited_risk_score: Inherited Risk Score
                        :param vulnerable_component_ratio: Vulnerable Component Ratio
                        :param critical_severity_vulns: Critical Severity Vulnerabilities
                        :param high_severity_vulns: High Severity Vulnerabilities
                        :param medium_severity_vulns: Medium Severity Vulnerabilities
                        :param low_severity_vulns: Low Severity Vulnerabilities
                        :param total_dependencies: Total Dependencies
                        :param vulnerable_dependencies: Vulnerable Dependencies
                        :param total_vulnerabilities: Total Vulnerabilities
                        """
                        self.__inherited_risk_score = inherited_risk_score
                        self.__vulnerable_component_ratio = vulnerable_component_ratio
                        self.__critical_severity_vulns = critical_severity_vulns
                        self.__high_severity_vulns = high_severity_vulns
                        self.__medium_severity_vulns = medium_severity_vulns
                        self.__low_severity_vulns = low_severity_vulns
                        self.__total_dependencies = total_dependencies
                        self.__vulnerable_dependencies = vulnerable_dependencies
                        self.__total_vulnerabilities = total_vulnerabilities
                        pass

                    def _get_inherited_risk_score(self):
                        return self.__inherited_risk_score
                    def _set_inherited_risk_score(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("inherited_risk_score must be int")

                        self.__inherited_risk_score = value
                    inherited_risk_score = property(_get_inherited_risk_score, _set_inherited_risk_score)
                    """
                    Inherited Risk Score
                    """

                    def _get_vulnerable_component_ratio(self):
                        return self.__vulnerable_component_ratio
                    def _set_vulnerable_component_ratio(self, value):
                        if value is not None and  not isinstance(value, float):
                            raise TypeError("vulnerable_component_ratio must be float")

                        self.__vulnerable_component_ratio = value
                    vulnerable_component_ratio = property(_get_vulnerable_component_ratio, _set_vulnerable_component_ratio)
                    """
                    Vulnerable Component Ratio
                    """

                    def _get_critical_severity_vulns(self):
                        return self.__critical_severity_vulns
                    def _set_critical_severity_vulns(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("critical_severity_vulns must be int")

                        self.__critical_severity_vulns = value
                    critical_severity_vulns = property(_get_critical_severity_vulns, _set_critical_severity_vulns)
                    """
                    Critical Severity Vulnerabilities
                    """

                    def _get_high_severity_vulns(self):
                        return self.__high_severity_vulns
                    def _set_high_severity_vulns(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("high_severity_vulns must be int")

                        self.__high_severity_vulns = value
                    high_severity_vulns = property(_get_high_severity_vulns, _set_high_severity_vulns)
                    """
                    High Severity Vulnerabilities
                    """

                    def _get_medium_severity_vulns(self):
                        return self.__medium_severity_vulns
                    def _set_medium_severity_vulns(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("medium_severity_vulns must be int")

                        self.__medium_severity_vulns = value
                    medium_severity_vulns = property(_get_medium_severity_vulns, _set_medium_severity_vulns)
                    """
                    Medium Severity Vulnerabilities
                    """

                    def _get_low_severity_vulns(self):
                        return self.__low_severity_vulns
                    def _set_low_severity_vulns(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("low_severity_vulns must be int")

                        self.__low_severity_vulns = value
                    low_severity_vulns = property(_get_low_severity_vulns, _set_low_severity_vulns)
                    """
                    Low Severity Vulnerabilities
                    """

                    def _get_total_dependencies(self):
                        return self.__total_dependencies
                    def _set_total_dependencies(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("total_dependencies must be int")

                        self.__total_dependencies = value
                    total_dependencies = property(_get_total_dependencies, _set_total_dependencies)
                    """
                    Total Dependencies
                    """

                    def _get_vulnerable_dependencies(self):
                        return self.__vulnerable_dependencies
                    def _set_vulnerable_dependencies(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("vulnerable_dependencies must be int")

                        self.__vulnerable_dependencies = value
                    vulnerable_dependencies = property(_get_vulnerable_dependencies, _set_vulnerable_dependencies)
                    """
                    Vulnerable Dependencies
                    """

                    def _get_total_vulnerabilities(self):
                        return self.__total_vulnerabilities
                    def _set_total_vulnerabilities(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("total_vulnerabilities must be int")

                        self.__total_vulnerabilities = value
                    total_vulnerabilities = property(_get_total_vulnerabilities, _set_total_vulnerabilities)
                    """
                    Total Vulnerabilities
                    """


                    @staticmethod
                    def from_dict(d):
                        v = {}
                        if "inherited_risk_score" in d:
                            v["inherited_risk_score"] = int.from_dict(d["inherited_risk_score"]) if hasattr(int, 'from_dict') else d["inherited_risk_score"]
                        if "vulnerable_component_ratio" in d:
                            v["vulnerable_component_ratio"] = float.from_dict(d["vulnerable_component_ratio"]) if hasattr(float, 'from_dict') else d["vulnerable_component_ratio"]
                        if "critical_severity_vulns" in d:
                            v["critical_severity_vulns"] = int.from_dict(d["critical_severity_vulns"]) if hasattr(int, 'from_dict') else d["critical_severity_vulns"]
                        if "high_severity_vulns" in d:
                            v["high_severity_vulns"] = int.from_dict(d["high_severity_vulns"]) if hasattr(int, 'from_dict') else d["high_severity_vulns"]
                        if "medium_severity_vulns" in d:
                            v["medium_severity_vulns"] = int.from_dict(d["medium_severity_vulns"]) if hasattr(int, 'from_dict') else d["medium_severity_vulns"]
                        if "low_severity_vulns" in d:
                            v["low_severity_vulns"] = int.from_dict(d["low_severity_vulns"]) if hasattr(int, 'from_dict') else d["low_severity_vulns"]
                        if "total_dependencies" in d:
                            v["total_dependencies"] = int.from_dict(d["total_dependencies"]) if hasattr(int, 'from_dict') else d["total_dependencies"]
                        if "vulnerable_dependencies" in d:
                            v["vulnerable_dependencies"] = int.from_dict(d["vulnerable_dependencies"]) if hasattr(int, 'from_dict') else d["vulnerable_dependencies"]
                        if "total_vulnerabilities" in d:
                            v["total_vulnerabilities"] = int.from_dict(d["total_vulnerabilities"]) if hasattr(int, 'from_dict') else d["total_vulnerabilities"]
                        return QualitySchema._sonar._owasp_dependency_check(**v)


                    def as_dict(self):
                        d = {}
                        if self.__inherited_risk_score is not None:
                            d['inherited_risk_score'] = self.__inherited_risk_score.as_dict() if hasattr(self.__inherited_risk_score, 'as_dict') else self.__inherited_risk_score
                        if self.__vulnerable_component_ratio is not None:
                            d['vulnerable_component_ratio'] = self.__vulnerable_component_ratio.as_dict() if hasattr(self.__vulnerable_component_ratio, 'as_dict') else self.__vulnerable_component_ratio
                        if self.__critical_severity_vulns is not None:
                            d['critical_severity_vulns'] = self.__critical_severity_vulns.as_dict() if hasattr(self.__critical_severity_vulns, 'as_dict') else self.__critical_severity_vulns
                        if self.__high_severity_vulns is not None:
                            d['high_severity_vulns'] = self.__high_severity_vulns.as_dict() if hasattr(self.__high_severity_vulns, 'as_dict') else self.__high_severity_vulns
                        if self.__medium_severity_vulns is not None:
                            d['medium_severity_vulns'] = self.__medium_severity_vulns.as_dict() if hasattr(self.__medium_severity_vulns, 'as_dict') else self.__medium_severity_vulns
                        if self.__low_severity_vulns is not None:
                            d['low_severity_vulns'] = self.__low_severity_vulns.as_dict() if hasattr(self.__low_severity_vulns, 'as_dict') else self.__low_severity_vulns
                        if self.__total_dependencies is not None:
                            d['total_dependencies'] = self.__total_dependencies.as_dict() if hasattr(self.__total_dependencies, 'as_dict') else self.__total_dependencies
                        if self.__vulnerable_dependencies is not None:
                            d['vulnerable_dependencies'] = self.__vulnerable_dependencies.as_dict() if hasattr(self.__vulnerable_dependencies, 'as_dict') else self.__vulnerable_dependencies
                        if self.__total_vulnerabilities is not None:
                            d['total_vulnerabilities'] = self.__total_vulnerabilities.as_dict() if hasattr(self.__total_vulnerabilities, 'as_dict') else self.__total_vulnerabilities
                        return d

                    def __repr__(self):
                        return "<Class _owasp_dependency_check. inherited_risk_score: {}, vulnerable_component_ratio: {}, critical_severity_vulns: {}, high_severity_vulns: {}, medium_severity_vulns: {}, low_severity_vulns: {}, total_dependencies: {}, vulnerable_dependencies: {}, total_vulnerabilities: {}>".format(limitedRepr(self.__inherited_risk_score[:20] if isinstance(self.__inherited_risk_score, bytes) else self.__inherited_risk_score), limitedRepr(self.__vulnerable_component_ratio[:20] if isinstance(self.__vulnerable_component_ratio, bytes) else self.__vulnerable_component_ratio), limitedRepr(self.__critical_severity_vulns[:20] if isinstance(self.__critical_severity_vulns, bytes) else self.__critical_severity_vulns), limitedRepr(self.__high_severity_vulns[:20] if isinstance(self.__high_severity_vulns, bytes) else self.__high_severity_vulns), limitedRepr(self.__medium_severity_vulns[:20] if isinstance(self.__medium_severity_vulns, bytes) else self.__medium_severity_vulns), limitedRepr(self.__low_severity_vulns[:20] if isinstance(self.__low_severity_vulns, bytes) else self.__low_severity_vulns), limitedRepr(self.__total_dependencies[:20] if isinstance(self.__total_dependencies, bytes) else self.__total_dependencies), limitedRepr(self.__vulnerable_dependencies[:20] if isinstance(self.__vulnerable_dependencies, bytes) else self.__vulnerable_dependencies), limitedRepr(self.__total_vulnerabilities[:20] if isinstance(self.__total_vulnerabilities, bytes) else self.__total_vulnerabilities))

            class _releasability:



                    _types_map = {
                        'alert_status': {'type': str, 'subtype': None},
                    }
                    _formats_map = {
                    }
                    _validations_map = {
                        'alert_status': { 'required': False,},
                    }

                    def __init__(self
                            , alert_status=None
                            ):
                        """
                        :param alert_status: The project status with regard to its quality gate.
                        """
                        self.__alert_status = alert_status
                        pass

                    def _get_alert_status(self):
                        return self.__alert_status
                    def _set_alert_status(self, value):
                        if value is not None and  not isinstance(value, str):
                            raise TypeError("alert_status must be str")

                        self.__alert_status = value
                    alert_status = property(_get_alert_status, _set_alert_status)
                    """
                    The project status with regard to its quality gate.
                    """


                    @staticmethod
                    def from_dict(d):
                        v = {}
                        if "alert_status" in d:
                            v["alert_status"] = str.from_dict(d["alert_status"]) if hasattr(str, 'from_dict') else d["alert_status"]
                        return QualitySchema._sonar._releasability(**v)


                    def as_dict(self):
                        d = {}
                        if self.__alert_status is not None:
                            d['alert_status'] = self.__alert_status.as_dict() if hasattr(self.__alert_status, 'as_dict') else self.__alert_status
                        return d

                    def __repr__(self):
                        return "<Class _releasability. alert_status: {}>".format(limitedRepr(self.__alert_status[:20] if isinstance(self.__alert_status, bytes) else self.__alert_status))

            class _reliability:



                    _types_map = {
                        'bugs': {'type': int, 'subtype': None},
                        'reliability_remediation_effort': {'type': int, 'subtype': None},
                        'reliability_rating': {'type': float, 'subtype': None},
                    }
                    _formats_map = {
                    }
                    _validations_map = {
                        'bugs': { 'required': False,},
                        'reliability_remediation_effort': { 'required': False,},
                        'reliability_rating': { 'required': False,},
                    }

                    def __init__(self
                            , bugs=None
                            , reliability_remediation_effort=None
                            , reliability_rating=None
                            ):
                        """
                        :param bugs: Bugs
                        :param reliability_remediation_effort: Reliability Remediation Effort
                        :param reliability_rating: Reliability rating
                        """
                        self.__bugs = bugs
                        self.__reliability_remediation_effort = reliability_remediation_effort
                        self.__reliability_rating = reliability_rating
                        pass

                    def _get_bugs(self):
                        return self.__bugs
                    def _set_bugs(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("bugs must be int")

                        self.__bugs = value
                    bugs = property(_get_bugs, _set_bugs)
                    """
                    Bugs
                    """

                    def _get_reliability_remediation_effort(self):
                        return self.__reliability_remediation_effort
                    def _set_reliability_remediation_effort(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("reliability_remediation_effort must be int")

                        self.__reliability_remediation_effort = value
                    reliability_remediation_effort = property(_get_reliability_remediation_effort, _set_reliability_remediation_effort)
                    """
                    Reliability Remediation Effort
                    """

                    def _get_reliability_rating(self):
                        return self.__reliability_rating
                    def _set_reliability_rating(self, value):
                        if value is not None and  not isinstance(value, float):
                            raise TypeError("reliability_rating must be float")

                        self.__reliability_rating = value
                    reliability_rating = property(_get_reliability_rating, _set_reliability_rating)
                    """
                    Reliability rating
                    """


                    @staticmethod
                    def from_dict(d):
                        v = {}
                        if "bugs" in d:
                            v["bugs"] = int.from_dict(d["bugs"]) if hasattr(int, 'from_dict') else d["bugs"]
                        if "reliability_remediation_effort" in d:
                            v["reliability_remediation_effort"] = int.from_dict(d["reliability_remediation_effort"]) if hasattr(int, 'from_dict') else d["reliability_remediation_effort"]
                        if "reliability_rating" in d:
                            v["reliability_rating"] = float.from_dict(d["reliability_rating"]) if hasattr(float, 'from_dict') else d["reliability_rating"]
                        return QualitySchema._sonar._reliability(**v)


                    def as_dict(self):
                        d = {}
                        if self.__bugs is not None:
                            d['bugs'] = self.__bugs.as_dict() if hasattr(self.__bugs, 'as_dict') else self.__bugs
                        if self.__reliability_remediation_effort is not None:
                            d['reliability_remediation_effort'] = self.__reliability_remediation_effort.as_dict() if hasattr(self.__reliability_remediation_effort, 'as_dict') else self.__reliability_remediation_effort
                        if self.__reliability_rating is not None:
                            d['reliability_rating'] = self.__reliability_rating.as_dict() if hasattr(self.__reliability_rating, 'as_dict') else self.__reliability_rating
                        return d

                    def __repr__(self):
                        return "<Class _reliability. bugs: {}, reliability_remediation_effort: {}, reliability_rating: {}>".format(limitedRepr(self.__bugs[:20] if isinstance(self.__bugs, bytes) else self.__bugs), limitedRepr(self.__reliability_remediation_effort[:20] if isinstance(self.__reliability_remediation_effort, bytes) else self.__reliability_remediation_effort), limitedRepr(self.__reliability_rating[:20] if isinstance(self.__reliability_rating, bytes) else self.__reliability_rating))

            class _scm:



                    _types_map = {
                        'last_commit_date': {'type': int, 'subtype': None},
                    }
                    _formats_map = {
                    }
                    _validations_map = {
                        'last_commit_date': { 'required': False,},
                    }

                    def __init__(self
                            , last_commit_date=None
                            ):
                        self.__last_commit_date = last_commit_date
                        pass

                    def _get_last_commit_date(self):
                        return self.__last_commit_date
                    def _set_last_commit_date(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("last_commit_date must be int")

                        self.__last_commit_date = value
                    last_commit_date = property(_get_last_commit_date, _set_last_commit_date)


                    @staticmethod
                    def from_dict(d):
                        v = {}
                        if "last_commit_date" in d:
                            v["last_commit_date"] = int.from_dict(d["last_commit_date"]) if hasattr(int, 'from_dict') else d["last_commit_date"]
                        return QualitySchema._sonar._scm(**v)


                    def as_dict(self):
                        d = {}
                        if self.__last_commit_date is not None:
                            d['last_commit_date'] = self.__last_commit_date.as_dict() if hasattr(self.__last_commit_date, 'as_dict') else self.__last_commit_date
                        return d

                    def __repr__(self):
                        return "<Class _scm. last_commit_date: {}>".format(limitedRepr(self.__last_commit_date[:20] if isinstance(self.__last_commit_date, bytes) else self.__last_commit_date))

            class _security:



                    _types_map = {
                        'vulnerabilities': {'type': int, 'subtype': None},
                        'security_remediation_effort': {'type': int, 'subtype': None},
                        'security_rating': {'type': float, 'subtype': None},
                        'security_hotspots': {'type': int, 'subtype': None},
                        'security_review_rating': {'type': float, 'subtype': None},
                    }
                    _formats_map = {
                    }
                    _validations_map = {
                        'vulnerabilities': { 'required': False,},
                        'security_remediation_effort': { 'required': False,},
                        'security_rating': { 'required': False,},
                        'security_hotspots': { 'required': False,},
                        'security_review_rating': { 'required': False,},
                    }

                    def __init__(self
                            , vulnerabilities=None
                            , security_remediation_effort=None
                            , security_rating=None
                            , security_hotspots=None
                            , security_review_rating=None
                            ):
                        """
                        :param vulnerabilities: Vulnerabilities
                        :param security_remediation_effort: Security remediation effort
                        :param security_rating: Security rating
                        :param security_hotspots: Security Hotspots
                        :param security_review_rating: Security Review Rating
                        """
                        self.__vulnerabilities = vulnerabilities
                        self.__security_remediation_effort = security_remediation_effort
                        self.__security_rating = security_rating
                        self.__security_hotspots = security_hotspots
                        self.__security_review_rating = security_review_rating
                        pass

                    def _get_vulnerabilities(self):
                        return self.__vulnerabilities
                    def _set_vulnerabilities(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("vulnerabilities must be int")

                        self.__vulnerabilities = value
                    vulnerabilities = property(_get_vulnerabilities, _set_vulnerabilities)
                    """
                    Vulnerabilities
                    """

                    def _get_security_remediation_effort(self):
                        return self.__security_remediation_effort
                    def _set_security_remediation_effort(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("security_remediation_effort must be int")

                        self.__security_remediation_effort = value
                    security_remediation_effort = property(_get_security_remediation_effort, _set_security_remediation_effort)
                    """
                    Security remediation effort
                    """

                    def _get_security_rating(self):
                        return self.__security_rating
                    def _set_security_rating(self, value):
                        if value is not None and  not isinstance(value, float):
                            raise TypeError("security_rating must be float")

                        self.__security_rating = value
                    security_rating = property(_get_security_rating, _set_security_rating)
                    """
                    Security rating
                    """

                    def _get_security_hotspots(self):
                        return self.__security_hotspots
                    def _set_security_hotspots(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("security_hotspots must be int")

                        self.__security_hotspots = value
                    security_hotspots = property(_get_security_hotspots, _set_security_hotspots)
                    """
                    Security Hotspots
                    """

                    def _get_security_review_rating(self):
                        return self.__security_review_rating
                    def _set_security_review_rating(self, value):
                        if value is not None and  not isinstance(value, float):
                            raise TypeError("security_review_rating must be float")

                        self.__security_review_rating = value
                    security_review_rating = property(_get_security_review_rating, _set_security_review_rating)
                    """
                    Security Review Rating
                    """


                    @staticmethod
                    def from_dict(d):
                        v = {}
                        if "vulnerabilities" in d:
                            v["vulnerabilities"] = int.from_dict(d["vulnerabilities"]) if hasattr(int, 'from_dict') else d["vulnerabilities"]
                        if "security_remediation_effort" in d:
                            v["security_remediation_effort"] = int.from_dict(d["security_remediation_effort"]) if hasattr(int, 'from_dict') else d["security_remediation_effort"]
                        if "security_rating" in d:
                            v["security_rating"] = float.from_dict(d["security_rating"]) if hasattr(float, 'from_dict') else d["security_rating"]
                        if "security_hotspots" in d:
                            v["security_hotspots"] = int.from_dict(d["security_hotspots"]) if hasattr(int, 'from_dict') else d["security_hotspots"]
                        if "security_review_rating" in d:
                            v["security_review_rating"] = float.from_dict(d["security_review_rating"]) if hasattr(float, 'from_dict') else d["security_review_rating"]
                        return QualitySchema._sonar._security(**v)


                    def as_dict(self):
                        d = {}
                        if self.__vulnerabilities is not None:
                            d['vulnerabilities'] = self.__vulnerabilities.as_dict() if hasattr(self.__vulnerabilities, 'as_dict') else self.__vulnerabilities
                        if self.__security_remediation_effort is not None:
                            d['security_remediation_effort'] = self.__security_remediation_effort.as_dict() if hasattr(self.__security_remediation_effort, 'as_dict') else self.__security_remediation_effort
                        if self.__security_rating is not None:
                            d['security_rating'] = self.__security_rating.as_dict() if hasattr(self.__security_rating, 'as_dict') else self.__security_rating
                        if self.__security_hotspots is not None:
                            d['security_hotspots'] = self.__security_hotspots.as_dict() if hasattr(self.__security_hotspots, 'as_dict') else self.__security_hotspots
                        if self.__security_review_rating is not None:
                            d['security_review_rating'] = self.__security_review_rating.as_dict() if hasattr(self.__security_review_rating, 'as_dict') else self.__security_review_rating
                        return d

                    def __repr__(self):
                        return "<Class _security. vulnerabilities: {}, security_remediation_effort: {}, security_rating: {}, security_hotspots: {}, security_review_rating: {}>".format(limitedRepr(self.__vulnerabilities[:20] if isinstance(self.__vulnerabilities, bytes) else self.__vulnerabilities), limitedRepr(self.__security_remediation_effort[:20] if isinstance(self.__security_remediation_effort, bytes) else self.__security_remediation_effort), limitedRepr(self.__security_rating[:20] if isinstance(self.__security_rating, bytes) else self.__security_rating), limitedRepr(self.__security_hotspots[:20] if isinstance(self.__security_hotspots, bytes) else self.__security_hotspots), limitedRepr(self.__security_review_rating[:20] if isinstance(self.__security_review_rating, bytes) else self.__security_review_rating))

            class _size:



                    _types_map = {
                        'lines': {'type': int, 'subtype': None},
                        'generated_lines': {'type': int, 'subtype': None},
                        'ncloc': {'type': int, 'subtype': None},
                        'ncloc_language_distribution': {'type': str, 'subtype': None},
                        'generated_ncloc': {'type': int, 'subtype': None},
                        'classes': {'type': int, 'subtype': None},
                        'files': {'type': int, 'subtype': None},
                        'directories': {'type': int, 'subtype': None},
                        'functions': {'type': int, 'subtype': None},
                        'statements': {'type': int, 'subtype': None},
                        'projects': {'type': int, 'subtype': None},
                        'comment_lines': {'type': int, 'subtype': None},
                    }
                    _formats_map = {
                    }
                    _validations_map = {
                        'lines': { 'required': False,},
                        'generated_lines': { 'required': False,},
                        'ncloc': { 'required': False,},
                        'ncloc_language_distribution': { 'required': False,},
                        'generated_ncloc': { 'required': False,},
                        'classes': { 'required': False,},
                        'files': { 'required': False,},
                        'directories': { 'required': False,},
                        'functions': { 'required': False,},
                        'statements': { 'required': False,},
                        'projects': { 'required': False,},
                        'comment_lines': { 'required': False,},
                    }

                    def __init__(self
                            , lines=None
                            , generated_lines=None
                            , ncloc=None
                            , ncloc_language_distribution=None
                            , generated_ncloc=None
                            , classes=None
                            , files=None
                            , directories=None
                            , functions=None
                            , statements=None
                            , projects=None
                            , comment_lines=None
                            ):
                        """
                        :param lines: Lines
                        :param generated_lines: Number of generated lines
                        :param ncloc: Non commenting lines of code
                        :param ncloc_language_distribution: Non Commenting Lines of Code Distributed By Language
                        :param generated_ncloc: Generated non Commenting Lines of Code
                        :param classes: Classes
                        :param files: Number of files
                        :param directories: Directories
                        :param functions: Functions
                        :param statements: Number of statements
                        :param projects: Number of projects
                        :param comment_lines: Number of comment lines
                        """
                        self.__lines = lines
                        self.__generated_lines = generated_lines
                        self.__ncloc = ncloc
                        self.__ncloc_language_distribution = ncloc_language_distribution
                        self.__generated_ncloc = generated_ncloc
                        self.__classes = classes
                        self.__files = files
                        self.__directories = directories
                        self.__functions = functions
                        self.__statements = statements
                        self.__projects = projects
                        self.__comment_lines = comment_lines
                        pass

                    def _get_lines(self):
                        return self.__lines
                    def _set_lines(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("lines must be int")

                        self.__lines = value
                    lines = property(_get_lines, _set_lines)
                    """
                    Lines
                    """

                    def _get_generated_lines(self):
                        return self.__generated_lines
                    def _set_generated_lines(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("generated_lines must be int")

                        self.__generated_lines = value
                    generated_lines = property(_get_generated_lines, _set_generated_lines)
                    """
                    Number of generated lines
                    """

                    def _get_ncloc(self):
                        return self.__ncloc
                    def _set_ncloc(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("ncloc must be int")

                        self.__ncloc = value
                    ncloc = property(_get_ncloc, _set_ncloc)
                    """
                    Non commenting lines of code
                    """

                    def _get_ncloc_language_distribution(self):
                        return self.__ncloc_language_distribution
                    def _set_ncloc_language_distribution(self, value):
                        if value is not None and  not isinstance(value, str):
                            raise TypeError("ncloc_language_distribution must be str")

                        self.__ncloc_language_distribution = value
                    ncloc_language_distribution = property(_get_ncloc_language_distribution, _set_ncloc_language_distribution)
                    """
                    Non Commenting Lines of Code Distributed By Language
                    """

                    def _get_generated_ncloc(self):
                        return self.__generated_ncloc
                    def _set_generated_ncloc(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("generated_ncloc must be int")

                        self.__generated_ncloc = value
                    generated_ncloc = property(_get_generated_ncloc, _set_generated_ncloc)
                    """
                    Generated non Commenting Lines of Code
                    """

                    def _get_classes(self):
                        return self.__classes
                    def _set_classes(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("classes must be int")

                        self.__classes = value
                    classes = property(_get_classes, _set_classes)
                    """
                    Classes
                    """

                    def _get_files(self):
                        return self.__files
                    def _set_files(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("files must be int")

                        self.__files = value
                    files = property(_get_files, _set_files)
                    """
                    Number of files
                    """

                    def _get_directories(self):
                        return self.__directories
                    def _set_directories(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("directories must be int")

                        self.__directories = value
                    directories = property(_get_directories, _set_directories)
                    """
                    Directories
                    """

                    def _get_functions(self):
                        return self.__functions
                    def _set_functions(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("functions must be int")

                        self.__functions = value
                    functions = property(_get_functions, _set_functions)
                    """
                    Functions
                    """

                    def _get_statements(self):
                        return self.__statements
                    def _set_statements(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("statements must be int")

                        self.__statements = value
                    statements = property(_get_statements, _set_statements)
                    """
                    Number of statements
                    """

                    def _get_projects(self):
                        return self.__projects
                    def _set_projects(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("projects must be int")

                        self.__projects = value
                    projects = property(_get_projects, _set_projects)
                    """
                    Number of projects
                    """

                    def _get_comment_lines(self):
                        return self.__comment_lines
                    def _set_comment_lines(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("comment_lines must be int")

                        self.__comment_lines = value
                    comment_lines = property(_get_comment_lines, _set_comment_lines)
                    """
                    Number of comment lines
                    """


                    @staticmethod
                    def from_dict(d):
                        v = {}
                        if "lines" in d:
                            v["lines"] = int.from_dict(d["lines"]) if hasattr(int, 'from_dict') else d["lines"]
                        if "generated_lines" in d:
                            v["generated_lines"] = int.from_dict(d["generated_lines"]) if hasattr(int, 'from_dict') else d["generated_lines"]
                        if "ncloc" in d:
                            v["ncloc"] = int.from_dict(d["ncloc"]) if hasattr(int, 'from_dict') else d["ncloc"]
                        if "ncloc_language_distribution" in d:
                            v["ncloc_language_distribution"] = str.from_dict(d["ncloc_language_distribution"]) if hasattr(str, 'from_dict') else d["ncloc_language_distribution"]
                        if "generated_ncloc" in d:
                            v["generated_ncloc"] = int.from_dict(d["generated_ncloc"]) if hasattr(int, 'from_dict') else d["generated_ncloc"]
                        if "classes" in d:
                            v["classes"] = int.from_dict(d["classes"]) if hasattr(int, 'from_dict') else d["classes"]
                        if "files" in d:
                            v["files"] = int.from_dict(d["files"]) if hasattr(int, 'from_dict') else d["files"]
                        if "directories" in d:
                            v["directories"] = int.from_dict(d["directories"]) if hasattr(int, 'from_dict') else d["directories"]
                        if "functions" in d:
                            v["functions"] = int.from_dict(d["functions"]) if hasattr(int, 'from_dict') else d["functions"]
                        if "statements" in d:
                            v["statements"] = int.from_dict(d["statements"]) if hasattr(int, 'from_dict') else d["statements"]
                        if "projects" in d:
                            v["projects"] = int.from_dict(d["projects"]) if hasattr(int, 'from_dict') else d["projects"]
                        if "comment_lines" in d:
                            v["comment_lines"] = int.from_dict(d["comment_lines"]) if hasattr(int, 'from_dict') else d["comment_lines"]
                        return QualitySchema._sonar._size(**v)


                    def as_dict(self):
                        d = {}
                        if self.__lines is not None:
                            d['lines'] = self.__lines.as_dict() if hasattr(self.__lines, 'as_dict') else self.__lines
                        if self.__generated_lines is not None:
                            d['generated_lines'] = self.__generated_lines.as_dict() if hasattr(self.__generated_lines, 'as_dict') else self.__generated_lines
                        if self.__ncloc is not None:
                            d['ncloc'] = self.__ncloc.as_dict() if hasattr(self.__ncloc, 'as_dict') else self.__ncloc
                        if self.__ncloc_language_distribution is not None:
                            d['ncloc_language_distribution'] = self.__ncloc_language_distribution.as_dict() if hasattr(self.__ncloc_language_distribution, 'as_dict') else self.__ncloc_language_distribution
                        if self.__generated_ncloc is not None:
                            d['generated_ncloc'] = self.__generated_ncloc.as_dict() if hasattr(self.__generated_ncloc, 'as_dict') else self.__generated_ncloc
                        if self.__classes is not None:
                            d['classes'] = self.__classes.as_dict() if hasattr(self.__classes, 'as_dict') else self.__classes
                        if self.__files is not None:
                            d['files'] = self.__files.as_dict() if hasattr(self.__files, 'as_dict') else self.__files
                        if self.__directories is not None:
                            d['directories'] = self.__directories.as_dict() if hasattr(self.__directories, 'as_dict') else self.__directories
                        if self.__functions is not None:
                            d['functions'] = self.__functions.as_dict() if hasattr(self.__functions, 'as_dict') else self.__functions
                        if self.__statements is not None:
                            d['statements'] = self.__statements.as_dict() if hasattr(self.__statements, 'as_dict') else self.__statements
                        if self.__projects is not None:
                            d['projects'] = self.__projects.as_dict() if hasattr(self.__projects, 'as_dict') else self.__projects
                        if self.__comment_lines is not None:
                            d['comment_lines'] = self.__comment_lines.as_dict() if hasattr(self.__comment_lines, 'as_dict') else self.__comment_lines
                        return d

                    def __repr__(self):
                        return "<Class _size. lines: {}, generated_lines: {}, ncloc: {}, ncloc_language_distribution: {}, generated_ncloc: {}, classes: {}, files: {}, directories: {}, functions: {}, statements: {}, projects: {}, comment_lines: {}>".format(limitedRepr(self.__lines[:20] if isinstance(self.__lines, bytes) else self.__lines), limitedRepr(self.__generated_lines[:20] if isinstance(self.__generated_lines, bytes) else self.__generated_lines), limitedRepr(self.__ncloc[:20] if isinstance(self.__ncloc, bytes) else self.__ncloc), limitedRepr(self.__ncloc_language_distribution[:20] if isinstance(self.__ncloc_language_distribution, bytes) else self.__ncloc_language_distribution), limitedRepr(self.__generated_ncloc[:20] if isinstance(self.__generated_ncloc, bytes) else self.__generated_ncloc), limitedRepr(self.__classes[:20] if isinstance(self.__classes, bytes) else self.__classes), limitedRepr(self.__files[:20] if isinstance(self.__files, bytes) else self.__files), limitedRepr(self.__directories[:20] if isinstance(self.__directories, bytes) else self.__directories), limitedRepr(self.__functions[:20] if isinstance(self.__functions, bytes) else self.__functions), limitedRepr(self.__statements[:20] if isinstance(self.__statements, bytes) else self.__statements), limitedRepr(self.__projects[:20] if isinstance(self.__projects, bytes) else self.__projects), limitedRepr(self.__comment_lines[:20] if isinstance(self.__comment_lines, bytes) else self.__comment_lines))

            class _component:



                    _types_map = {
                        'sonar_version': {'type': str, 'subtype': None},
                        'key': {'type': str, 'subtype': None},
                        'name': {'type': str, 'subtype': None},
                        'description': {'type': str, 'subtype': None},
                    }
                    _formats_map = {
                    }
                    _validations_map = {
                        'sonar_version': { 'required': False,},
                        'key': { 'required': False,},
                        'name': { 'required': False,},
                        'description': { 'required': False,},
                    }

                    def __init__(self
                            , sonar_version=None
                            , key=None
                            , name=None
                            , description=None
                            ):
                        """
                        :param sonar_version: The Sonar server version
                        :param key: The Component key
                        :param name: The Component name
                        :param description: The Component description
                        """
                        self.__sonar_version = sonar_version
                        self.__key = key
                        self.__name = name
                        self.__description = description
                        pass

                    def _get_sonar_version(self):
                        return self.__sonar_version
                    def _set_sonar_version(self, value):
                        if value is not None and  not isinstance(value, str):
                            raise TypeError("sonar_version must be str")

                        self.__sonar_version = value
                    sonar_version = property(_get_sonar_version, _set_sonar_version)
                    """
                    The Sonar server version
                    """

                    def _get_key(self):
                        return self.__key
                    def _set_key(self, value):
                        if value is not None and  not isinstance(value, str):
                            raise TypeError("key must be str")

                        self.__key = value
                    key = property(_get_key, _set_key)
                    """
                    The Component key
                    """

                    def _get_name(self):
                        return self.__name
                    def _set_name(self, value):
                        if value is not None and  not isinstance(value, str):
                            raise TypeError("name must be str")

                        self.__name = value
                    name = property(_get_name, _set_name)
                    """
                    The Component name
                    """

                    def _get_description(self):
                        return self.__description
                    def _set_description(self, value):
                        if value is not None and  not isinstance(value, str):
                            raise TypeError("description must be str")

                        self.__description = value
                    description = property(_get_description, _set_description)
                    """
                    The Component description
                    """


                    @staticmethod
                    def from_dict(d):
                        v = {}
                        if "sonar_version" in d:
                            v["sonar_version"] = str.from_dict(d["sonar_version"]) if hasattr(str, 'from_dict') else d["sonar_version"]
                        if "key" in d:
                            v["key"] = str.from_dict(d["key"]) if hasattr(str, 'from_dict') else d["key"]
                        if "name" in d:
                            v["name"] = str.from_dict(d["name"]) if hasattr(str, 'from_dict') else d["name"]
                        if "description" in d:
                            v["description"] = str.from_dict(d["description"]) if hasattr(str, 'from_dict') else d["description"]
                        return QualitySchema._sonar._component(**v)


                    def as_dict(self):
                        d = {}
                        if self.__sonar_version is not None:
                            d['sonar_version'] = self.__sonar_version.as_dict() if hasattr(self.__sonar_version, 'as_dict') else self.__sonar_version
                        if self.__key is not None:
                            d['key'] = self.__key.as_dict() if hasattr(self.__key, 'as_dict') else self.__key
                        if self.__name is not None:
                            d['name'] = self.__name.as_dict() if hasattr(self.__name, 'as_dict') else self.__name
                        if self.__description is not None:
                            d['description'] = self.__description.as_dict() if hasattr(self.__description, 'as_dict') else self.__description
                        return d

                    def __repr__(self):
                        return "<Class _component. sonar_version: {}, key: {}, name: {}, description: {}>".format(limitedRepr(self.__sonar_version[:20] if isinstance(self.__sonar_version, bytes) else self.__sonar_version), limitedRepr(self.__key[:20] if isinstance(self.__key, bytes) else self.__key), limitedRepr(self.__name[:20] if isinstance(self.__name, bytes) else self.__name), limitedRepr(self.__description[:20] if isinstance(self.__description, bytes) else self.__description))




            _types_map = {
                'complexity': {'type': _complexity, 'subtype': None},
                'coverage': {'type': _coverage, 'subtype': None},
                'documentation': {'type': _documentation, 'subtype': None},
                'duplications': {'type': _duplications, 'subtype': None},
                'general': {'type': _general, 'subtype': None},
                'issues': {'type': _issues, 'subtype': None},
                'maintainability': {'type': _maintainability, 'subtype': None},
                'owasp_dependency_check': {'type': _owasp_dependency_check, 'subtype': None},
                'releasability': {'type': _releasability, 'subtype': None},
                'reliability': {'type': _reliability, 'subtype': None},
                'scm': {'type': _scm, 'subtype': None},
                'security': {'type': _security, 'subtype': None},
                'size': {'type': _size, 'subtype': None},
                'component': {'type': _component, 'subtype': None},
            }
            _formats_map = {
            }
            _validations_map = {
                'complexity': { 'required': False,},
                'coverage': { 'required': False,},
                'documentation': { 'required': False,},
                'duplications': { 'required': False,},
                'general': { 'required': False,},
                'issues': { 'required': False,},
                'maintainability': { 'required': False,},
                'owasp_dependency_check': { 'required': False,},
                'releasability': { 'required': False,},
                'reliability': { 'required': False,},
                'scm': { 'required': False,},
                'security': { 'required': False,},
                'size': { 'required': False,},
                'component': { 'required': False,},
            }

            def __init__(self
                    , complexity=None
                    , coverage=None
                    , documentation=None
                    , duplications=None
                    , general=None
                    , issues=None
                    , maintainability=None
                    , owasp_dependency_check=None
                    , releasability=None
                    , reliability=None
                    , scm=None
                    , security=None
                    , size=None
                    , component=None
                    ):
                self.__complexity = complexity
                self.__coverage = coverage
                self.__documentation = documentation
                self.__duplications = duplications
                self.__general = general
                self.__issues = issues
                self.__maintainability = maintainability
                self.__owasp_dependency_check = owasp_dependency_check
                self.__releasability = releasability
                self.__reliability = reliability
                self.__scm = scm
                self.__security = security
                self.__size = size
                self.__component = component
                pass

            def _get_complexity(self):
                return self.__complexity
            def _set_complexity(self, value):
                if value is not None and  not isinstance(value, QualitySchema._sonar._complexity):
                    raise TypeError("complexity must be QualitySchema._sonar._complexity")

                self.__complexity = value
            complexity = property(_get_complexity, _set_complexity)

            def _get_coverage(self):
                return self.__coverage
            def _set_coverage(self, value):
                if value is not None and  not isinstance(value, QualitySchema._sonar._coverage):
                    raise TypeError("coverage must be QualitySchema._sonar._coverage")

                self.__coverage = value
            coverage = property(_get_coverage, _set_coverage)

            def _get_documentation(self):
                return self.__documentation
            def _set_documentation(self, value):
                if value is not None and  not isinstance(value, QualitySchema._sonar._documentation):
                    raise TypeError("documentation must be QualitySchema._sonar._documentation")

                self.__documentation = value
            documentation = property(_get_documentation, _set_documentation)

            def _get_duplications(self):
                return self.__duplications
            def _set_duplications(self, value):
                if value is not None and  not isinstance(value, QualitySchema._sonar._duplications):
                    raise TypeError("duplications must be QualitySchema._sonar._duplications")

                self.__duplications = value
            duplications = property(_get_duplications, _set_duplications)

            def _get_general(self):
                return self.__general
            def _set_general(self, value):
                if value is not None and  not isinstance(value, QualitySchema._sonar._general):
                    raise TypeError("general must be QualitySchema._sonar._general")

                self.__general = value
            general = property(_get_general, _set_general)

            def _get_issues(self):
                return self.__issues
            def _set_issues(self, value):
                if value is not None and  not isinstance(value, QualitySchema._sonar._issues):
                    raise TypeError("issues must be QualitySchema._sonar._issues")

                self.__issues = value
            issues = property(_get_issues, _set_issues)

            def _get_maintainability(self):
                return self.__maintainability
            def _set_maintainability(self, value):
                if value is not None and  not isinstance(value, QualitySchema._sonar._maintainability):
                    raise TypeError("maintainability must be QualitySchema._sonar._maintainability")

                self.__maintainability = value
            maintainability = property(_get_maintainability, _set_maintainability)

            def _get_owasp_dependency_check(self):
                return self.__owasp_dependency_check
            def _set_owasp_dependency_check(self, value):
                if value is not None and  not isinstance(value, QualitySchema._sonar._owasp_dependency_check):
                    raise TypeError("owasp_dependency_check must be QualitySchema._sonar._owasp_dependency_check")

                self.__owasp_dependency_check = value
            owasp_dependency_check = property(_get_owasp_dependency_check, _set_owasp_dependency_check)

            def _get_releasability(self):
                return self.__releasability
            def _set_releasability(self, value):
                if value is not None and  not isinstance(value, QualitySchema._sonar._releasability):
                    raise TypeError("releasability must be QualitySchema._sonar._releasability")

                self.__releasability = value
            releasability = property(_get_releasability, _set_releasability)

            def _get_reliability(self):
                return self.__reliability
            def _set_reliability(self, value):
                if value is not None and  not isinstance(value, QualitySchema._sonar._reliability):
                    raise TypeError("reliability must be QualitySchema._sonar._reliability")

                self.__reliability = value
            reliability = property(_get_reliability, _set_reliability)

            def _get_scm(self):
                return self.__scm
            def _set_scm(self, value):
                if value is not None and  not isinstance(value, QualitySchema._sonar._scm):
                    raise TypeError("scm must be QualitySchema._sonar._scm")

                self.__scm = value
            scm = property(_get_scm, _set_scm)

            def _get_security(self):
                return self.__security
            def _set_security(self, value):
                if value is not None and  not isinstance(value, QualitySchema._sonar._security):
                    raise TypeError("security must be QualitySchema._sonar._security")

                self.__security = value
            security = property(_get_security, _set_security)

            def _get_size(self):
                return self.__size
            def _set_size(self, value):
                if value is not None and  not isinstance(value, QualitySchema._sonar._size):
                    raise TypeError("size must be QualitySchema._sonar._size")

                self.__size = value
            size = property(_get_size, _set_size)

            def _get_component(self):
                return self.__component
            def _set_component(self, value):
                if value is not None and  not isinstance(value, QualitySchema._sonar._component):
                    raise TypeError("component must be QualitySchema._sonar._component")

                self.__component = value
            component = property(_get_component, _set_component)


            @staticmethod
            def from_dict(d):
                v = {}
                if "complexity" in d:
                    v["complexity"] = QualitySchema._sonar._complexity.from_dict(d["complexity"]) if hasattr(QualitySchema._sonar._complexity, 'from_dict') else d["complexity"]
                if "coverage" in d:
                    v["coverage"] = QualitySchema._sonar._coverage.from_dict(d["coverage"]) if hasattr(QualitySchema._sonar._coverage, 'from_dict') else d["coverage"]
                if "documentation" in d:
                    v["documentation"] = QualitySchema._sonar._documentation.from_dict(d["documentation"]) if hasattr(QualitySchema._sonar._documentation, 'from_dict') else d["documentation"]
                if "duplications" in d:
                    v["duplications"] = QualitySchema._sonar._duplications.from_dict(d["duplications"]) if hasattr(QualitySchema._sonar._duplications, 'from_dict') else d["duplications"]
                if "general" in d:
                    v["general"] = QualitySchema._sonar._general.from_dict(d["general"]) if hasattr(QualitySchema._sonar._general, 'from_dict') else d["general"]
                if "issues" in d:
                    v["issues"] = QualitySchema._sonar._issues.from_dict(d["issues"]) if hasattr(QualitySchema._sonar._issues, 'from_dict') else d["issues"]
                if "maintainability" in d:
                    v["maintainability"] = QualitySchema._sonar._maintainability.from_dict(d["maintainability"]) if hasattr(QualitySchema._sonar._maintainability, 'from_dict') else d["maintainability"]
                if "owasp-dependency-check" in d:
                    v["owasp_dependency_check"] = QualitySchema._sonar._owasp_dependency_check.from_dict(d["owasp-dependency-check"]) if hasattr(QualitySchema._sonar._owasp_dependency_check, 'from_dict') else d["owasp-dependency-check"]
                if "releasability" in d:
                    v["releasability"] = QualitySchema._sonar._releasability.from_dict(d["releasability"]) if hasattr(QualitySchema._sonar._releasability, 'from_dict') else d["releasability"]
                if "reliability" in d:
                    v["reliability"] = QualitySchema._sonar._reliability.from_dict(d["reliability"]) if hasattr(QualitySchema._sonar._reliability, 'from_dict') else d["reliability"]
                if "scm" in d:
                    v["scm"] = QualitySchema._sonar._scm.from_dict(d["scm"]) if hasattr(QualitySchema._sonar._scm, 'from_dict') else d["scm"]
                if "security" in d:
                    v["security"] = QualitySchema._sonar._security.from_dict(d["security"]) if hasattr(QualitySchema._sonar._security, 'from_dict') else d["security"]
                if "size" in d:
                    v["size"] = QualitySchema._sonar._size.from_dict(d["size"]) if hasattr(QualitySchema._sonar._size, 'from_dict') else d["size"]
                if "component" in d:
                    v["component"] = QualitySchema._sonar._component.from_dict(d["component"]) if hasattr(QualitySchema._sonar._component, 'from_dict') else d["component"]
                return QualitySchema._sonar(**v)


            def as_dict(self):
                d = {}
                if self.__complexity is not None:
                    d['complexity'] = self.__complexity.as_dict() if hasattr(self.__complexity, 'as_dict') else self.__complexity
                if self.__coverage is not None:
                    d['coverage'] = self.__coverage.as_dict() if hasattr(self.__coverage, 'as_dict') else self.__coverage
                if self.__documentation is not None:
                    d['documentation'] = self.__documentation.as_dict() if hasattr(self.__documentation, 'as_dict') else self.__documentation
                if self.__duplications is not None:
                    d['duplications'] = self.__duplications.as_dict() if hasattr(self.__duplications, 'as_dict') else self.__duplications
                if self.__general is not None:
                    d['general'] = self.__general.as_dict() if hasattr(self.__general, 'as_dict') else self.__general
                if self.__issues is not None:
                    d['issues'] = self.__issues.as_dict() if hasattr(self.__issues, 'as_dict') else self.__issues
                if self.__maintainability is not None:
                    d['maintainability'] = self.__maintainability.as_dict() if hasattr(self.__maintainability, 'as_dict') else self.__maintainability
                if self.__owasp_dependency_check is not None:
                    d['owasp-dependency-check'] = self.__owasp_dependency_check.as_dict() if hasattr(self.__owasp_dependency_check, 'as_dict') else self.__owasp_dependency_check
                if self.__releasability is not None:
                    d['releasability'] = self.__releasability.as_dict() if hasattr(self.__releasability, 'as_dict') else self.__releasability
                if self.__reliability is not None:
                    d['reliability'] = self.__reliability.as_dict() if hasattr(self.__reliability, 'as_dict') else self.__reliability
                if self.__scm is not None:
                    d['scm'] = self.__scm.as_dict() if hasattr(self.__scm, 'as_dict') else self.__scm
                if self.__security is not None:
                    d['security'] = self.__security.as_dict() if hasattr(self.__security, 'as_dict') else self.__security
                if self.__size is not None:
                    d['size'] = self.__size.as_dict() if hasattr(self.__size, 'as_dict') else self.__size
                if self.__component is not None:
                    d['component'] = self.__component.as_dict() if hasattr(self.__component, 'as_dict') else self.__component
                return d

            def __repr__(self):
                return "<Class _sonar. complexity: {}, coverage: {}, documentation: {}, duplications: {}, general: {}, issues: {}, maintainability: {}, owasp_dependency_check: {}, releasability: {}, reliability: {}, scm: {}, security: {}, size: {}, component: {}>".format(limitedRepr(self.__complexity[:20] if isinstance(self.__complexity, bytes) else self.__complexity), limitedRepr(self.__coverage[:20] if isinstance(self.__coverage, bytes) else self.__coverage), limitedRepr(self.__documentation[:20] if isinstance(self.__documentation, bytes) else self.__documentation), limitedRepr(self.__duplications[:20] if isinstance(self.__duplications, bytes) else self.__duplications), limitedRepr(self.__general[:20] if isinstance(self.__general, bytes) else self.__general), limitedRepr(self.__issues[:20] if isinstance(self.__issues, bytes) else self.__issues), limitedRepr(self.__maintainability[:20] if isinstance(self.__maintainability, bytes) else self.__maintainability), limitedRepr(self.__owasp_dependency_check[:20] if isinstance(self.__owasp_dependency_check, bytes) else self.__owasp_dependency_check), limitedRepr(self.__releasability[:20] if isinstance(self.__releasability, bytes) else self.__releasability), limitedRepr(self.__reliability[:20] if isinstance(self.__reliability, bytes) else self.__reliability), limitedRepr(self.__scm[:20] if isinstance(self.__scm, bytes) else self.__scm), limitedRepr(self.__security[:20] if isinstance(self.__security, bytes) else self.__security), limitedRepr(self.__size[:20] if isinstance(self.__size, bytes) else self.__size), limitedRepr(self.__component[:20] if isinstance(self.__component, bytes) else self.__component))

    class _scan:
            class _mcafee:



                    _types_map = {
                        'Total_files': {'type': int, 'subtype': None},
                        'Clean': {'type': int, 'subtype': None},
                        'Possibly_Infected': {'type': int, 'subtype': None},
                        'Total_Objects': {'type': int, 'subtype': None},
                        'Objects_Possibly_Infected': {'type': int, 'subtype': None},
                        'Not_Scanned': {'type': int, 'subtype': None},
                    }
                    _formats_map = {
                    }
                    _validations_map = {
                        'Total_files': { 'required': False,},
                        'Clean': { 'required': False,},
                        'Possibly_Infected': { 'required': False,},
                        'Total_Objects': { 'required': False,},
                        'Objects_Possibly_Infected': { 'required': False,},
                        'Not_Scanned': { 'required': False,},
                    }

                    def __init__(self
                            , Total_files=None
                            , Clean=None
                            , Possibly_Infected=None
                            , Total_Objects=None
                            , Objects_Possibly_Infected=None
                            , Not_Scanned=None
                            ):
                        self.__Total_files = Total_files
                        self.__Clean = Clean
                        self.__Possibly_Infected = Possibly_Infected
                        self.__Total_Objects = Total_Objects
                        self.__Objects_Possibly_Infected = Objects_Possibly_Infected
                        self.__Not_Scanned = Not_Scanned
                        pass

                    def _get_Total_files(self):
                        return self.__Total_files
                    def _set_Total_files(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("Total_files must be int")

                        self.__Total_files = value
                    Total_files = property(_get_Total_files, _set_Total_files)

                    def _get_Clean(self):
                        return self.__Clean
                    def _set_Clean(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("Clean must be int")

                        self.__Clean = value
                    Clean = property(_get_Clean, _set_Clean)

                    def _get_Possibly_Infected(self):
                        return self.__Possibly_Infected
                    def _set_Possibly_Infected(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("Possibly_Infected must be int")

                        self.__Possibly_Infected = value
                    Possibly_Infected = property(_get_Possibly_Infected, _set_Possibly_Infected)

                    def _get_Total_Objects(self):
                        return self.__Total_Objects
                    def _set_Total_Objects(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("Total_Objects must be int")

                        self.__Total_Objects = value
                    Total_Objects = property(_get_Total_Objects, _set_Total_Objects)

                    def _get_Objects_Possibly_Infected(self):
                        return self.__Objects_Possibly_Infected
                    def _set_Objects_Possibly_Infected(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("Objects_Possibly_Infected must be int")

                        self.__Objects_Possibly_Infected = value
                    Objects_Possibly_Infected = property(_get_Objects_Possibly_Infected, _set_Objects_Possibly_Infected)

                    def _get_Not_Scanned(self):
                        return self.__Not_Scanned
                    def _set_Not_Scanned(self, value):
                        if value is not None and  not isinstance(value, int):
                            raise TypeError("Not_Scanned must be int")

                        self.__Not_Scanned = value
                    Not_Scanned = property(_get_Not_Scanned, _set_Not_Scanned)


                    @staticmethod
                    def from_dict(d):
                        v = {}
                        if "Total-files" in d:
                            v["Total_files"] = int.from_dict(d["Total-files"]) if hasattr(int, 'from_dict') else d["Total-files"]
                        if "Clean" in d:
                            v["Clean"] = int.from_dict(d["Clean"]) if hasattr(int, 'from_dict') else d["Clean"]
                        if "Possibly-Infected" in d:
                            v["Possibly_Infected"] = int.from_dict(d["Possibly-Infected"]) if hasattr(int, 'from_dict') else d["Possibly-Infected"]
                        if "Total-Objects" in d:
                            v["Total_Objects"] = int.from_dict(d["Total-Objects"]) if hasattr(int, 'from_dict') else d["Total-Objects"]
                        if "Objects-Possibly-Infected" in d:
                            v["Objects_Possibly_Infected"] = int.from_dict(d["Objects-Possibly-Infected"]) if hasattr(int, 'from_dict') else d["Objects-Possibly-Infected"]
                        if "Not-Scanned" in d:
                            v["Not_Scanned"] = int.from_dict(d["Not-Scanned"]) if hasattr(int, 'from_dict') else d["Not-Scanned"]
                        return QualitySchema._scan._mcafee(**v)


                    def as_dict(self):
                        d = {}
                        if self.__Total_files is not None:
                            d['Total-files'] = self.__Total_files.as_dict() if hasattr(self.__Total_files, 'as_dict') else self.__Total_files
                        if self.__Clean is not None:
                            d['Clean'] = self.__Clean.as_dict() if hasattr(self.__Clean, 'as_dict') else self.__Clean
                        if self.__Possibly_Infected is not None:
                            d['Possibly-Infected'] = self.__Possibly_Infected.as_dict() if hasattr(self.__Possibly_Infected, 'as_dict') else self.__Possibly_Infected
                        if self.__Total_Objects is not None:
                            d['Total-Objects'] = self.__Total_Objects.as_dict() if hasattr(self.__Total_Objects, 'as_dict') else self.__Total_Objects
                        if self.__Objects_Possibly_Infected is not None:
                            d['Objects-Possibly-Infected'] = self.__Objects_Possibly_Infected.as_dict() if hasattr(self.__Objects_Possibly_Infected, 'as_dict') else self.__Objects_Possibly_Infected
                        if self.__Not_Scanned is not None:
                            d['Not-Scanned'] = self.__Not_Scanned.as_dict() if hasattr(self.__Not_Scanned, 'as_dict') else self.__Not_Scanned
                        return d

                    def __repr__(self):
                        return "<Class _mcafee. Total_files: {}, Clean: {}, Possibly_Infected: {}, Total_Objects: {}, Objects_Possibly_Infected: {}, Not_Scanned: {}>".format(limitedRepr(self.__Total_files[:20] if isinstance(self.__Total_files, bytes) else self.__Total_files), limitedRepr(self.__Clean[:20] if isinstance(self.__Clean, bytes) else self.__Clean), limitedRepr(self.__Possibly_Infected[:20] if isinstance(self.__Possibly_Infected, bytes) else self.__Possibly_Infected), limitedRepr(self.__Total_Objects[:20] if isinstance(self.__Total_Objects, bytes) else self.__Total_Objects), limitedRepr(self.__Objects_Possibly_Infected[:20] if isinstance(self.__Objects_Possibly_Infected, bytes) else self.__Objects_Possibly_Infected), limitedRepr(self.__Not_Scanned[:20] if isinstance(self.__Not_Scanned, bytes) else self.__Not_Scanned))




            _types_map = {
                'mcafee': {'type': _mcafee, 'subtype': None},
            }
            _formats_map = {
            }
            _validations_map = {
                'mcafee': { 'required': False,},
            }

            def __init__(self
                    , mcafee=None
                    ):
                self.__mcafee = mcafee
                pass

            def _get_mcafee(self):
                return self.__mcafee
            def _set_mcafee(self, value):
                if value is not None and  not isinstance(value, QualitySchema._scan._mcafee):
                    raise TypeError("mcafee must be QualitySchema._scan._mcafee")

                self.__mcafee = value
            mcafee = property(_get_mcafee, _set_mcafee)


            @staticmethod
            def from_dict(d):
                v = {}
                if "mcafee" in d:
                    v["mcafee"] = QualitySchema._scan._mcafee.from_dict(d["mcafee"]) if hasattr(QualitySchema._scan._mcafee, 'from_dict') else d["mcafee"]
                return QualitySchema._scan(**v)


            def as_dict(self):
                d = {}
                if self.__mcafee is not None:
                    d['mcafee'] = self.__mcafee.as_dict() if hasattr(self.__mcafee, 'as_dict') else self.__mcafee
                return d

            def __repr__(self):
                return "<Class _scan. mcafee: {}>".format(limitedRepr(self.__mcafee[:20] if isinstance(self.__mcafee, bytes) else self.__mcafee))




    _types_map = {
        'schema': {'type': str, 'subtype': None},
        'ident': {'type': identifier, 'subtype': None},
        'name': {'type': str, 'subtype': None},
        'description': {'type': str, 'subtype': None},
        'history': {'type': list, 'subtype': event},
        'tags': {'type': list, 'subtype': str},
        'mcscan': {'type': _mcscan, 'subtype': None},
        'sonar': {'type': _sonar, 'subtype': None},
        'scan': {'type': _scan, 'subtype': None},
        'status': {'type': str, 'subtype': None},
    }
    _formats_map = {
    }
    _validations_map = {
        'schema': { 'required': False,},
        'ident': { 'required': False,},
        'name': { 'required': False,},
        'description': { 'required': False,},
        'history': { 'required': False,},
        'tags': { 'required': False,},
        'mcscan': { 'required': False,},
        'sonar': { 'required': False,},
        'scan': { 'required': False,},
        'status': { 'required': False,},
    }

    def __init__(self
            , *args
            , schema=None
            , ident=None
            , name=None
            , description=None
            , history=None
            , tags=None
            , mcscan=None
            , sonar=None
            , scan=None
            , status='Failed'
            , **kwargs
            ):
        self.__schema = schema
        self.__ident = ident
        self.__name = name
        self.__description = description
        self.__history = history
        self.__tags = tags
        self.__mcscan = mcscan
        self.__sonar = sonar
        self.__scan = scan
        self.__status = status
        super().__init__(*args, **kwargs)
        pass

    def _get_schema(self):
        return self.__schema
    def _set_schema(self, value):
        if value is not None and  not isinstance(value, str):
            raise TypeError("schema must be str")

        self.__schema = value
    schema = property(_get_schema, _set_schema)

    def _get_ident(self):
        return self.__ident
    def _set_ident(self, value):
        if value is not None and  not isinstance(value, identifier):
            raise TypeError("ident must be identifier")

        self.__ident = value
    ident = property(_get_ident, _set_ident)

    def _get_name(self):
        return self.__name
    def _set_name(self, value):
        if value is not None and  not isinstance(value, str):
            raise TypeError("name must be str")

        self.__name = value
    name = property(_get_name, _set_name)

    def _get_description(self):
        return self.__description
    def _set_description(self, value):
        if value is not None and  not isinstance(value, str):
            raise TypeError("description must be str")

        self.__description = value
    description = property(_get_description, _set_description)

    def _get_history(self):
        return self.__history
    def _set_history(self, value):
        if value is not None and  not isinstance(value, list):
            raise TypeError("history must be list")
        if value is not None and  not all(isinstance(i, event) for i in value):
            raise TypeError("history list values must be event")

        self.__history = value
    history = property(_get_history, _set_history)

    def _get_tags(self):
        return self.__tags
    def _set_tags(self, value):
        if value is not None and  not isinstance(value, list):
            raise TypeError("tags must be list")
        if value is not None and  not all(isinstance(i, str) for i in value):
            raise TypeError("tags list values must be str")

        self.__tags = value
    tags = property(_get_tags, _set_tags)

    def _get_mcscan(self):
        return self.__mcscan
    def _set_mcscan(self, value):
        if value is not None and  not isinstance(value, QualitySchema._mcscan):
            raise TypeError("mcscan must be QualitySchema._mcscan")

        self.__mcscan = value
    mcscan = property(_get_mcscan, _set_mcscan)

    def _get_sonar(self):
        return self.__sonar
    def _set_sonar(self, value):
        if value is not None and  not isinstance(value, QualitySchema._sonar):
            raise TypeError("sonar must be QualitySchema._sonar")

        self.__sonar = value
    sonar = property(_get_sonar, _set_sonar)

    def _get_scan(self):
        return self.__scan
    def _set_scan(self, value):
        if value is not None and  not isinstance(value, QualitySchema._scan):
            raise TypeError("scan must be QualitySchema._scan")

        self.__scan = value
    scan = property(_get_scan, _set_scan)

    def _get_status(self):
        return self.__status
    def _set_status(self, value):
        if value is not None and  not isinstance(value, str):
            raise TypeError("status must be str")

        self.__status = value
    status = property(_get_status, _set_status)


    @staticmethod
    def from_dict(d):
        v = d.copy()
        if "schema" in d:
            v["schema"] = str.from_dict(d["schema"]) if hasattr(str, 'from_dict') else d["schema"]
        if "ident" in d:
            v["ident"] = identifier.from_dict(d["ident"]) if hasattr(identifier, 'from_dict') else d["ident"]
        if "name" in d:
            v["name"] = str.from_dict(d["name"]) if hasattr(str, 'from_dict') else d["name"]
        if "description" in d:
            v["description"] = str.from_dict(d["description"]) if hasattr(str, 'from_dict') else d["description"]
        if "history" in d:
            v["history"] = [event.from_dict(p) if hasattr(event, 'from_dict') else p for p in d["history"]]
        if "tags" in d:
            v["tags"] = [str.from_dict(p) if hasattr(str, 'from_dict') else p for p in d["tags"]]
        if "mcscan" in d:
            v["mcscan"] = QualitySchema._mcscan.from_dict(d["mcscan"]) if hasattr(QualitySchema._mcscan, 'from_dict') else d["mcscan"]
        if "sonar" in d:
            v["sonar"] = QualitySchema._sonar.from_dict(d["sonar"]) if hasattr(QualitySchema._sonar, 'from_dict') else d["sonar"]
        if "scan" in d:
            v["scan"] = QualitySchema._scan.from_dict(d["scan"]) if hasattr(QualitySchema._scan, 'from_dict') else d["scan"]
        if "status" in d:
            v["status"] = str.from_dict(d["status"]) if hasattr(str, 'from_dict') else d["status"]
        return QualitySchema(**v)


    def as_dict(self):
        d = super().as_dict()
        if self.__schema is not None:
            d['schema'] = self.__schema.as_dict() if hasattr(self.__schema, 'as_dict') else self.__schema
        if self.__ident is not None:
            d['ident'] = self.__ident.as_dict() if hasattr(self.__ident, 'as_dict') else self.__ident
        if self.__name is not None:
            d['name'] = self.__name.as_dict() if hasattr(self.__name, 'as_dict') else self.__name
        if self.__description is not None:
            d['description'] = self.__description.as_dict() if hasattr(self.__description, 'as_dict') else self.__description
        if self.__history is not None:
            d['history'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__history]
        if self.__tags is not None:
            d['tags'] = [p.as_dict() if hasattr(p, 'as_dict') else p for p in self.__tags]
        if self.__mcscan is not None:
            d['mcscan'] = self.__mcscan.as_dict() if hasattr(self.__mcscan, 'as_dict') else self.__mcscan
        if self.__sonar is not None:
            d['sonar'] = self.__sonar.as_dict() if hasattr(self.__sonar, 'as_dict') else self.__sonar
        if self.__scan is not None:
            d['scan'] = self.__scan.as_dict() if hasattr(self.__scan, 'as_dict') else self.__scan
        if self.__status is not None:
            d['status'] = self.__status.as_dict() if hasattr(self.__status, 'as_dict') else self.__status
        return d

    def __repr__(self):
        return "<Class QualitySchema. schema: {}, ident: {}, name: {}, description: {}, history: {}, tags: {}, mcscan: {}, sonar: {}, scan: {}, status: {}>".format(limitedRepr(self.__schema[:20] if isinstance(self.__schema, bytes) else self.__schema), limitedRepr(self.__ident[:20] if isinstance(self.__ident, bytes) else self.__ident), limitedRepr(self.__name[:20] if isinstance(self.__name, bytes) else self.__name), limitedRepr(self.__description[:20] if isinstance(self.__description, bytes) else self.__description), limitedRepr(self.__history[:20] if isinstance(self.__history, bytes) else self.__history), limitedRepr(self.__tags[:20] if isinstance(self.__tags, bytes) else self.__tags), limitedRepr(self.__mcscan[:20] if isinstance(self.__mcscan, bytes) else self.__mcscan), limitedRepr(self.__sonar[:20] if isinstance(self.__sonar, bytes) else self.__sonar), limitedRepr(self.__scan[:20] if isinstance(self.__scan, bytes) else self.__scan), limitedRepr(self.__status[:20] if isinstance(self.__status, bytes) else self.__status))

