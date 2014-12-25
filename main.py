import subprocess
import glo
import gf

subprocess.call("figlet Pygate",shell=True)
ans = True

glo.output_r("Pygate Main Menu")

while ans:
    ans = raw_input("[Pygate]~> ")

    #Selection Menu

    if ans == "minecraft":
        glo.output_y("Loading Minecraft Manager")

    elif ans == "starmade":
        glo.output_y("Loading Starmade Manager")

    elif ans == "gmod":
        glo.output_y("Loading Gmod Manager")

    elif ans == "openstack":
        glo.output_y("Loading OpenStack Manager")
    #System Tools

    elif ans == "clear":
        subprocess.call("clear")

    # Git EZ push :)
    elif ans == 'git':
        gf.git()

    # Help Menu
    elif ans == "help":
        glo.output_y("Help menu")
    else:
        glo.output_r("Not Valid CHoice Try again or run help")
