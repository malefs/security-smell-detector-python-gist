from parso import parse

file = open('app.py')
code = ''
for line in file:
    code = code + line

parser = parse(code)
parser = parser.get_root_node()

def dfs(tree):
    if type(tree) == 'parso.python.tree.PythonLeaf':
        print(tree)
        return


    for node in tree.children:
        print(type(node))

        if len(node.children) > 0:
            dfs(node)

dfs(parser)