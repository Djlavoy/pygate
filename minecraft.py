import subprocess
import shutil
import sys
import help


# Path which the servers will be installed in
path = "/root/"
helplocation = help.h["minecraft"]

# Minecraft Manager Loop
ans=True
print("Minecraft Manager")
while ans:
    ans = raw_input("[Minecraft]~> ")
    if ans == "installer":
        import minecraft_installer
    elif ans == "start start":
        server = raw_input("Which server will you like start: ")
        # Starts inputed Minecraft server 
        print 'Starting {} server'.format(server)
    elif ans == "stop server":
        server = raw_input("which server will you like to stop: ")
        # Stop inputed Minecraft Server
        print 'Stoping {} server'.format(server)
    elif ans == "help":
        with open("{}".format(helplocation)) as help:
            shutil.copyfileobj(help, sys.stdout)
    elif ans == "exit":
        break
    else: 
        print("\n Not A valid Selection")

