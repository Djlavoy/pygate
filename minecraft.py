import subprocess
import lob
import mc_function

subprocess.call("figlet Minecraft Manager",shell=True)
ans=True
while ans:
    ans = raw_input("[Minecraft]~> ")
    if ans == "installer":
            mc_function.installer()
    elif ans == "exit":
        break
    else:
        lob.output_r("invaild!")
