from termcolor import colored

# Version Release
rv = {'version': '0.0.2'}

# Help menus Directorys
h = {'main' : "/root/pygate/config/help/main_menu_help.txt",
     'minecraft' : "/root/pygate/config/help/mc_manager_help.txt",
     'minecraft_installer' : "/root/pygate/config/help/mc_installer_help.txt",
     'minecraft_installer_a' : "/root/pygate/config/help/mc_installer_available.txt",
     'gmod_installer' : "root/pygate/config/help/gmod_installer_help.txt",
     'gmod' : "root/pygate/config/help/gmod_manager_help.txt"
    }
# Install Path for  Servers
p = {'minecraft_path': '/root/minecraft/',
     'starmade_path': '/root/starmade/',
     'gmod_path' : '/root/gmod/'
    }

#   For Game version
v = {'v1.8': "Offical Minecraft1.8",
      'tek': "Offical Tekkit",
      'gmod' : "Offical Gmod"
    }

#   For Game Download
d = {'v1.8': 'https://s3.amazonaws.com/Minecraft.Download/versions/1.8/minecraft_server.1.8.jar',
      'tek': 'somedownloadlink',
      'gmod' : 'http://media.steampowered.com/client/steamcmd_linux.tar.gz'
    }
# Function that prints all pretty :)
# Prints Output Normal Color 
def output(text):
    print("\n+------| {} |-----+").format(text)

# Prints Output in Red
def output_r(text):
    print colored("\n+-----| {} |-----+", 'red').format(text)

# Prints Output in Blue
def output_b(text):
    print colored("\n+-----| {} |-----+", 'blue').format(text)

# Prints Output in Green
def output_g(text):
    print colored("\n+-----| {} |-----+", 'green').format(text)

# Prints Output in Yellow
def output_y(text):
    print colored("\n+-----| {} |-----+", 'yellow').format(text)

