import output
import subprocess


def gitcommit():
    output.b("Checking for updates")
    subprocess.call("git pull", shell=True)
    output.b("Pushing upto GitHub")
    commit = raw_input("Commit: ")
    subprocess.call("git add .", shell=True)
    subprocess.call("git commit -m "+"'"+commit+"'", shell=True)
    subprocess.call("git push", shell=True)
    output.b("Complete")
