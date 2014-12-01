import subprocess
import shutil
import sys
import config

# Help location
helplocation = config.h['main']
version = config.rv['version']

subprocess.call("figlet Pygate {}".format(version),shell=True)
ans=True
config.output_r("PYGate Main Menu")
while ans:
    ans = raw_input("[PyGate]~> ")
    # ----- Games Menus ------
    if ans == "minecraft":
        config.output_y ("Loading Minecraft Settings")
        import minecraft

    elif ans == "starmade":
        config.output_y("Loading Starmade Settings")
        import starmade

    elif ans == 'gmod':
        config.output_y("Loading Gmod Settings")
        import gmod
    # ---- Systems Tools -----
    elif ans == "ss":
        import serverstatus

    elif ans == "ping":
        p = raw_input("\nWhat will you like to ping: ")
        config.output_g("Starting Ping")
        subprocess.call("ping -c 5 {}".format(p),shell=True)
        config.output_g("Complete")
         
    elif ans == "clear":
        subprocess.call("clear")
    
    elif ans == "git":
    
        config.output_b("Checking for updates")
        subprocess.call("git pull",shell=True)
        config.output_b("Pushing up Github" )
        commit = raw_input("Commit: ")
        subprocess.call("cd /root/pygate",shell=True)
        subprocess.call("git add .",shell=True)
        subprocess.call("git commit -m "+"'"+commit+"'",shell=True)
        subprocess.call("git push",shell=True)
        config.output_b("Complete")
    
    elif ans == "exit":
        config.output_b("Goodbye")
        ans = None
    
    elif ans == "help":
        with open("{}".format(helplocation), "r") as help:
            shutil.copyfileobj(help, sys.stdout)
    
    else:
       config.output_b("Not Valid Choice Try again or run help")

