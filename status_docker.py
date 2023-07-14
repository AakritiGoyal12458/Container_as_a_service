#!/usr/bin/python3

import subprocess
import cgi

print("Content type:text/hmtl")
print()

form=cgi.FieldStorage()

container_number= form.getvalue("status")

# container_number is now a string but we need to convert to int 
cmd = " docker ps -a"

output=subprocess.getoutput("sudo " + cmd)
# print( output ) : run and see output diffrence 	

#my intrest is to get only image name,no id ,etc
output=output.split("\n")int[container_number] #header will not print now 

# status_of_container = output.split()[6] : to check if a container is up or not //6th field
status_of_container = output.split()[6]
print( output )	