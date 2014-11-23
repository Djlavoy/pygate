import subprocess

# Path which the servers will be installed in
path = "/root/"
mc_manager_help = open("/root/pygate/config/mc_manager_help.txt", 'r')

# Minecraft Manager Loop
ans=True
print("Minecraft Manager")
while ans:
    ans = raw_input("[Minecraft]~> ")
    if ans == "installer":
        import minecraft_installer
    elif ans == "start start":
        server = raw_input("Which server will you like start: ")
        # Starts inputed Minecraft server 
        print 'Starting {} server'.format(server)
    elif ans == "stop server":
        server = raw_input("which server will you like to stop: ")
        # Stop inputed Minecraft Server
        print 'Stoping {} server'.format(server)
    elif ans == "help":
        for line in mc_manager_help:
            print line,
    elif ans == "exit":
        break
    else: 
        print("\n Not A valid Selection")

