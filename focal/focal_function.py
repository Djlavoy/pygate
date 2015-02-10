import time
import subprocess
import redis
from netaddr import *
from core import output

###############
# Global Vars #
###############
redis_ip = "localhost"
r = redis.StrictRedis(host='{}'.format(redis_ip), port=6379, db=0)

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
            output.y("set pxe : set pxe network ")
            output.y("set ip start : set pxe ip start range")
            output.y("set ip end : set pxe ip end range")
            output.y("set netmask : set pxe netmask")
            output.y("set gateway : set pxe gateway")
            output.y("set ntp : set ntp ip address")
            output.y("show config : show network")
            output.y("exit : exits focal manager")
        elif ans == "set pxe":
            set_ip_start()
            set_ip_end()
            set_nm()
            set_gw()
            set_ntp()
        elif ans == "set ip start":
            set_ip_start()
        elif ans == "set ip end":
            set_ip_end()
        elif ans == "set netmask":
            set_nm()
        elif ans == "set gateway":
            set_gw()
        elif ans == "set ntp":
            set_ntp
        elif ans == "show config":
            focal_show()
        elif ans == "status":
            status()
        elif ans == "exit":
            break
        elif ans == "..":
            break
        else:
            output.y("invalid!")

###################
# Set PXE Network #
###################


def set_ip_start():
    ask_ip_s = raw_input("IP Start Range: ")
    r.set('tools_ip_s', ip_s)


def set_ip_end():
    ip_e = raw_input("IP End Range: ")
    r.set('tools_ip_e', ip_e)


def set_nm():
    nm = raw_input("Netmask: ")
    r.set('tools_nm', nm)


def set_gw():
    gw = raw_input("Gateway: ")
    r.set('tools_gw', gw)


def set_ntp():
    ntp = raw_input("Ntp Server: ")
    r.set('tools_ntp', ntp)


############################
# Shows PXE boot prameters #
############################


def focal_show():

    output.y("IP Start Range")
    print(r.get('tools_ip_s'))

    output.y("IP End Range")
    print(r.get('tools_ip_e'))

    output.y("Netmask")
    print(r.get('tools_nm'))

    output.y("Gateway")
    print(r.get('tools_gw'))

    output.y("Ntp")
    print(r.get('tools_ntp'))


##########
# Status #
##########


def status():
    try:
        ask = int(raw_input("Set Interval in Seconds [Default 5]: ") or "5")
    except ValueError:
        print("Oops! That was no valid number. Try again ....")
    else:
        try:
            while True:
                print(focal_show())
                if ask == "5":
                    time.sleep(ask)
                else:
                    time.sleep(ask)
                    subprocess.call("clear", shell=True)
        except KeyboardInterrupt:
            print("\nExiting...\n")
