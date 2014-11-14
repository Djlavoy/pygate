import subprocess
ans=True
print("Minecraft Manager")
while ans:
    ans = raw_input("[Minecraft]~> ")
    if ans == "install":
        print("\n=====Version that can be installed=====")
        print("\nexample: install 1.8")
        print("\n1.8: will install Offical Version 1.8 Minecraft")
        print("\n=====")
    elif ans == "install 1.8":
        print("\n=====Opening Minecraft Port=====")
        subprocess.call("ufw allow 25565",shell=True)
        print("\n=====Creating Directory /root/mc_1.8=====")
        subprocess.call("mkdir /root/mc_1.8",shell=True)
        print("\n=====Downloading Offical Latest Minecraft 1.8=====")
        subprocess.call("wget https://s3.amazonaws.com/Minecraft.Download/versions/1.8/minecraft_server.1.8.jar",shell=True)
        print("\n=====Creating Startup Script=====")
        subprocess.call("echo 'cd /root/mc_1.8;java -Xmx1024M -Xms1024M -jar minecraft_server.jar -nogui' > /root/mc_1.8/start.sh",shell=True)
        subprocess.call("echo eula=true > eula.txt",shell=True)
        print("\n=====Moving files to /root/mc_1.8=====")
        subprocess.call("mv minecraft_server.1.8.jar /root/mc_1.8/minecraft_server.jar",shell=True)
        subprocess.call("mv eula.txt /root/mc_1.8",shell=True)
        print("\n=====Setting Permissons=====")
        subprocess.call("chmod 755 /root/mc_1.8/start.sh",shell=True)

    elif ans == "start server":
      print("\nServer is starting")
      subprocess.Popen(["sh","/root/mc_1.8/start.sh"])
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
