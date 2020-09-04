import os
from shutil import copyfile

installPath = "/usr/local/bin"
possiblePaths = os.environ['PATH'].split(':')
commmandName = "gcp"
fileName = "generate-password.py"

if(installPath in possiblePaths):
    copyfile(fileName, installPath + "/" + commmandName)

    os.chdir(installPath)

    os.system('chmod +x ' + commmandName)

    print("Install Command (" + commmandName + ")")
else:
    print("Command ("+ commmandName + ") - not Installed")

