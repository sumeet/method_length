import unittest

from expecter import expect

from method_length import Method, find_method_lengths


code = """\
def short_method(my_arg): pass

def another_short_method(my_arg):
    line_1

class MyClass:
    def longest_method(self):
        line_1
        line_2
        line_3
        line_4
"""


code_with_docstring = '''\
def method_with_multi_line_docstring(arguments):
    """Multi-line docstring.

    Multi-line docstring.
    """
    line_1

def method_with_one_line_docstring():
    """One line docstring."""
    line_1
'''


class MeasuresMethodLengthsTest(unittest.TestCase):

    def test_finds_method_lengths(self):
        expect(find_method_lengths(code)) == [
            Method('short_method', 0),
            Method('another_short_method', 1),
            Method('longest_method', 4)]

    def test_ignores_docstrings(self):
        expect(find_method_lengths(code_with_docstring)) == [
            Method('method_with_multi_line_docstring', 1),
            Method('method_with_one_line_docstring', 1)]


if __name__ == '__main__':
    unittest.main()
