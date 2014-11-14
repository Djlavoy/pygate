import subprocess
ans=True
print("Minecraft Manager")
while ans:
    ans = raw_input("[Minecraft]~> ")
    if ans == "installer":
        import minecraft_installer
    elif ans == "start server":
      print("\nServer is starting")
      subprocess.Popen(["sh","/root/offical_minecraft/start.sh"])
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
      print("\n Exiting Minecraft Manager")
      ans = None
    elif ans == "help":
        print("""
    "===Minecraft Manager Help==="
    "installer" : Starts Minecraft Installer
    "start server" : Starts Minecraft Server
    "stop server" : Stops Minecraft Server
    "restart server" : Restarts Minecraft Server
    "server status" : check server load
    "clear" : clear screen
    "exit" : Exit/Quit
    "==========================="
    """)
    else:
       print("\n Not Valid Choice Try again or run help")
