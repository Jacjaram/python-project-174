import os
import subprocess
from gendiff.scripts.gendiff import generate_diff


def test_generate_diff():
    dir_path = os.path.dirname(__file__)
    file1 = os.path.join(dir_path, 'fixtures', 'test_file1.json')
    file2 = os.path.join(dir_path, 'fixtures', 'test_file2.json')
    expected = '''{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow:
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}'''
    result = generate_diff(file1, file2)
    assert result == expected


def test_equal():
    expected = '''{
    common: {
        setting1: Value 1
        setting2: 200
        setting3: true
        setting6: {
            doge: {
                wow:
            }
            key: value
        }
    }
    group1: {
        baz: bas
        foo: bar
        nest: {
            key: value
        }
    }
    group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
}'''
    dir_path = os.path.dirname(__file__)
    file1 = os.path.join(dir_path, 'fixtures', 'test_file1.json')
    file3 = os.path.join(dir_path, 'fixtures', 'test_file1_copy.json')
    result = generate_diff(file1, file3)
    assert result == expected


def test_yaml_generate_diff():
    dir_path = os.path.dirname(__file__)
    file1 = os.path.join(dir_path, 'fixtures', 'test_file1.yml')
    file2 = os.path.join(dir_path, 'fixtures', 'test_file2.yaml')
    expected = '''{
    common: {
        setting1: Value 1
        setting2: 200
        setting3: true
        setting6: {
            doge: {
                wow:
            }
            key: value
        }
    }
    group1: {
        baz: bas
        foo: bar
        nest: {
            key: value
        }
    }
    group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
}'''
    result = generate_diff(file1, file2)
    assert result == expected


def test_script_run():
    dir_path = os.path.dirname(__file__)
    file1 = os.path.join(dir_path, 'fixtures', 'test_file1.json')
    file2 = os.path.join(dir_path, 'fixtures', 'test_file2.json')
    expected = '''{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow:
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}'''
    result = subprocess.run(
        ["python", "-m", "gendiff.scripts.gendiff", file1, file2],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert result.stdout.strip() == expected.strip()


def test_format_plain():
    dir_path = os.path.dirname(__file__)
    file1 = os.path.join(dir_path, 'fixtures', 'test_file1.json')
    file2 = os.path.join(dir_path, 'fixtures', 'test_file2.json')
    expected = """Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]"""
    result = generate_diff(file1, file2, 'plain')
    assert result == expected


def test_format_json():
    dir_path = os.path.dirname(__file__)
    file1 = os.path.join(dir_path, 'fixtures', 'test_file1.json')
    file2 = os.path.join(dir_path, 'fixtures', 'test_file2.json')
    expected = """{
  "common": {
    "status": "nested",
    "children": {
      "follow": {
        "status": "added",
        "value": false
      },
      "setting1": {
        "status": "unchanged",
        "value": "Value 1"
      },
      "setting2": {
        "status": "removed",
        "value": 200
      },
      "setting3": {
        "status": "changed",
        "old_value": true,
        "new_value": null
      },
      "setting4": {
        "status": "added",
        "value": "blah blah"
      },
      "setting5": {
        "status": "added",
        "value": {
          "key5": "value5"
        }
      },
      "setting6": {
        "status": "nested",
        "children": {
          "doge": {
            "status": "nested",
            "children": {
              "wow": {
                "status": "changed",
                "old_value": "",
                "new_value": "so much"
              }
            }
          },
          "key": {
            "status": "unchanged",
            "value": "value"
          },
          "ops": {
            "status": "added",
            "value": "vops"
          }
        }
      }
    }
  },
  "group1": {
    "status": "nested",
    "children": {
      "baz": {
        "status": "changed",
        "old_value": "bas",
        "new_value": "bars"
      },
      "foo": {
        "status": "unchanged",
        "value": "bar"
      },
      "nest": {
        "status": "changed",
        "old_value": {
          "key": "value"
        },
        "new_value": "str"
      }
    }
  },
  "group2": {
    "status": "removed",
    "value": {
      "abc": 12345,
      "deep": {
        "id": 45
      }
    }
  },
  "group3": {
    "status": "added",
    "value": {
      "deep": {
        "id": {
          "number": 45
        }
      },
      "fee": 100500
    }
  }
}"""
    result = generate_diff(file1, file2, 'json')
    assert result == expected
