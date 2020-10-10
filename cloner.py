import json

#unicode support + 2/3 support
import io

#git downloading via system() 
### YES, IT IS DANGEROUS AND YES, I WILL FIX IT.
import os

#git api querying
from urllib.request import Request, urlopen

def idl(url):
    return urlopen(url).read().decode(urlopen(url).headers.get_content_charset('utf-8'))


def g__clone(g__project_name, g__project_version="latest"):
    g__query = json.loads(idl("https://api.github.com/search/repositories?q="+g__project_name))
    g__result = []
    for i in g__query["items"]:
        g__result.append(i["full_name"]+"\n")
    print("Choose a repo you want to download:\n")
    for i in range(len(g__result)):
        print(str(i)+":"+" "+g__result[i])
    g__select = input("repo author number>")
    os.system("cd git/bin && git.exe clone https://github.com/"+g__result[int(g__select)]+".git")
    os.system("cd git/bin && move "+g__project_name+" ../.. && cd ../..")
