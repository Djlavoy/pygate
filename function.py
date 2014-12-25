import lob
import subprocess

def git():
    lob.output_b("Checking for updates")
    subprocess.call("git pull",shell=True)
    lob.output_b("Pushing upto GitHub")
    commit = raw_input("Commit: ")
    subprocess.call("git add .", shell=True)
    subprocess.call("git commit -m "+"'"+commit+"'",shell=True)
    subprocess.call("git push",shell=True)
    lob.output_b("Complete")
