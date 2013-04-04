import re
import os
import sys
import fileinput
# import fnmatch
from subprocess import Popen, PIPE
 
def regex_process(fromfile, tofile, patterns):
    with open(fromfile, "r") as f:
        contents = f.read()
        for pattern, repl in patterns:
            contents = re.sub(pattern, repl, contents)
    with open(tofile, "w") as f:
            f.write(contents)
 
def call_pandoc(fromfile, tofile, fromformat, toformat, options=[]):
    if toformat != "pdf":
        tooptions = ["-t", toformat]
    else:
        tooptions = []
    cmd = ['pandoc', "-f", fromformat] + tooptions + ["-o", \
           tofile, "--id-prefix", \
           "pandoc-"] + options + [fromfile]
    r = Popen(cmd, stdout=PIPE).communicate()

def listfiles():
    files = [file for file in sys.argv[1:]]
    if not files:
        files = [file for file in os.listdir('.') if file.endswith('.md')]
    return files
    
if __name__ == '__main__':
    print listfiles()
    