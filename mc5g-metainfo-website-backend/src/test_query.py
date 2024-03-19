#!/usr/bin/python3

import re, unittest

from query import Query
from module_utils.schema.productschema import ProductSchema

class TestCompileQuery(unittest.TestCase):
  def checkCompileEqual(self, schema, input, output):
    result = Query(schema, input).getCompiledQuery()
    #print(result)
    #print(output)
    self.assertEqual(result, output)
  
  def checkCompileRaise(self, schema, input, output):
      with self.assertRaises(output):
        try:
          Query(schema, input)
        except RuntimeError as e:
          #print(e)
          raise e

  def test_status(self):
    self.checkCompileEqual(ProductSchema, { 'status': 'GA Released' }, { 'status': 'GA Released' })

  def test_not_status(self):
    self.checkCompileEqual(ProductSchema, { '$not': { 'status': 'GA Released' } }, { '$not': { 'status': 'GA Released' } })

  def test_and_name_status(self):
    self.checkCompileEqual(ProductSchema, { '$and': [{ 'name': 'AUSF', 'status': 'GA Released' }] }, { '$and': [{ 'name': 'AUSF', 'status': 'GA Released' }] })

  def test_or_name_status(self):
    self.checkCompileEqual(ProductSchema, { '$or': [{ 'name': 'AUSF', 'status': 'GA Released' }] }, { '$or': [{ 'name': 'AUSF', 'status': 'GA Released' }] })

  def test_not_and_name_status(self):
    self.checkCompileEqual(ProductSchema, { '$not': { '$and': [{'name': 'AUSF', 'status': 'GA Released' }] } }, { '$not': { '$and': [{ 'name': 'AUSF', 'status': 'GA Released' }] } })

  def test_and_name_not_status(self):
    self.checkCompileEqual(ProductSchema, { '$and': [{ 'name': 'AUSF' }, {'$not': { 'status': 'GA Released' } }] }, { '$and': [{ 'name': 'AUSF' }, { '$not': { 'status': 'GA Released' } }] })

  def test_tags_anyOf(self):
    self.checkCompileEqual(ProductSchema, { 'tags': {'$anyOf': ['MC5G-AUSF-1.2209.0', 'MC5G-5G-EIR-1.2209.0'] } }, { 'tags': {'$in': ['MC5G-AUSF-1.2209.0', 'MC5G-5G-EIR-1.2209.0'] } })

  def test_tags_allOf(self):
    self.checkCompileEqual(ProductSchema, { 'tags': {'$allOf': ['MC5G-AUSF-1.2209.0', 'MC5G-5G-EIR-1.2209.0'] } }, { 'tags': {'$all': ['MC5G-AUSF-1.2209.0', 'MC5G-5G-EIR-1.2209.0'] } })

  def test_ident_groupId(self):
    self.checkCompileEqual(ProductSchema, { 'ident': {'groupId': 'com.hpe.cms.5g.prod'} }, { 'ident.groupId': 'com.hpe.cms.5g.prod' })

  def test_ident_groupId_artifactId(self):
    self.checkCompileEqual(ProductSchema, { 'ident': {'groupId': 'com.hpe.cms.5g.prod', 'artifactId': 'hpe-nf-ausf-prod'} }, { 'ident.groupId': 'com.hpe.cms.5g.prod', 'ident.artifactId': 'hpe-nf-ausf-prod' })

  def test_ident_groupId_artifactId_version_regex(self):
    self.checkCompileEqual(ProductSchema, { 'ident': {'groupId': 'com.hpe.cms.5g.prod', 'artifactId': 'hpe-nf-ausf-prod', 'version': '/1\\.[0-9]\\.[0-9]-.*/'} }, { 'ident.groupId': 'com.hpe.cms.5g.prod', 'ident.artifactId': 'hpe-nf-ausf-prod', 'ident.version': re.compile('1\\.[0-9]\\.[0-9]-.*') })

  def test_components_anyOf(self):
    self.checkCompileEqual(
      ProductSchema,
      {
        "components": {
          "$anyOf": [
            {
              "groupId": "com.hpe.cms.5g.comp",
              "artifactId": "hpe-nf-operator-comp",
              "version": "0.7.0-202209300802-7"
            },
            {
              "groupId": "com.hpe.cms.5g.comp",
              "artifactId": "hpe-nf-ausf-nausf-auth-comp",
              "version": "0.17.0-202210041015-5"
            }
          ]
        }
      },
      {
        "$and": [
          {
            "$or": [
              {
                "components": {
                  "$elemMatch": {
                    "groupId": "com.hpe.cms.5g.comp",
                    "artifactId": "hpe-nf-operator-comp",
                    "version": "0.7.0-202209300802-7"
                  }
                }
              },
              {
                "components": {
                  "$elemMatch": {
                    "groupId": "com.hpe.cms.5g.comp",
                    "artifactId": "hpe-nf-ausf-nausf-auth-comp",
                    "version": "0.17.0-202210041015-5"
                  }
                }
              }
            ]
          }
        ]
      }
    )

  def test_packages_yum_allOf(self):
    self.checkCompileEqual(
      ProductSchema,
      {
        "packages": {
          "yum": {
            "$allOf": [
              {
                "name": "hpe-5g-pgw-ansible",
                "version": "0.12.0-4654.git27e661c.el8"
              },
              {
                "name": "hpe-5g-pgw-workflow-rpm",
                "version": "0.12.0-4654.git27e661c.el8"
              }
            ]
          }
        }
      },
      {
        "$and": [
          {
            "packages.yum": {
              "$elemMatch": {
                "name": "hpe-5g-pgw-ansible",
                "version": "0.12.0-4654.git27e661c.el8"
              }
            }
          },
          {
            "packages.yum": {
              "$elemMatch": {
                "name": "hpe-5g-pgw-workflow-rpm",
                "version": "0.12.0-4654.git27e661c.el8"
              }
            }
          }
        ]
      }
    )

  def test_components_allOf_packages_yum_allOf(self):
    self.checkCompileEqual(
      ProductSchema,
      {
        "components": {
          "$allOf": [
            {
              "groupId": "com.hpe.cms.5g.comp",
              "artifactId": "hpe-nf-operator-comp",
              "version": "0.7.0-202209300802-7"
            },
            {
              "groupId": "com.hpe.cms.5g.comp",
              "artifactId": "hpe-nf-ausf-nausf-auth-comp",
              "version": "0.17.0-202210041015-5"
            }
          ]
        },
        "packages": {
          "yum": {
            "$allOf": [
              {
                "name": "hpe-5g-pgw-ansible",
                "version": "0.12.0-4654.git27e661c.el8"
              },
              {
                "name": "hpe-5g-pgw-workflow-rpm",
                "version": "0.12.0-4654.git27e661c.el8"
              }
            ]
          }
        }
      },
      {
        "$and": [
          {
            "components": {
              "$elemMatch": {
                "groupId": "com.hpe.cms.5g.comp",
                "artifactId": "hpe-nf-operator-comp",
                "version": "0.7.0-202209300802-7"
              }
            }
          },
          {
            "components": {
              "$elemMatch": {
                "groupId": "com.hpe.cms.5g.comp",
                "artifactId": "hpe-nf-ausf-nausf-auth-comp",
                "version": "0.17.0-202210041015-5"
              }
            }
          },
          {
            "packages.yum": {
              "$elemMatch": {
                "name": "hpe-5g-pgw-ansible",
                "version": "0.12.0-4654.git27e661c.el8"
              }
            }
          },
          {
            "packages.yum": {
              "$elemMatch": {
                "name": "hpe-5g-pgw-workflow-rpm",
                "version": "0.12.0-4654.git27e661c.el8"
              }
            }
          }
        ]
      }
    )

  def test_components_allOf_packages_yum_anyOf_packages_docker_anyOf(self):
    self.checkCompileEqual(
      ProductSchema,
      {
        "components": {
          "$allOf": [
            {
              "groupId": "com.hpe.cms.5g.comp",
              "artifactId": "hpe-nf-operator-comp",
              "version": "0.7.0-202209300802-7"
            },
            {
              "groupId": "com.hpe.cms.5g.comp",
              "artifactId": "hpe-nf-ausf-nausf-auth-comp",
              "version": "0.17.0-202210041015-5"
            }
          ]
        },
        "packages": {
          "yum": {
            "$anyOf": [
              {
                "name": "hpe-5g-pgw-ansible",
                "version": "0.12.0-4654.git27e661c.el8"
              },
              {
                "name": "hpe-5g-pgw-workflow-rpm",
                "version": "0.12.0-4654.git27e661c.el8"
              }
            ]
          },
          "docker": {
            "$anyOf": [
              {
                "name": "hpe-5g-pgw-ansible",
                "tag": "0.12.0-4654.git27e661c.el8"
              },
              {
                "name": "hpe-5g-pgw-workflow-rpm",
                "tag": "0.12.0-4654.git27e661c.el8"
              }
            ]
          }
        }
      },
      {
        "$and": [
          {
            '$or': [
              {
                "packages.yum": {
                  "$elemMatch": {
                    "name": "hpe-5g-pgw-ansible",
                    "version": "0.12.0-4654.git27e661c.el8"
                  }
                }
              },
              {
                "packages.yum": {
                  "$elemMatch": {
                    "name": "hpe-5g-pgw-workflow-rpm",
                    "version": "0.12.0-4654.git27e661c.el8"
                  }
                }
              }
            ]
          },
          {
            '$or': [
              {
                "packages.docker": {
                  "$elemMatch": {
                    "name": "hpe-5g-pgw-ansible",
                    "tag": "0.12.0-4654.git27e661c.el8"
                  }
                }
              },
              {
                "packages.docker": {
                  "$elemMatch": {
                    "name": "hpe-5g-pgw-workflow-rpm",
                    "tag": "0.12.0-4654.git27e661c.el8"
                  }
                }
              }
            ]
          },
          {
            "components": {
              "$elemMatch": {
                "groupId": "com.hpe.cms.5g.comp",
                "artifactId": "hpe-nf-operator-comp",
                "version": "0.7.0-202209300802-7"
              }
            }
          },
          {
            "components": {
              "$elemMatch": {
                "groupId": "com.hpe.cms.5g.comp",
                "artifactId": "hpe-nf-ausf-nausf-auth-comp",
                "version": "0.17.0-202210041015-5"
              }
            }
          }
        ]
      }
    )

  def test_status_invalid_not(self):
    self.checkCompileRaise(ProductSchema, { 'status': { '$not': 'GA Released' } }, RuntimeError)

  def test_status_invalid_type(self):
    self.checkCompileRaise(ProductSchema, { 'status': True }, RuntimeError)

  def test_tags_anyOf_invalid_type(self):
    self.checkCompileRaise(ProductSchema, { 'tags': {'$anyOf': True } }, RuntimeError)

  def test_tags_anyOf_invalid_subtype(self):
    self.checkCompileRaise(ProductSchema, { 'tags': {'$anyOf': ['MC5G-AUSF-1.2209.0', True] } }, RuntimeError)

  def test_ident_invalid_type(self):
    self.checkCompileRaise(ProductSchema, { 'ident': True }, RuntimeError)

  def test_ident_invalid_operator(self):
    self.checkCompileRaise(ProductSchema, { 'ident': { '$in': ['GA Released'] } }, RuntimeError)

  def test_ident_invalid_subtype(self):
    self.checkCompileRaise(ProductSchema, { 'ident': {'groupId': 'com.hpe.cms.5g.prod', 'artifactId': True} }, RuntimeError)

  def test_components_invalid_operator(self):
    self.checkCompileRaise(
      ProductSchema,
      {
        "components": {
          "$in": [
            {
              "groupId": "com.hpe.cms.5g.comp",
              "artifactId": "hpe-nf-operator-comp",
              "version": "0.7.0-202209300802-7"
            },
            {
              "groupId": "com.hpe.cms.5g.comp",
              "artifactId": "hpe-nf-ausf-nausf-auth-comp",
              "version": "0.17.0-202210041015-5"
            }
          ]
        }
      },
      RuntimeError
    )

  def test_components_invalid_subkey(self):
    self.checkCompileRaise(
      ProductSchema,
      {
        "components": {
          "$anyOf": [
            {
              "badKey": True
            }
          ]
        }
      },
      RuntimeError
    )

  def test_components_invalid_subvalue(self):
    self.checkCompileRaise(
      ProductSchema,
      {
        "components": {
          "$anyOf": [
            {
              "groupId": True
            }
          ]
        }
      },
      RuntimeError
    )

  def test_components_invalid_value(self):
    self.checkCompileRaise(
      ProductSchema,
      {
        "components": {
          "$anyOf": [
            True
          ]
        }
      },
      RuntimeError
    )

if __name__ == '__main__':
  unittest.main()