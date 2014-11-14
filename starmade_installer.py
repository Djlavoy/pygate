import subprocess
ans=True
print("Starmade Installer")
while ans:
    ans = raw_input("[Starmade Installer]~> ")
    if ans == "offical latest":
        print("\n=====Opening Starmade Port=====")
        subprocess.call("ufw allow 25565",shell=True)
        print("\n=====Creating Directory /root/offical_starmade=====")
        subprocess.call("mkdir /root/offical_starmade",shell=True)
        print("\n=====Downloading Offical Latest Starmade=====")
        subprocess.call("wget https://s3.amazonaws.com/Minecraft.Download/versions/1.8/minecraft_server.1.8.jar",shell=True)
        print("\n=====Creating Startup Script=====")
        subprocess.call("echo 'cd /root/offical_minecraft;java -Xmx1024M -Xms1024M -jar minecraft_server.jar -nogui' > /root/offical_minecraft/start.sh",shell=True)
        subprocess.call("echo eula=true > eula.txt",shell=True)
        print("\n=====Moving files to /root/offical_starmade=====")
        subprocess.call("mv minecraft_server.1.8.jar /root/offical_minecraft/minecraft_server.jar",shell=True)
        subprocess.call("mv start.sh /root/offical_minecraft",shell=True)
        subprocess.call("mv eula.txt /root/offical_minecraft",shell=True)
        print("\n=====Setting Permissons=====")
        subprocess.call("chmod 755 /root/offical_minecraft/start.sh",shell=True)
        print("\n=====Complete=====")
    elif ans == "clear":
        subprocess.call("clear")
    elif ans == "exit":
      print("\n=====Exiting Starmade Manager=====")
      ans = None
    elif ans == "help":
        print("""
    "===Starmade Installer Help==="
    "offical latest" : install latest offical release 
    "clear" : clear screen
    "exit" : Exit/Quit
    "==========================="
    """)
    else:
       print("\n Not Valid Choice Try again or run help")
