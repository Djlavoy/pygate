import subprocess
import redis
from core import lob

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
            lob.output_y("set pxe : set pxe network ")
            lob.output_y("set ip start : set pxe ip start range")
            lob.output_y("set ip end : set pxe ip end range")
            lob.output_y("set netmask : set pxe netmask")
            lob.output_y("set gateway : set pxe gateway")
            lob.output_y("set ntp : set ntp ip address")
            lob.output_y("show config : show network")
            lob.output_y("exit : exits focal manager")
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
        elif ans == "exit":
            break
        elif ans == "..":
            break
        else:
            lob.output_r("invalid!")

###################
# Set PXE Network #
###################


def set_ip_start():
    ip_s = raw_input("IP Start Range: ")
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




