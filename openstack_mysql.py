import subprocess
import os 
import shutil
import sys 
import config
import MySQLdb as db 
import apt

ans = True 
config.output_y("[Openstack Mysql Manager]")

while ans:
    ans = raw_input("[Openstack Mysql Manager]~> ")
    if ans == "help":
        config.output_y("install mysql : Installs mysql server")
        config.output_y("install full: Install all Openstack users and users ")
        
    elif ans == "install mysql":
        config.output_r("Installing all services and users")
        cache = apt.Cache()   
        config.output_y("Checking if mysql is installed")
        if cache['mysql-server'].is_installed:
            config.output_y("Mysql is installed")
        else:
            config.output_r("Mysql is not installed")
            config.output_b("Installing Mysql")
            subprocess.call("apt-get install mysql-server -y", shell=True)
            config.output_b("Mysql Server Install Complete")
    elif ans == "install all":
        config.output_r("Openstack Databases;")
        con = db.connect()
        cur = con.cursor()
             
       #===Creating Databases===# 
            #Database Keystone
        try:
            cur.execute('CREATE DATABASE keystone;')
            config.output_r("Database Keystone Created")
        except db.Error, e:
            print "Error %d: %s" % (e.args[0],e.args[1])
        
            #Database Glance
        try:
            cur.execute('CREATE DATABASE glance;')
            config.output_r("Database Glance Created")
        except db.Error, e:
            print "Error %d: %s" % (e.args[0],e.args[1])           

            #Database Nova
        try:
            cur.execute('CREATE DATABASE nova;')
            config.output_r("Database Nova Created")
        except db.Error, e:
            print "Error %d: %s" % (e.args[0],e.args[1])

            #Database Neutron
        try:
            cur.execute('CREATE DATABASE neutron;')
            config.output_r("Database Neutron Created")
        except db.Error, e:
            print "Error %d: %s" % (e.args[0],e.args[1])

            #Database Cinder
        try:
            cur.execute('CREATE DATABASE cinder;')
            config.output_r("Database Cinder Created")
        except db.Error, e:
            print "Error %d: %s" % (e.args[0],e.args[1])

            #Database Heat
        try:
            cur.execute("CREATE DATABASE heat")
            config.output_r("Database Heat Created")    
        except db.Error, e:
            print "Error %d: %s" % (e.args[0],e.args[1])
        #===End of Creating Databases===#

        #===Creating Users===#
        config.output_r("OpenStack Users")
        try:
            cur.execute("GRANT ALL PRIVILEGES ON keystone.* TO 'keystone'@'localhost' IDENTIFIED BY '';")      
            cur.execute("GRANT ALL PRIVILEGES ON keystone.* TO 'keystone'@'%' IDENTIFIED BY '';")
            config.output_r("Created And Set Permissons for User Keystone")
        except db.Error, e:
            print "Error %d: %s" % (e.args[0],e.args[1])
            
        finally:
            if con:
                con.close()
    elif ans == "exit":
        break
    elif ans == "..":
        break
    else:
        config.output_r("Not A valid Selection")            

