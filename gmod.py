import subprocess
import shutil
import sys
import config

subprocess.call("figlet Garrys Mod",shell=True)
# Path which the servers will be installed in
helplocation = config.h["gmod"]

# Garrys Mod Manager Loop
ans=True
config.output_r("Gmod Manager")
while ans:
    ans = raw_input("[Gmod]~> ")
    if ans == "installer":
        import gmod_installer
    elif ans == "start start":
        server = raw_input("Which server will you like start: ")
        # Starts inputed Gmod server 
        print 'Starting {} server'.format(server)
    elif ans == "stop server":
        server = raw_input("which server will you like to stop: ")
        # Stop inputed Gmod Server
        config.output_r('Stoping {} server'.format(server))
    elif ans == "help":
        with open("{}".format(helplocation)) as help:
            shutil.copyfileobj(help, sys.stdout)
    elif ans == "exit":
        break
    else: 
        config.output_r("Not A valid Selection")

