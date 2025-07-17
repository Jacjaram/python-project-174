import os
from gendiff.scripts.gendiff import generate_diff


def test_generate_diff():    
    dir_path = os.path.dirname(__file__)
    file1 = os.path.join(dir_path, 'test_file1.json')
    file2 = os.path.join(dir_path, 'test_file2.json')
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
    dir_path = os.path.dirname(__file__)
    file1 = os.path.join(dir_path, 'test_file1.json')
    file3 = os.path.join(dir_path, 'test_file1 copy.json')
    result = generate_diff(file1, file3)
    assert result == '{}', "Los archivos iguales deberían producir una diferencia vacía"
    
    
# def test_emptys_files_generate_diff():
#     expected = '''{
# }'''
#     result = generate_diff('', '')
#     assert result == expected