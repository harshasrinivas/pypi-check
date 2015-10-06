# encoding=utf8
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals
from future.standard_library import install_aliases
install_aliases()
import sys
import pypilist
import blessings
t = blessings.Terminal()

def main():
    check = sys.argv[1]
    data = pypilist.list()
    for i in data :
        if i == check :
            print(t.red("✘"), t.cyan("Sorry!"), t.red(check), "is registered already.")
            exit()
    print(t.green("✓"),t.green(check),"is available!")
