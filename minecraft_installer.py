import subprocess
import os 
import urllib

# Path which the servers will be installed in
path = "/root/"

ans=True
print("Minecraft Installer")
while ans:
    ans = raw_input("[Minecraft Installer]~> ")
    if ans == "install":
        print("\n=====Version that can be installed=====")
        print("\nexample: install 1.8")
        print("\n1.8 : will install Offical Version 1.8 Minecraft")
        print("\ntekkit : will install Offical Latest Tekkit Minecraft")
        print("\n=====")
    elif ans == "install 1.8":
        minecraft_version = "Offical Minecraft 1.8"
        minecraft_download = 'https://s3.amazonaws.com/Minecraft.Download/versions/1.8/minecraft_server.1.8.jar'        
        break 
    elif ans == "install tekkit":
        minecraft_version = "Offical tekkit"
        minecraft_download = "tekkit link"
        break
    else: 
        print("\n Not A valid Selection")

server = raw_input("Server Name: ")
if os.path.exists(path+server):
    print("Server "+server+" Already Exist")
    pass
else:
    os.makedirs(path+server);
    ram = raw_input("Ram: ")
    print("\n=====Opening Minecraft Port=====")
    subprocess.call("ufw allow 25565",shell=True)
    print("\n=====Creating Directory "+path+server+"=====")
    print("\n=====Downloading "+minecraft_version+"=====")
    subprocess.call("wget "+minecraft_download,shell=True)
    print("\n=====Creating Startup Script=====")
    subprocess.call("echo 'cd "+path+server+";java ""-Xmx"+ram+"M -Xms"+ram+"M -jar minecraft_server.jar -nogui' > "+path+server+"/start.sh",shell=True)
    subprocess.call("echo eula=true > eula.txt",shell=True)
    print("\n=====Moving files to "+path+server+"=====")
    subprocess.call("mv minecraft_server.1.8.jar "+path+server+"/minecraft_server.jar",shell=True)
    subprocess.call("mv eula.txt "+path+server,shell=True)
    print("\n=====Setting Permissons=====")
    print("\n=====Before=====")
    subprocess.call("ls -la "+path+server,shell=True)
    subprocess.call("chmod 755 "+path+server+"/start.sh",shell=True)
    print("\n=====After=====")
