import subprocess
from core import output
from core import function
from focal import focal_function

subprocess.call("figlet PyGate", shell=True)

ans = True
output.r("PyGate Main Menu")

while ans:
    ans = raw_input("[PyGate]~> ")
    if ans == "help":
        output.r("focal : Loads Focal Manager")
        output.r("git commit : commits to github ")
        output.r("exit : exits pygate")
    elif ans == "focal":
        output.y("Loading Focal Manager")
        focal_function.main_menu()
    elif ans == "clear":
        subprocess.call("clear")
    elif ans == "git commit":
        function.gitcommit()
    elif ans == "exit":
        subprocess.call("pyclean .", shell=True)
        break
    elif ans == "..":
        subprocess.call("pyclean .", shell=True)
        break
    else:
        output.y("Not Valid Choice Try again or run help")


