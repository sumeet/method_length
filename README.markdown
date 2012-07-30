Prints out method lengths for Python files.

# Examples

## Longest methods in a project
```bash
$ find . -name '*.py' | xargs -n1 python ./method_length.py | sort -nr | head
4    test_finds_method_lengths (./test.py)
3    test_ignores_docstrings (./test.py)
3    last_line (./method_length.py)
3    find_method_lengths (./method_length.py)
2    docstring_length (./method_length.py)
1    length (./method_length.py)
1    get_line_no (./method_length.py)
```

## Average length for a project
```bash
$ alias average='awk '\''{ total += $1; count++ } END { print total/count }'\'
$ find . -name '*.py' | xargs -n1 python ./method_length.py | average
2.42857
```
