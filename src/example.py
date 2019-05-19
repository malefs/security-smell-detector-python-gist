import ast, socket, re, sys, argparse
from pprint import pprint
from urllib.parse import urlparse


def foo():
    return 'foo'


def bar(input):
    return True

x = foo()
y = argparse.ArgumentParser()
z = 'hhh'
DEBUG = True

data = bar(sys.argv[0])

pattern = '[a-z]'
re.match(pattern, z)
re.compile(pattern)
re.search(pattern, z)

password = 'fff'

connection = 'http://www.google.com'
ddd ='http://releases.ubuntu.com/18.04.2/ubuntu-18.04.2-desktop-amd64.iso'


bar(x)

def main():
    with open("example.py", "r") as source:
        tree = ast.parse(source.read())

    analyzer = Analyzer()
    analyzer.visit(tree)

    hardcodedSecretWords = ['key','id', 'cert', 'root','passno','pass-no', 'pass_no', 'auth_token', 'authetication_token','auth-token', 'authentication-token', 'user', 'uname', 'username', 'user-name', 'user_name', 'owner-name', 'owner_name', 'owner', 'admin', 'login', 'pass', 'pwd', 'password', 'passwd', 'secret', 'uuid', 'crypt', 'certificate', 'userid', 'loginid', 'token', 'ssh_key', 'md5', 'rsa', 'ssl_content', 'ca_content', 'ssl-content', 'ca-content', 'ssh_key_content', 'ssh-key-content', 'ssh_key_public', 'ssh-key-public', 'ssh_key_private', 'ssh-key-private', 'ssh_key_public_content', 'ssh_key_private_content', 'ssh-key-public-content', 'ssh-key-private-content']
    hardcodedPasswords = ['pass', 'pwd', 'password', 'passwd', 'passno', 'pass-no', 'pass_no']
    for var in analyzer.vars:
        for item in hardcodedSecretWords:
            if re.match(r'[_A-Za-z0-9-]*{text}\b'.format(text=str(item).lower()), str(var.id).lower().strip()):
                if any(x.lineno == var.lineno for x in analyzer.strings):
                    print('match secret')

    for var in analyzer.vars:
        for item in hardcodedPasswords:
            if re.match(r'[_A-Za-z0-9-]*{text}\b'.format(text=str(item).lower()), str(var.id).lower().strip()):
                if any(x.lineno == var.lineno and x.s == '' for x in analyzer.strings):
                    print('match empty pass')

    for var in analyzer.vars:
        if var.id == 'DEBUG' or var.id == 'DEBUG_PROPAGATE_EXCEPTIONS':
            if any(x.lineno == var.lineno and x.s == 'True' for x in analyzer.strings):
                print('debug')

    for value in analyzer.strings:
        download = ['iso', 'tar', 'tar.gz', 'tar.bzip2', 'zip', 'rar', 'gzip', 'gzip2', 'deb', 'rpm', 'sh', 'run', 'bin', 'exe', 'zip', 'rar', '7zip', 'msi', 'bat']
        parsedUrl = urlparse(str(value.s))
        if re.match(
                r'^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([_\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$',
                str(value.s)):
            if ('http' in str(value.s).strip().lower() or 'www' in str(
                    value.s).strip().lower()) and 'https' not in str(value.s).strip().lower():
                print('http match')
            for item in download:
                if re.match(r'(http|https|www)[_\-a-zA-Z0-9:\/.]*{text}$'.format(text=item), str(value.s)):
                    if 'hashlib' not in analyzer.imports and 'pygpgme' not in analyzer.imports:
                        print('noic')
        elif parsedUrl.scheme == 'http' or parsedUrl.scheme == 'https':
            if parsedUrl.scheme == 'http':
                print('http match')
            for item in download:
                if re.match(r'(http|https|www)[_\-a-zA-Z0-9:\/.]*{text}$'.format(text=item), str(value.s)):
                    if 'hashlib' not in analyzer.imports and 'pygpgme' not in analyzer.imports:
                        print('noic')

    for item in analyzer.subscripts:
        if isinstance(item.value, ast.Attribute):
            if item.value.attr == 'argv':
                print('shell')

    for item in analyzer.calls:
        if isinstance(item.func, ast.Attribute):
            if item.func.attr == 'ArgumentParser' and item.func.value.id == 'argparse':
                print('shell')

    for item in analyzer.calls:
        if isinstance(item.func, ast.Attribute):
            if (item.func.attr == 'match' or item.func.attr == 'search' or item.func.attr == 'compile'):
                if isinstance(item.func.value, ast.Name):
                    if item.func.value.id == 're':
                        print('regex')

    # for node in ast.walk(tree):
    #     if isinstance(node, ast.Str):
    #         print(node)
    #         x = 0
    #
    #     if isinstance(node, ast.Name):
    #         print(node)
    #         x = 0
    #
    #     if isinstance(node, ast.Call):
    #         print(node)
    #         x = 0
    #     if isinstance(node, ast.Assign):
    #         print(node)
    #         x = 0
    x = 0

class Analyzer(ast.NodeVisitor):
    def __init__(self):
        self.imports = []
        self.vars = []
        self.strings = []
        self.subscripts = []
        self.calls = []

    def visit_Import(self, node):
        for alias in node.names:
            self.imports.append(alias.name)
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        for alias in node.names:
            self.imports.append(alias.name)
        self.generic_visit(node)

    def visit_Name(self, node):
        self.vars.append(node)
        self.generic_visit(node)

    def visit_Str(self, node):
        self.strings.append(node)
        self.generic_visit(node)

    def visit_Subscript(self, node):
        self.subscripts.append(node)
        self.generic_visit(node)

    def visit_Call(self, node):
        self.calls.append(node)
        self.generic_visit(node)
if __name__ == "__main__":
    main()

