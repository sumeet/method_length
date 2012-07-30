import ast
from collections import namedtuple
import sys


def find_method_lengths(code):
    tree = ast.parse(code)
    return [Method(node.name, length(node)) for node in ast.walk(tree) if
            isinstance(node, ast.FunctionDef)]


def length(node):
    return last_line(node) - node.lineno - docstring_length(node)


def docstring_length(node):
    docstring = ast.get_docstring(node, clean=False)
    return 0 if docstring is None else docstring.count('\n') + 1


def last_line(node):
    children = ast.iter_child_nodes(node)
    child_lines = map(last_line, children)
    return max([get_line_no(node)] + child_lines)


def get_line_no(node):
    return getattr(node, 'lineno', float('-inf'))


Method = namedtuple('Method', 'name lines')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'usage: %s filename.py' % sys.argv[0]
        quit(1)

    filename = sys.argv[1]
    code = open(filename).read()
    methods = find_method_lengths(code)
    for method in methods:
        print '%s\t%s (%s)' % (method.lines, method.name, filename)
