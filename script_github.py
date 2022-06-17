# Include standard modules
import getopt, sys
import subprocess



def github():

    def current_branch():
        command = "git name-rev --name-only HEAD"
        return subprocess.getoutput(command);
# Get full command-line arguments
    full_cmd_arguments = sys.argv

# Keep all but the first
    command = "git {command1} origin"
    argument_list = full_cmd_arguments[1:]
    short_options = "ha:b"
    long_options = ["action", "branch" , "help"]
    try:
        arguments, values = getopt.getopt(argument_list, short_options, long_options)
        for arg, value in arguments:
            if arg in ("-a", "--action"):
                 command =  command.replace("{command1}", value)
            elif arg in ("-h", "--help"):
                 print ("Displaying help")
            elif arg in ("-b", "--branch"):
                if(value !=  ""):
                    command+=" "+value
                else:
                    command+=" "+current_branch()

        print(command)
        subprocess.run(command, shell=True, check=True)
    except getopt.error as err:
    # Output error, and return with an error code
         print (str(err))
         sys.exit(2)




if __name__ == "__main__":
    github()
                
