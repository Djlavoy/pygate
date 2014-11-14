import subprocess
ans=True
print("Starmade Manager")
while ans:
    ans = raw_input("[Starmade]~> ")
    if ans == "installer":
        import starmade_installer
    elif ans == "start server":
      print("\nServer is starting")
    elif ans == "stop server":
      print("\n Server is stopping")
    elif ans == "restart server":
      print("\n Server is restarting")
    elif ans == "server status":
        import serverstatus
    elif ans == "ping":
        subprocess.call("ping google.com")
    elif ans == "clear":
        subprocess.call("clear")
    elif ans == "exit":
      print("\n Exiting Starmade Manager")
      ans = None
    elif ans == "help":
        print("""
    "===Starmade Manager Help==="
    "installer" : Starts Starmade Installer
    "start server" : Starts Starmade Server
    "stop server" : Stops Starmade Server
    "restart server" : Restarts Starmade Server
    "server status" : check server load
    "clear" : clear screen
    "exit" : Exit/Quit
    "==========================="
    """)
    else:
       print("\n Not Valid Choice Try again or run help")
