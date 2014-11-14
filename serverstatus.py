__author__ = 'davidlavoy'
import subprocess

print("\n===")
subprocess.call("w")
print("\n===")
subprocess.call("ufw status",shell=True)
print("\n===")
subprocess.call("echo --Ipv4-- && curl ipv4.icanhazip.com",shell=True)
subprocess.call("echo --Ipv6-- && curl icanhazip.com",shell=True)
print("\n===")
subprocess.call("free -m",shell=True)
print("\n===")
subprocess.call("df -h",shell=True)
print("\n===")
subprocess.call("df -i",shell=True)
print("\n===")
subprocess.call("date")
