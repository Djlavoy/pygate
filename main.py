import subprocess
ans=True
print("PYGate Main Menu")
while ans:
    ans = raw_input("[PyGate]~> ")
    if ans == "minecraft":
        print("\nLoading Minecraft Settings")
        import minecraft
    elif ans == "starmade":
        print("\n Loading Starmade Settings")
        import starmade
    elif ans == "ss":
        import serverstatus
    elif ans == "ping":
        subprocess.call("ping -c 5 google.com",shell=True)
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
        Print("\n Complete")
    elif ans == "exit":
        print("\n Goodbye")
        ans = None
    elif ans == "help":
        print("""
    "===PYGATE Help==="
    "minecraft" : Loads Minecraft settings
    "starmade" : Loads Starmade settings
    "ss" : check server load
    "git" : will push changes to github
    "clear" : clear screen
    "ping" : pings google.com
    "exit" : Exit/Quit
    "================"
    """)
    else:
       print("\n Not Valid Choice Try again or run help")

