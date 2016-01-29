'''
Sprout - An accessible, extensible, and self-contained Configuration Management Engine for Linux and Windows.
Written By: Luke Brady 2015, 2016
Tell Your Friends!!!
https://github.com/lbrad23105/Sprout
lbrad23105@gmail.com
'''
#This code will be imported into the configuration file.

import sys, os, re, socket,subprocess
from subprocess import call as sub

#Checks the system and runs windows configurations.
if sys.platform == "win32":
    #Defines the Node Sprout.
    def Config( configuration ):
        print("> Sprout has configured your machine.")
        return 0
    
    #Defines the File Sprout.
    def File( name , content = "", ensure = "absent", path = ""):
        if( ensure == "present" ):
            if os.path.exists(path + '\\' + name):
                print("> The file '" + name + "' already exists.")
                return 0
            else:
                fileOne = open(path + '\\' + name,'w')
                fileOne.write(content)
                fileOne.close()
                print("> The file '" + name + "' has been created.")
                return 0
                
        if( ensure == "absent" ):
            if os.path.exists(path + '\\' + name):
                os.remove(path + '\\' + name)
                print("> File '" + name + "' has been removed.")
                return 0
                
    #Defines the Script Sprout.
    def Script( name, code, ensure = "absent"):
        if ensure == "present":
                pspass = subprocess.Popen([r'C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe',
                             '-ExecutionPolicy',
                             'Unrestricted',
                             './buildxml.ps1','mkdir','C:\\Users\\Luke Brady\\Desktop\\Cool'], cwd=os.getcwd())
                result = pspass.wait()
                print("> PowerShell has run " + code + ".")
        
    #Defines the Directory Sprout.
    def Directory( name, ensure = "absent", path = ""):
        if ensure == "present":
            if os.path.exists(path + "\\" + name):
                print("> The directory '" + path + "\\" + name + "' already exists.")
                return 0
            else:
                os.makedirs(path + "\\" + name)
                print("> " + path + "\\" + name  + " has been created.")
        if( ensure == "absent" ):
            if os.path.exists(path + "\\" + name):
                os.rmdir(path)
                print("> Directory '" + path + "\\" + name + "' removed.")
            else:
                print("> Directory '" + path + "\\" + name + "' does not exist.")
            

    def Registry_Key( ensure = "absent", path = "", purge_values = False):
        return 0

    def Registry_Value( data, ensure = "absent" ):
        return 0

    def Package( name, ensure = "absent" ):
        return 0

    def User( name, comment = "", ensure = "absent", uid = "", gid = "", groups = [], password = "" ):
        return 0
'''
Below is the Linux Version of Sprout. This allows Sprout to check the system type and
run configurations accordingly. 
'''

#Checks system and runs Linux configuations.
if sys.platform == "linux":
    #Defines the Node Sprout.
    def Config( configuration ):
        print("> Sprout has configured your machine.")
        return 0
        
     #Defines the File Sprout.
    def File( name, mode, content = None, ensure = None, path = None):
        if( ensure == "present" ):
            if(os.path.exists(path + '/' + name)):
                print("> The file '" + name + "' already exists.")
                return 0
            else:
            #Uses the sub env variable imported earlier.
                file = open(path + "/" + name, w)
                file.write(content)
                sub(["sudo","chmod",mode,path + '/' + name])
                file.close()
                print("> The file " + name + " has been created in " + path + ".")
                return 0
        if( ensure == "absent" ):
            if os.path.exists(path + '/' + name):
                os.remove(path + "/" + name)
                print("> The file " + name  + " has been deleted.")
                return 0
    #Defines the Directory Sprout.
    def Directory( name, ensure = "absent", path = ""):
        if ensure == "present":
            if os.path.exists(path + "/" + name):
                print("> The directory '" + path + "/" + name + "' already exists.")
                return 0
            else:
                os.makedirs(path + "/" + name)
                print("> " + path + "/" + name  + " has been created.")
                return 0
        if( ensure == "absent" ):
            if os.path.exists(path + "/" + name):
                os.rmdir(path)
                print("> Directory '" + path + "/" + name + "' removed.")
                return 0
            else:
                print("> Directory '" + path + "/" + name + "' does not exist.")
                return 0
            

    def Package( name, distro, ensure = "absent" ):
        #Install Packages.
        if( ensure == "present" and distro == "debian" ):
            #Subcommand calls apt-get for use within Debian Distros.
            sub(["sudo","apt-get","install","-y",name])
            print("> " + name + " has been installed.")
            return 0
        if( ensure == "present" and distro == "redhat" ):
            #Subcommand calls apt-get for use within RedHat Distros.
            sub(["sudo","yum","install","-y",name])
            print("> " + name + " has been installed.")
            return 0
        if( ensure == "present" and distro == "fedora" ):
            #Subcommand calls apt-get for use within Fedora.
            sub(["sudo","dnf","install","-y",name])
            print("> " + name + " has been installed.")
            return 0
        #Remove Packages.
        if( ensure == "absent" and distro == "debian" ):
            #Subcommand calls apt-get for use within Debian Distros.
            sub(["sudo","apt","remove","-y",name])
            return 0
        if( ensure == "absent" and distro == "debian" ):
            #Subcommand calls apt-get for use within Debian Distros.
            sub(["sudo","apt","remove","-y",name])
            return 0
        if( ensure == "absent" and distro == "debian" ):
            #Subcommand calls apt-get for use within Debian Distros.
            sub(["sudo","apt","remove","-y",name])
            return 0
        else:
            return 0

    def Cron( name, user, command, minute, hour, day, month ):
        cron = minute + ' ' + hour + ' ' + day + ' ' + month + ' ' + user + ' ' + command
        sub(["sudo","crontab","<",cron])
        print("> Cron job " + name + " has been added to " + user + "'s crontab.")
        return 0
    def User( name, comment = "", ensure = "absent", uid = "", gid = "", groups = [], password = "" ):
        if(ensure == "present"):
            sub(['adduser',name,'-p',password])
        return 0
