import ast, socket, re, sys, argparse, os, subprocess
from pprint import pprint
from urllib.parse import urlparse

class Analyzer(ast.NodeVisitor):
    def __init__(self):
        self.imports = []
        self.vars = []
        self.strings = []
        self.subscripts = []
        self.calls = []
        self.attrs = []
        self.assign = []

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

    def visit_Attribute(self, node):
        self.attrs.append(node)
        self.generic_visit(node)

    def visit_Assign(self, node):
        self.assign.append(node)
        self.generic_visit(node)

def detectSmell(input):
    dump = open('smell-updatedxxxxxxxxx.csv', 'a')
    try:
        with open(f'/home/brokenquark/Workspace/ICSME19/gist-src/{input}', "r") as source:
            tree = ast.parse(source.read())
    except:
        print(f'failure parsing {input}')
        subprocess.call(f'rm /home/brokenquark/Workspace/ICSME19/gist-src/{input}', shell=True)
        return 1

    analyzer = Analyzer()
    analyzer.visit(tree)

    hardcodedSecretWords = ['key','id', 'cert', 'root','passno','pass-no', 'pass_no', 'auth_token', 'authetication_token','auth-token', 'authentication-token', 'user', 'uname', 'username', 'user-name', 'user_name', 'owner-name', 'owner_name', 'owner', 'admin', 'login', 'pass', 'pwd', 'password', 'passwd', 'secret', 'uuid', 'crypt', 'certificate', 'userid', 'loginid', 'token', 'ssh_key', 'md5', 'rsa', 'ssl_content', 'ca_content', 'ssl-content', 'ca-content', 'ssh_key_content', 'ssh-key-content', 'ssh_key_public', 'ssh-key-public', 'ssh_key_private', 'ssh-key-private', 'ssh_key_public_content', 'ssh_key_private_content', 'ssh-key-public-content', 'ssh-key-private-content']
    hardcodedPasswords = ['pass', 'pwd', 'password', 'passwd', 'passno', 'pass-no', 'pass_no']


    for value in analyzer.strings:
        download = ['iso', 'tar', 'tar.gz', 'tar.bzip2', 'zip', 'rar', 'gzip', 'gzip2', 'deb', 'rpm', 'sh', 'run', 'bin', 'exe', 'zip', 'rar', '7zip', 'msi', 'bat']
        try:
            parsedUrl = urlparse(str(value.s))
        except:
            parsedUrl = ''
        if len(parsedUrl) > 1:
            if re.match(
                    r'^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([_\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$',
                    str(value.s)):
                if ('http' in str(value.s).strip().lower() or 'www' in str(
                        value.s).strip().lower()) and 'https' not in str(value.s).strip().lower():
                    pass
                    # dump.write(f'{input}, use of http without tls, {value.lineno}\n')
                for item in download:
                    if re.match(r'(http|https|www)[_\-a-zA-Z0-9:\/.]*{text}$'.format(text=item), str(value.s)):
                        dump.write(f'{input}, no integrity check\n')
            elif parsedUrl.scheme == 'http' or parsedUrl.scheme == 'https':
                if parsedUrl.scheme == 'http':
                    pass
                    # dump.write(f'{input}, use of http without tls, {value.lineno}\n')
                for item in download:
                    if re.match(r'(http|https|www)[_\-a-zA-Z0-9:\/.]*{text}$'.format(text=item), str(value.s)):
                        dump.write(f'{input}, no integrity check, {value.lineno}\n')


    return 0
count = 0
for dirName, subdirList, fileList in os.walk('/home/brokenquark/Workspace/ICSME19/gist-src'):
    for fileName in fileList:
        count = count + detectSmell(fileName)

print(count)