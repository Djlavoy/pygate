import subprocess
from core import lob
from core import function
from gather import gather_function

subprocess.call("figlet PyGate",shell=True)

ans = True
lob.output_r("PyGate Main Menu")

while ans:
    ans = raw_input("[PyGate]~> ")
    if ans == "help":
        lob.output_r("minecraft : Loads Minecraft Manager")
        lob.output_r("staremade : Loads Starmade Manager")
        lob.output_r("openstack : Loads Openstack Manager")
        lob.output_r("gmod : Loads Garrysmod Manager")
        lob.output_r("git commit : commits to github ")
        lob.output_r("exit : exits pygate")

    # ----- Game Menus ------
    elif ans == "minecraft":
        lob.output_y("Loading Minecraft Manager")
        from minecraft import minecraft
    elif ans == "starmade":
        lob.output_y("Loading Starmade Manager")
    elif ans == "gmod":
        lob.output_y("Loading Gmod Manager")
    # ------ Systems Tools -----
    elif ans == "openstack":
        lob.output_y("Loading Openstack Manager")
        from openstack import openstack
    elif ans == "gather":
        lob.output_y("Loading Gather Manager")
        gather_function.main_menu()
    elif ans == "clear":
        subprocess.call("clear")
    elif ans == "git commit":
        function.gitcommit()
    elif ans == "exit":
        break
    elif ans == "..":
        break
    else:
        lob.output_r("Not Valid Choice Try again or run help")


