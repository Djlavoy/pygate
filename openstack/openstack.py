import subprocess
from core import lob
import os_function

subprocess.call("figlet Openstack Manager", shell=True)

ans = True
while ans:
    ans = raw_input("[Openstack]~> ")
    if ans == "help":
        lob.output_y("mysql : Loads Mysql Manager")
    elif ans == "mysql":
        lob.output_y("Loading Mysql Manager")
        os_function.mysql
    elif ans == "exit":
        break
    elif ans == "..":
        break
    else:
        lob.output_r("Not A Valid Selection")
