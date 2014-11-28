import subprocess
import os
import shutil
import sys
import config



# Path which the servers will be installed in
helplocation = config.h['minecraft_installer']
installeravailable = config.h['minecraft_installer_a']

ans = True
config.output_y("Minecraft Installer")
while ans:
    ans = raw_input("[Minecraft Installer]~> ")
    if ans == "install":
        with open("{}".format(installeravailable), "r") as help:
            shutil.copyfileobj(help, sys.stdout)
    elif ans == "install 1.8":
        m_v = config.v['v1.8']
        m_d = config.d['v1.8']
        break
    elif ans == "install tekkit":
        m_d = config.v['tek']
        m_d = config.d['tek']
        break
    elif ans == 'help':
        with open("{}".format(helplocation), "r") as help:
            shutil.copyfileobj(help, sys.stdout)
    else:
        config.output_r("Not A valid Selection")


# Install Script
server = raw_input("Server Name: ")
if os.path.exists(server):
    config.output_b("Server {} Already Exist".format(server))
    pass
else:
    ram = raw_input("Ram: ")
    c = path+server
    os.makedirs(c)

    config.output_b("Opening Minecraft Port")
    subprocess.call("ufw allow 25565", shell=True)

    config.output_b("Creating Directory")
    config.output_b("Created Directory {}".format(c))

    config.output_b("Downloading {}".format(m_v))
    #if os.path.exists
    subprocess.call("wget {}".format(m_d), shell=True)

    config.output_b("Creating Startup Script")
    subprocess.call("echo 'cd {}; java -Xmx{}M -Xms{}M -jar minecraft_server -nogui' > {}/start.sh".format(c, ram, ram, c), shell=True)
    subprocess.call("echo eula=true > eula.txt", shell=True)

    config.output_b("Moving files to {}".format(server))
    subprocess.call("mv minecraft_server.1.8.jar {}/minecraft_server.jar".format(c), shell=True)
    subprocess.call("mv eula.txt {}".format(c), shell=True)

    config.output_b("Setting Permissons for {}".format(c))

    config.output_b("Before")
    subprocess.call("ls -la {}".format(c), shell=True)
    subprocess.call("chmod 755 {}/start.sh".format(c), shell=True)

    config.output_b("After")
    subprocess.call("ls -la {}".format(c), shell=True)

    config.output_b("Complete")
    config.output_b("The server is now installed in {}".format(c))
