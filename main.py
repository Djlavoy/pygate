import subprocess
ans=True
print("PYGate Main Menu")
while ans:
    ans = raw_input("[PyGate]~> ")
    if ans == "mc":
        print("\nLoading Minecraft Settings")
        import minecraft
    elif ans == "sm":
        print("\n Loading Starmade Settings")
        import starmade
    elif ans == "ss":
        import serverstatus
    elif ans == "ping":
        subprocess.call("ping -c 5 google.com",shell=True)
    elif ans == "clear":
        subprocess.call("clear")
    elif ans == "exit":
      print("\n Goodbye")
      ans = None
    elif ans == "help":
        print("""
    "===PYGATE Help==="
    "mc" : Loads Minecraft settings
    "sm" : Loads Starmade settings
    "ss" : check server load
    "clear" : clear screen
    "ping" : pings google.com
    "exit" : Exit/Quit
    "================"
    """)
    else:
       print("\n Not Valid Choice Try again or run help")

