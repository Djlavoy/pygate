import glo
import subprocess

# Git Function
def git():
    glo.output_b("Checking for updates")
    subprocess.call("git pull",shell=True)
    glo.output_b("Pushing to GitHub")
    commit = raw_input("Commit: ")
    subprocess.call("git add .",shell=True)
    subprocess.call("git commit -m "+"'"+commit+"'",shell=True)
    subprocess.call("git push",shell=True)
    glo.output_b("Complete")
