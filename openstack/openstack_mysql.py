import subprocess
import apt
import MySQLdb as db
from core import lob
import openstack_config


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
            lob.output_y("show passwords : will show current mysql passwords")
        elif ans == "show passwords":
            mysql_show_passwords()
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
        elif ans == "exit":
            break
        elif ans == "..":
            break
        else:
            lob.output_r("Not A Valid Selection")


def mysql_show_passwords():

    lob.output_r("Keystone Password")
    print(openstack_config.keystone_password)

    lob.output_r("Nova Password")
    print(openstack_config.nova_password)

    lob.output_r("Glance Password")
    print(openstack_config.glance_password)

    lob.output_r("Neutron Password")
    print(openstack_config.neutron_password)

    lob.output_r("Cinder Password")
    print(openstack_config.cinder_password)

    lob.output_r("Heat Password")
    print(openstack_config.heat_password)


def mysql_installer():
    lob.output_r("Attempting to install Mysql Server")
    cache = apt.Cache()
    lob.output_y("Checking if Mysql Server is installed")
    if cache['mysql-server'].is_installed:
        lob.output_y("Mysql Server is installed")
    else:
        lob.output_r("Mysql Server is not installed")
        lob.output_r("Installing Mysql Server")
        subprocess.call("apt-get install mysql-server -y", shell=True)
        lob.output_b("Mysql Server Install Complete")


def install_nova():
    con = db.connect()
    cur = con.cursor()
    #Creating Database Nova
    try:
        cur.execute('CREATE DATABASE nova;')
        lob.output_r("Database Nova Created")
    except db.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
    #Creating User Nova
    try:
        cur.execute("GRANT ALL PRIVILEGES ON nova.* TO 'nova'@'localhost' IDENTIFIED BY '" + openstack_config.nova_password + "';")
        cur.execute("GRANT ALL PRIVILEGES ON nova.* TO 'nova'@'%' IDENTIFIED BY '" + openstack_config.nova_password + "';")
        lob.output_r("User Nova Created")
    except db.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])


def install_keystone():
    con = db.connect()
    cur = con.cursor()

    #Creating Database Keystone
    try:
        cur.execute('CREATE DATABASE keystone;')
        lob.output_r("Database Keystone Created")
    except db.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])

    try:
        cur.execute("GRANT ALL PRIVILEGES ON keystone.* TO 'keystone'@'localhost' IDENTIFIED BY '"+openstack_config.keystone_password+"';")
        cur.execute("GRANT ALL PRIVILEGES ON keystone.* TO 'keystone'@'%' IDENTIFIED BY 'i"+openstack_config.keystone_password+"';")
        lob.output_r("User Keystone Created")
    except db.Error, e:
        print "Errot %d: %s" % (e.args[0], e.args[1])


def install_glance():
    con = db.connect()
    cur = con.cursor()

    #Creating Database GLANCE
    try:
        cur.execute('CREATE DATABASE glance;')
        lob.output_r("Database Glance Created")
    except db.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])

    try:
        cur.execute("GRANT ALL PRIVILEGES ON glance.* TO 'glance'@'localhost' IDENTIFIED BY '"+openstack_config.glance_password+"';")
        cur.execute("GRANT ALL PRIVILEGES ON glance.* TO 'glance'@'%' IDENTIFIED BY '"+openstack_config.glance_password+"';")
        lob.output_r("User Glance Created")
    except db.Error, e:
        print "Errot %d: %s" % (e.args[0], e.args[1])


def install_neutron():
    con = db.connect()
    cur = con.cursor()

    #Creating Database neutron
    try:
        cur.execute('CREATE DATABASE neutron;')
        lob.output_r("Database neutron Created")
    except db.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])

    try:
        cur.execute("GRANT ALL PRIVILEGES ON neutron.* TO 'neutron'@'localhost' IDENTIFIED BY '"+openstack_config.neutron_password+"';")
        cur.execute("GRANT ALL PRIVILEGES ON neutron.* TO 'neutron'@'%' IDENTIFIED BY '"+openstack_config.neutron_password+"';")
        lob.output_r("User neutron Created")
    except db.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])


def install_cinder():
    con = db.connect()
    cur = con.cursor()

    #Creating Database cinder
    try:
        cur.execute('CREATE DATABASE cinder;')
        lob.output_r("Database cinder Created")
    except db.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])

    try:
        cur.execute("GRANT ALL PRIVILEGES ON cinder.* TO 'neutron'@'localhost' IDENTIFIED BY '"+openstack_config.cinder_password+"';")
        cur.execute("GRANT ALL PRIVILEGES ON cinder.* TO 'neutron'@'%' IDENTIFIED BY '"+openstack_config.cinder_password+"';")
        lob.output_r("User Cinder Created")
    except db.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])


def install_heat():
    con = db.connect()
    cur = con.cursor()

    #Creating Database heat
    try:
        cur.execute('CREATE DATABASE heat;')
        lob.output_r("Database heat Created")
    except db.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])

    try:
        cur.execute("GRANT ALL PRIVILEGES ON heat.* TO 'heat'@'localhost' IDENTIFIED BY '"+openstack_config.cinder_password+"';")
        cur.execute("GRANT ALL PRIVILEGES ON heat.* TO 'heat'@'%' IDENTIFIED BY '"+openstack_config.cinder_password+"';")
        lob.output_r("User Heat Created")
    except db.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])



