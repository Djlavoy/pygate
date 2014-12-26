import subprocess
import apt
from core import lob


def keystonemanager():
    ans = True
    lob.output_y("Openstack Keytone Manager")

    while ans:
        ans = raw_input("[Openstack Keystone Manager]~> ")

        if ans == "help":
            lob.output_y("install keystone : install keystone service")
        elif ans == "install keystone":
            keystone_installer()
        elif ans == "exit":
            break
        elif ans == "..":
            break
        else:
            lob.output_r("Invaild Selection!")


def keystone_installer():
    lob.output_r("Attempting to install Keystone Service")
    cache = apt.Cache()
    lob.output_y("Checking if Keystone Service is installed")
    if cache['keystone'].is_installed:
        lob.output_r("Keystone Service is Installed")
    else:
        lob.output_r("Keystone Server is not Installed ")
        lob.output_r("Attempting to install Keystone")
        subprocess.call("apt-get install keystone -y", shell=True)
        lob.output_r("Keystone Install Complete")

    lob.output_r("Checking if Keystone Client is Installed")
    if cache['python-keystoneclient'].is_installed:
        lob.output_r("Keystone Client is Already Installed")
    else:
        lob.output_r("Keystone Client is not installed")
        lob.output_r("Attempting to install Keystone Client")
        subprocess.call("apt-get install pythong-keystoneclient -y")
        lob.output_r("Keystone Client Installed")


