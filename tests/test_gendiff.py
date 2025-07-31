import os
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
    
