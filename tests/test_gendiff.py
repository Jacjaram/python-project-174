import os
from gendiff.scripts.gendiff import generate_diff


def test_generate_diff():    
    dir_path = os.path.dirname(__file__)
    file1 = os.path.join(dir_path, 'fixtures', 'test_file1.json')
    file2 = os.path.join(dir_path, 'fixtures', 'test_file2.json')
    expected = '''{
  - follow: false
    host: "hexlet.io"
  - proxy: "123.234.53.22"
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''
    result = generate_diff(file1, file2)
    assert result == expected


def test_equal():
    expected = '''{
    follow: false
    host: "hexlet.io"
    proxy: "123.234.53.22"
    timeout: 50
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
  - follow: false
    host: "hexlet.io"
  - proxy: "123.234.53.22"
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''
    result = generate_diff(file1, file2)
    # print(result)
    assert result == expected
    
