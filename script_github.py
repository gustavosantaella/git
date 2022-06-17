# Include standard modules
import getopt, sys
import subprocess
from pygit2 import Repository

repo = Repository('./.');

def git():
    head = head = repo.lookup_reference('HEAD').resolve()
    print(head.name)



if __name__ == "__main__":
    git()                
