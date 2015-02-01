import subprocess
import os
import re
import uuid
import redis
import psutil
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
        elif ans == "fetch":
            fetch()
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
    mem_bytes = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES')  # e.g. 4015976448
    mem_gib = mem_bytes/(1024.**3)  # e.g. 3.74

    print("{} G".format(mem_gib))

    r.hset(mac, "Ram", mem_gib)


def fetch_cpu():
    lob.output_y("CPU count")
    cpu_count = psutil.cpu_count()
    print(cpu_count)

    r.hset(mac, "CPU", cpu_count)


