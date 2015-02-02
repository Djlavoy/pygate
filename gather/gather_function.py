import subprocess
import os
import re
import uuid
import redis
import psutil
import netifaces
from core import lob

r = redis.StrictRedis(host='localhost', port=6379, db=0)
mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))


def main_menu():
    # Gather main menu

    subprocess.call("figlet Gather Manager", shell=True)
    ans = True
    while ans:
        ans = raw_input("[Gather]~> ")
        if ans == "help":
            lob.output_y("fetch : fetches server info")
            lob.output_y("exit : exits Gather Manager")
            lob.output_y("list macs : Shows all mac address")
            lob.output_y("get info : Get info of specified mac address")
            lob.output_y("checklist : check specifed mac address checklist ")
        elif ans == "fetch":
            fetch()
        elif ans == "list macs":
            print(r.lrange("mac", 0, -1))
        elif ans == "get info":
            get_info()
        elif ans == "checklistt":
            get_checklist()
        elif ans == "exit":
            break
        elif ans == "..":
            break
        else:
            lob.output_y("invalid!")


def fetch():
    fetch_mac()
    #fetch_ilo()
    fetch_ram()
    #fetch_diskspace()
    fetch_cpu()
    fetch_nics()
    fetch_hwclock()
    fetch_date()

def fetch_mac():
    lob.output_y("Mac Address")
    print(mac)

    check = r.lrange("mac", 0, -1)
    if mac in check:
        lob.output_y("Mac Address {} Already Exist!".format(mac))
    else:
        lob.output_y("Pushing Mac Address {} to Redis".format(mac))
        r.rpush('mac', mac)

    r.lrange("mac", 0, -1)
    r.hset(mac, "Mac Address", mac)


def fetch_ram():
    lob.output_y("Ram")
    mem_bytes = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES')
    mem_gib = mem_bytes/(1024.**3)

    print("{} G".format(mem_gib))

    r.hset(mac, "Ram", mem_gib)


def fetch_cpu():
    lob.output_y("CPU count")
    cpu_count = psutil.cpu_count()
    print(cpu_count)

    r.hset(mac, "CPU", cpu_count)


def fetch_nics():
    lob.output_y("Interfaces")
    interfaces = netifaces.interfaces()
    print(interfaces)
    r.hset(mac, "interfaces", interfaces)


def fetch_hwclock():
    lob.output_y("Hwclock")
    hwclock = subprocess.call("hwclock", shell=True)
    print(hwclock)
    r.hset(mac, "Hwclock", hwclock)


def fetch_date():
    lob.output_y("Date")
    date = subprocess.call("date", shell=True)
    print(date)
    r.hset(mac, "Date", date)


def get_info():
    ask = raw_input("What is the mac address? ")
    check = r.lrange("mac", 0, -1)
    if ask in check:
        lob.output_y("Ram")
        print(r.hget(ask, "Ram"))
        lob.output_y("CPUs")
        print(r.hget(ask, "CPU"))
        lob.output_y("Mac Address")
        print(mac)
        lob.output_y("Interfaces")
        print(r.hget(ask, "interfaces"))
        lob.output_y("Hwclock")
        print(r.hget(ask, "Hwclock"))
        lob.output_y("Date")
        print(r.hget(ask, "Date"))
    else:
        lob.output_r("Mac address not found")


def get_checklist():
    ask = raw_input("What is the mac address")
    check = r.lrange("mac", 0, -1)

    if ask in check:
        lob.output_y("Checking System")
        #check_something
        #check_something2
        #check_something3
    else:
        lob.output_r("Mac Address not found")








