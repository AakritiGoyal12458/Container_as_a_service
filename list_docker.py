#!/usr/bin/python3

import subprocess
import cgi

print("Content type:text/hmtl")
print()

cmd = " docker ps "

output=subprocess.getoutput("sudo " + cmd)
# print( output ) : run and see output diffrence 	

#my intrest is to get only image name,no id ,etc
# output=output.split("\n")[1:] #header will not print now 

# status_of_container = output.split()[6] : to check if a container is up or not //6th field
# status_of_container = output.split()[6]
print( <pre> + output + </pre> )	

# run python file : ./list_docker.py
