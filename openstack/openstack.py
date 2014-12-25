import subprocess
from core import lob
import openstack_mysql
subprocess.call("figlet Openstack Manager", shell=True)

ans = True
while ans:
    ans = raw_input("[Openstack]~> ")
    if ans == "help":
        lob.output_y("mysql : Loads Mysql Manager")
    elif ans == "mysql":
        lob.output_y("Loading Mysql Manager")
        openstack_mysql.mysqlmanager
    elif ans == "exit":
        break
    elif ans == "..":
        break
    else:
        lob.output_r("Not A Valid Selection")
