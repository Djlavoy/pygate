import subprocess
from core import lob
import openstack_mysql
import openstack_keystone
subprocess.call("figlet Openstack Manager", shell=True)

ans = True
while ans:
    ans = raw_input("[Openstack]~> ")
    if ans == "help":
        lob.output_y("mysql : Loads Mysql Manager")
        lob.output_y("keystone : Loads Keystone Manager")
    elif ans == "mysql":
        lob.output_y("Loading Mysql Manager")
        openstack_mysql.mysqlmanager()
    elif ans == "keystone":
        lob.output_y("Loading Keystone Manager")
        openstack_keystone.keystonemanager()
    elif ans == "exit":
        break
    elif ans == "..":
        break
    else:
        lob.output_r("Not A Valid Selection")
