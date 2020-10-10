from cloner import *
import sys
import os
from manifest import *
try:
    if(sys.argv[1] == "install"):
        try:
            g__clone(sys.argv[2], sys.argv[3])
            os.system("cd git/bin/"+sys.argv[2])
            print(os.listdir())
            Psitfile("git/bin/"+sys.argv[2]+"/"+".Psitfile")
        except:
            g__clone(sys.argv[2], "latest")
            os.chdir("git/bin/"+sys.argv[2]+"/")
            print(os.listdir())
            Psitfile(sys.argv[2]+".Psitfile")
except:
    print(open("help.txt").read())
