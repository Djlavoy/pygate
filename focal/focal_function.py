import subprocess
import redis
from core import lob

###############
# Global Vars #
###############
r = redis.StrictRedis(host='localhost', port=6379, db=0)

#############
# Main Menu #
#############


def main_menu():

    #Focal-Seed
    ans = True
    subprocess.call("figlet Focal Manager", shell=True)
    while ans:
        ans = raw_input("[Focal]~> ")
        if ans == "help":
            lob.output_y("config : set network ")
            lob.output_y("view config : view network")
            lob.output_y("exit : exits focal manager")
        elif ans == "config":
            focal_config()
        elif ans == "view config":
            focal_view_config()
        elif ans == "exit":
            break
        elif ans == "..":
            break
        else:
            lob.output_r("invalid!")

################
# Focal config #
################


def focal_config():
    ip_s = raw_input("IP Start Range: ")
    ip_e = raw_input("IP End Range: ")
    nm = raw_input("Netmask: ")
    gw = raw_input("Gateway: ")
    ntp = raw_input("Ntp Server: ")

    r.set('tools_ip_s', ip_s)
    r.set('tools_ip_e', ip_e)
    r.set('tools_nm', nm)
    r.set('tools_gw', gw)
    r.set('tools_ntp', ntp)


def focal_view_config():

    lob.output_y("IP Start Range")
    print(r.get('tools_ip_s'))

    lob.output_y("IP End Range")
    print(r.get('tools_ip_e'))

    lob.output_y("Netmask")
    print(r.get('tools_nm'))

    lob.output_y("Gateway")
    print(r.get('tools_gw'))

    lob.output_y("Ntp")
    print(r.get('tools_ntp'))




