import subprocess
import shutil
import sys
import config

subprocess.call("figlet Minecraft",shell=True)
# Path which the servers will be installed in
path = "/root/"
helplocation = config.h["minecraft"]

# Minecraft Manager Loop
ans=True
config.output_r("Minecraft Manager")
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
        config.output_r('Stoping {} server'.format(server))
    elif ans == "help":
        with open("{}".format(helplocation)) as help:
            shutil.copyfileobj(help, sys.stdout)
    elif ans == "exit":
        break
    else: 
        config.output_r("Not A valid Selection")

