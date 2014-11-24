__author__ = 'davidlavoy'
import subprocess
from termcolor import colored


print colored("\n+-----| Users & Load |-----+", 'red')
subprocess.call("w")

print("\n+-----| Firewall Status |-----+")
subprocess.call("ufw status",shell=True)

print("\n+-----| Network Stats |-----+")
subprocess.call("echo --Ipv4-- && curl ipv4.icanhazip.com",shell=True)
subprocess.call("echo --Ipv6-- && curl icanhazip.com",shell=True)
subprocess.call("echo --Netstat -- && netstat -plnt",shell=True)

print("\n+-----| Free Memory |-----+")
subprocess.call("free -m",shell=True)

print("\n+-----| Free Disk Space |-----+")
subprocess.call("df -h",shell=True)

print("\n+-----| Free Inode Space |-----+")
subprocess.call("df -i",shell=True)

print("\n+-----| Date |-----+")
subprocess.call("date")
