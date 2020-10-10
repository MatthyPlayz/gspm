import os

def Psitfile(path):
    with open(path) as f:
        d = f.read().split("\n")
        [os.system(i) for i in d]
