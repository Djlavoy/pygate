import subprocess
import os 
import shutil
import sys
import help


# Path which the servers will be installed in
path = "/root/"
helplocation = help.h['minecraft_installer']

# Dic, For Minecraft version
v = {'v1.8': "Offical Minecraft1.8",
     "tek": "Offical Tekkit"
    }
# Dic, For Minecraft Download
d = {'v1.8': 'https://s3.amazonaws.com/Minecraft.Download/versions/1.8/minecraft_server.1.8.jar',
     'tek' : 'somedownloadlink'
    }


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
        m_v = v['v1.8']
        m_d = d['v1.8']        
        break 
    elif ans == "install tekkit":
        m_d = v['tek']
        m_d = d['tek']
        break
    elif ans == 'help':
        with open("{}".format(helplocation), "r") as help:
              shutil.copyfileobj(help, sys.stdout)

    else: 
        print("\n Not A valid Selection")


# Install Script 
server = raw_input("Server Name: ")
if os.path.exists(server):
    print("Server {} Already Exist".format(server))
    pass
else:
    ram = raw_input("Ram: ")
    c = path+server
    os.makedirs(c);

    print("\n=====Opening Minecraft Port=====")
    subprocess.call("ufw allow 25565",shell=True)

    print("\n=====Creating Directory=====")
    print("Created Directory{}".format(c))

    print("\n=====Downloading {}=====".format(m_v))
    subprocess.call("wget {}".format(m_d),shell=True)

    print("\n=====Creating Startup Script=====")
    subprocess.call("echo 'cd {}; java -Xmx{}M -Xms{}M -jar minecraft_server -nogui' > {}/start.sh".format(c,ram,ram,c),shell=True)
    subprocess.call("echo eula=true > eula.txt",shell=True)

    print("\n=====Moving files to "+path+server+"=====")
    subprocess.call("mv minecraft_server.1.8.jar {}/minecraft_server.jar".format(c),shell=True)
    subprocess.call("mv eula.txt {}".format(c),shell=True)

    print("\n=====Setting Permissons for {}=====".format(c))
    
    print("\n=====Before=====")
    subprocess.call("ls -la {}".format(c),shell=True)
    subprocess.call("chmod 755 {}/start.sh".format(c),shell=True)
    
    print("\n=====After=====")
    subprocess.call("ls -la {}".format(c),shell=True)
    
    print("\n=====Complete=====")
    print("The server is now installed in {}".format(c))
