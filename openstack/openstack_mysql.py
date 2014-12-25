import subprocess
import apt
import MySQLdb as db
from core import lob


def mysqlmanager():
    ans = True
    lob.output_y("Openstack Mysql Manager")

    while ans:
        ans = raw_input("[Openstack Mysql Manager]~> ")

        if ans == "help":
            lob.output_y("install mysql : Installs Mysql Server")
            lob.output_y("install full : Installs all Openstack users and Databases")
            lob.output_y("install nova : Installs Nova user and Database")
            lob.output_y("install keystone : Install Keystone user and Database")
            lob.output_y("install glance: Install Glance user and Database")
            lob.output_y("install neutron : Install Neutron user and Database")
            lob.output_y("install cinder : Install Cinder user and Database")
            lob.output_y("install heat : Install Heat user and Database")
        elif ans == "install mysql":
            mysql_installer()
        elif ans == "install full":
            install_nova()
            install_keystone()
            install_glance()
            install_neutron()
            install_cinder()
            install_heat()
        elif ans == "install nova":
            install_nova()
        elif ans == "install keystone":
            install_keystone()
        elif ans == "install glance":
            install_glance()
        elif ans == "install neutron":
            install_neutron()
        elif ans == "install cinder":
            install_cinder()
        elif ans == "install heat":
            install_heat()
        else:
            lob.output_r("Not A Valid Selection")


def mysql_installer():
    lob.output_r("Attempting to install Mysql Server")
    cache = apt.Cache()
    lob.output_y("Checking if Mysql Server is installed")
    if cache['mysql-server'].is_installed:
        lob.output_y("Mysql Server is installed")
    else:
        lob.output_r("Mysql Server is not installed")
        lob.output_r("Installing Mysql Server")
        subprocess.call("apt-get insatll mysql-server -y", shell=True)
        lob.output_b("Mysql Server Install Complete")


def install_nova():


def install_keystone():


def install_glance():


def install_neutron():


def install_cinder():


def install_heat():


