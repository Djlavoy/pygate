import subprocess
from core import lob
import mc_function

subprocess.call("figlet Minecraft Manager",shell=True)
ans=True
while ans:
    ans = raw_input("[Minecraft]~> ")
    if ans == "installer":
            mc_function.installer()
    elif ans == "help":
        lob.output_y("installer : Opens Installer Manager")
        lob.output_y("exit : exits Minecraft Manager")
    elif ans == "exit":
        break
    elif ans == "..":
        break
    else:
        lob.output_r("invaild!")
