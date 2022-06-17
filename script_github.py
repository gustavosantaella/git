# Include standard modules
import getopt, sys
import subprocess
from pygit2 import Repository
import argparse

repo = Repository('./.');

command = "git {command}"

def get_current_branch():
    head = repo.lookup_reference('HEAD').resolve()
    name = head.name
    split = name.split('/')
    return split.pop()

def clean_branches_array(array):
    new_array = []
    for item in array:
        if(item != ""):
            new_array.append(item)
    return new_array

def get_remote_branches():
    command = "git branch -r"
    string_branches  = subprocess.getoutput(command)
    array_branches_with_empty = string_branches.replace("\n",'').split(' ')
    array_branches = clean_branches_array(array_branches_with_empty)    
    return array_branches 

def get_current_remote():
    current_remote = ""
    current_branch = get_current_branch()
    branches = get_remote_branches()
    for branch in branches:
        if(current_branch in branch):
            return branch.split("/")[0]


current_branch = get_current_branch()
current_remote = get_current_remote()


replace  = lambda string: command.replace("{command}", string)
def git():

    args = sys.argv
    if((len(args) == 1)):
        return print("you haven't any  command")

    arg  = args[1:][0]
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", dest="branch_name", type=str, help="You have to write a branch name")
    parser.add_argument("command", metavar="gc", type=str, nargs='+', help="any command from git")
    parse_args = parser.parse_args()

    try:    
        git_command = ""

        if(arg == "push" or arg == "pull"): 
            git_command = f"{replace(arg)} {current_remote} {current_branch}"
        else:
            git_command = replace(arg)
        
        print(f"Execunting command: {git_command}")
        console = subprocess.run(git_command, shell=True, check=True)
    except Exception as e:
        print(str(e))
    



if __name__ == "__main__":
    git()                
