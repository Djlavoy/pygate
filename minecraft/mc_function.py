import subprocess
import os
from core import lob

installpath = {'minecraft_path': '/root/Minecraft/'}


def main_menu():
    # Minecraft Main Menu

    subprocess.call("figlet Minecraft Manager", shell=True)
    ans = True
    while ans:
        ans = raw_input("[Minecraft]~> ")
        if ans == "help":
            lob.output_y("installer : launch installer")
            lob.output_y("exit : exits Minecraft Manager")
        elif ans == "installer":
            installer()
        elif ans == "exit":
            break
        elif ans == "..":
            break
        else:
            lob.output_r("Invalid Command!")


def installer():
    # Install Script
    V = True
    while V:
        lob.output_y("1.8")
        lob.output_y("Tekkit")
        version = raw_input("What version will you like to install? ")
        if version == "1.8":
            m_v = "Offical Minecraft 1.8"
            m_d = "https://s3.amazonaws.com/Minecraft.Download/versions/1.8/minecraft_server.1.8.jar"
            break
        elif version == "Tekkit":
            m_v = version['Tekkit']
            m_d = version['Tekkit']
            break
        else:
            lob.output_r("Invalid Version")

    server = raw_input("Server Name: ")
    if os.path.exists(server):
        lob.output_b("Server {} Already Exist".format(server))
        pass

    else:
        ram = raw_input("Ram in MB: ")
        path = installpath['minecraft_path']+server
        os.makedirs(c)

        #check if ufw is enabled
        lob.output_b("Checking Ufw Status")
        status = subprocess.check_output(['ufw','status'])

        if "Status: active" in status:
            lob.output_y("Ufw is active")
            lob.output_y("Opening Minecraft Port")
            subprocess.call("ufw allow 25565", shell=True)
        elif "Status: inactive" in status:
            lob.output_y("Ufw is inactive Skipping")
        else:
            lob.output_y("There was a error checking ufw")

        lob.output_b("Creating Directory")
        lob.output_b("Created Directory {}".format(path))

        lob.output_b("Downloading {}".format(m_v))
        # Need to add logic to check for pre downloaded minecraft jar
        subprocess.call("wget {}".format(m_d), shell=True)

        lob.output_b("Creating Startup Script")
        subprocess.call("echo 'java -Xmx{}M -Xms{}M -jar minecraft_server.jar -nogui' > {}/start.sh".format(ram, ram, path), shell=True)
        subprocess.call("echo eula=true > eula.txt", shell=True)

        lob.output_b("Moving files to {}".format(path))
        subprocess.call("mv minecraft_server.1.8.jar {}/minecraft_server.jar".format(path), shell=True)
        subprocess.call("mv eula.txt {}".format(path), shell=True)

        lob.output_b("Setting Permissons for {}".format(path))

        lob.output_b("Before")
        subprocess.call("ls -la {}".format(path), shell=True)
        subprocess.call("chmod 755 {}/start.sh".format(path), shell=True)

        lob.output_b("After")
        subprocess.call("ls -la {}".format(path), shell=True)

        lob.output_b("Complete")
        lob.output_b("The server is now installed in {}".format(path))
