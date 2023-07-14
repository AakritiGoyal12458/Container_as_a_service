#!/usr/bin/python3

import subprocess
import cgi

print("Content type:text/hmtl")
print()

form=cgi.FieldStorage()

container_number= form.getvalue("stop_id")

output=output.split("\n")int[container_number] 
container_id = output.split()[0] #0 is container id

cmd = " docker stop" + container_id
output=subprocess.getoutput("sudo " + cmd)

print( output )	