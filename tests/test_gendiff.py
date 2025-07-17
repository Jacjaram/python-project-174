from gendiff.scripts.gendiff import generate_diff


def test_generate_diff():
    expected = '''{
  - follow: false
    host: "hexlet.io"
  - proxy: "123.234.53.22"
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''
    result = generate_diff('test_file1.json', 'test_file2.json')
    assert result == expected

def test_equal():
    result = generate_diff('test_file1.json', 'test_file1 copy.json')
    assert result == '{}'
    
# def test_emptys_files_generate_diff():
#     expected = '''{
# }'''
#     result = generate_diff('', '')
#     assert result == expected