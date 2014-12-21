import subprocess
import shutil
import sys
import config

subprocess.call("figlet OpenStack",shell=True)

# Openstack Manager Loop
ans=True
config.output_r("Openstack Manager")

while ans:
    ans = raw_input("[Openstack]~> ")
    if ans == "help":
        config.output_y("mysql : Mysql Manager")
        config.output_y("keystone : Keystone Manager")
        config.output_y("nova : Nova Manager")
        config.output_y("cinder : Cinder Manager")
    elif ans == "mysql":
        import openstack_mysql
    elif ans == "exit":
        break
    elif ans == "..":
        break
    else:
        config.output_r("Not A valid Selection")
