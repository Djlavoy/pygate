import subprocess
import os 
ans=True
print("Minecraft Manager")
while ans:
    ans = raw_input("[Minecraft]~> ")
    if ans == "install":
        print("\n=====Version that can be installed=====")
        print("\nexample: install 1.8")
        print("\n1.8 : will install Offical Version 1.8 Minecraft")
        print("\ntekkit : will install Offical Latest Tekkit Minecraft")
        print("\n=====")
    elif ans == "install 1.8":
        server = "/root/"+raw_input("Server Name: ")
        if os.path.exists(server):
            print("Server "+server+" Already Exist")
            pass
        else:
            os.mkdir(server) 
            ram = raw_input("Ram: ")
            print("\n=====Opening Minecraft Port=====")
            subprocess.call("ufw allow 25565",shell=True)
            print("\n=====Creating Directory "+server+"=====")
            print("\n=====Downloading Offical Latest Minecraft 1.8=====")
            subprocess.call("wget https://s3.amazonaws.com/Minecraft.Download/versions/1.8/minecraft_server.1.8.jar",shell=True)
            print("\n=====Creating Startup Script=====")
            subprocess.call("echo 'cd "+server+";java ""-Xmx"+ram+"M -Xms"+ram+"M -jar minecraft_server.jar -nogui' > "+server+"/start.sh",shell=True)
            subprocess.call("echo eula=true > eula.txt",shell=True)
            print("\n=====Moving files to "+server+"=====")
            subprocess.call("mv minecraft_server.1.8.jar "+server+"/minecraft_server.jar",shell=True)
            subprocess.call("mv eula.txt "+server,shell=True)
            print("\n=====Setting Permissons=====")
            print("\n=====Before=====")
            subprocess.call("ls -la "+server,shell=True)
            subprocess.call("chmod 755 "+server+"/start.sh",shell=True)
            print("\n=====After=====")
            subprocess.call("ls -la "+server,shell=True)
    elif ans == "install tekkit":
        print("need to config the server ")
    elif ans == "start server":
      server = raw_input("Server Name: ")
      print("\nStarting")
      subprocess.Popen("sh /root/"+server+"/start.sh",shell=True)
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
    "install" : Will install given minecraft version
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
