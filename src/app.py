import time, os, subprocess, shutil

count = 1
for dirName, subdirList, fileList in os.walk('/home/brokenquark/Workspace/ICSME19/gists'):
    print(dirName)
    for fileName in fileList:
        file = open(f'{dirName}/{fileName}', 'r')
        dump = open('dump.txt', 'a')
        dump.write(f'---{dirName}/{fileName}---\n')
        dump.write(f'---INDEX: {count}---\n')
        dump.write(f'==================START==================\n')
        for line in file:
            dump.write(f'{line}')
        dump.write(f'==================END==================\n')
        dump.write('DECISION:\n\n\n')
        dump.close()
        file.close()
        count += 1


