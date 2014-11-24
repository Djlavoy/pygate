import subprocess
import shutil
import sys
import help

# Help location
helplocation = help.h['main']


ans=True
print("PYGate Main Menu")
while ans:
    ans = raw_input("[PyGate]~> ")
    if ans == "minecraft":
        print("\n+-----| Loading Minecraft Settings |-----+")
        import minecraft

    elif ans == "starmade":
        print("\n+-----| Loading Starmade Settings |----+")
        import starmade

    elif ans == "ss":
        import serverstatus

    elif ans == "ping":
        p = raw_input("\nWhat will like to ping: ")
        print("\n +------| Starting |-----+")
        subprocess.call("ping -c 5 {}".format(p),shell=True)
        print("\n +-----| Complete |-----+")
    
    elif ans == "clear":
        subprocess.call("clear")
    
    elif ans == "git":
    
        print("\n ===Checking for updates===")
        subprocess.call("git pull",shell=True)
        print("\n ===Pushing up Github===" )
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

