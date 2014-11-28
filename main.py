import subprocess
import shutil
import sys
import config

# Help location
helplocation = config.h['main']
version = config.rv['version']

subprocess.call("figlet Pygate {}".format(version),shell=True)
ans=True
print("PYGate Main Menu")
while ans:
    ans = raw_input("[PyGate]~> ")
    if ans == "minecraft":
        config.output_y ("Loading Minecraft Settings")
        print("\n+-----| Loading Minecraft Settings |-----+")
        import minecraft

    elif ans == "starmade":
        config.ouput_r("Loading Starmade Settings")
        print("\n+-----| Loading Starmade Settings |----+")
        import starmade

    elif ans == "ss":
        import serverstatus

    elif ans == "ping":
        p = raw_input("\nWhat will you like to ping: ")
        print("\n +------| Starting |-----+")
        subprocess.call("ping -c 5 {}".format(p),shell=True)
        print("\n +-----| Complete |-----+")
    
    elif ans == "clear":
        subprocess.call("clear")
    
    elif ans == "git":
    
        config.output_b("Checking for updates===")
        subprocess.call("git pull",shell=True)
        config.output_b("Pushing up Github" )
        commit = raw_input("Commit: ")
        subprocess.call("cd /root/pygate",shell=True)
        subprocess.call("git add .",shell=True)
        subprocess.call("git commit -m "+"'"+commit+"'",shell=True)
        subprocess.call("git push",shell=True)
        print("\n ===Complete===")
    
    elif ans == "exit":
        print("\n Goodbye")
        ans = None
    
    elif ans == "help":
        with open("{}".format(helplocation), "r") as help:
            shutil.copyfileobj(help, sys.stdout)
    
    else:
       print("\n Not Valid Choice Try again or run help")

