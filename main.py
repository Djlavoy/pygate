import subprocess
import lob
import function

subprocess.call("figlet PyGate",shell=True)

ans = True
lob.output_r("PyGate Main Menu")

while ans:
    ans = raw_input("[PyGate]~> ")

    # ----- Game Menus ------
    if ans == "minecraft":
        lob.output_y("Loading Minecraft Manager")
        import minecraft
    elif ans == "starmade":
        lob.output_y("Loading Starmade Manager")
    elif ans == "gmod":
        lob.output_y("Loading Gmod Manager")
    # ------ Systems Tools -----
    elif ans == "openstack":
        lob.output_y("Loading Openstack Manager")
    elif ans == "clear":
        subprocess.call("clear")
    elif ans == "git":
        function.git()
    elif ans == "exit":
        break
    else:
        lob.output_r("Not Valid Choice Try again or run help")


