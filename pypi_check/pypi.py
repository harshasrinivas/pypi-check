# encoding=utf8
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals
from future.standard_library import install_aliases
install_aliases()
import sys
import blessings
from bs4 import BeautifulSoup
t = blessings.Terminal()
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

def main():
    check = sys.argv[1]
    html = urlopen("https://pypi.python.org/simple/")
    soup = BeautifulSoup(html.read(), "html.parser")
    for link in soup.find_all('a'):
        if link.string == check :
            print(t.red("✘"), t.cyan("Sorry!"), t.red(link.string), "is registered already.")
            exit()
    print(t.green("✓"),t.green(check),"is available!")
