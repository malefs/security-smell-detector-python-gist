import time, os, subprocess, shutil

# count = 1
# for dirName, subdirList, fileList in os.walk('/home/brokenquark/Workspace/ICSME19/gist-hash'):
#     print(dirName)
#     for fileName in fileList:
#         file = open(f'{dirName}/{fileName}', 'r')
#         dump = open('dump.txt', 'a')
#         dump.write(f'---{dirName}/{fileName}---\n')
#         dump.write(f'---INDEX: {count}---\n')
#         dump.write(f'==================START==================\n')
#         for line in file:
#             dump.write(f'{line}')
#         dump.write(f'\n==================END==================\n')
#         dump.write('DECISION:\n\n\n')
#         dump.close()
#         file.close()
#         count += 1
#
#

count = 1
for dirName, subdirList, fileList in os.walk('/home/brokenquark/Workspace/ICSME19/gist-hash'):
    for fileName in fileList:
        file = open(f'{dirName}/{fileName}', 'r')
        hash = dirName.split("/")[6]
        file2 = open(f'/home/brokenquark/Workspace/ICSME19/gist-src/{hash}.py', 'w')
        for line in file:
            file2.write(f'{line}')
        file.close()
        file2.close()
        count += 1


