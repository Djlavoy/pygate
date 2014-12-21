import subprocess
import os
import shutil
import sys
import config

# Path which the servers will be installed in
helplocation = config.h['gmod']

ans = True
config.output_y("Garrysmod Installer")
while ans:
    ans = raw_input("[Gmod Installer]~> ")
    if ans == "install":
        with open("{}".format(helplocation), "r") as help:
            shutil.copyfileobj(help, sys.stdout)
    elif ans == "install dep":
        config.output_b("Installing dep for gmod server ")
    elif ans == "install latest":
        gmod_version = config.v['gmod']
        gmod_download = config.d['gmod']
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
    c = config.p['gmod_path']+server
    os.makedirs(c)

    config.output_b("Opening Gmod Ports")
    subprocess.call("ufw allow 27015", shell=True)

    config.output_b("Creating Directory")
    config.output_b("Created Directory {}".format(c))

    config.output_b("Downloading {}".format(gmod_version))
    subprocess.call("wget {}".format(gmod_download), shell=True)

    config.output_b("Checking Gmod Dep.")

    subprocess.call("dpk --add-architecture 1386", shell=True)
    subprocess.call("apt-get update", shell=True)
    subprocess.call("apt-get install ia32-libs", shell=True)

    subprocess.call('mv steamcmd_linux.tar.gz {}'.format(c), shell=True)
    subprocess.call('tar -xvzf {}/steamcmd_linux.tar.gz -C {}'.format(c, c), shell=True)
    subprocess.call('sh {}/steamcmd.sh +login anonymous +quit'.format(c), shell=True)
