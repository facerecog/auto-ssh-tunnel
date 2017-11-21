#!/usr/bin/env python
#
# Python Installer
#
import subprocess
import sys
import os
import platform

from Client import connect

# if nix or Mac then run installer
if platform.system() == "Linux" or platform.system() == "Darwin":
    # give installer a null value
    installer = False

    # Check user ID
    if os.getuid() != 0:
	print("Are you root? Please execute as root")
	exit()

    try:
	# if our command option is true then install dependencies
	if sys.argv[1] == "install":
	    installer = True
	    # check for custom ssh ports
	    if not sys.argv[2]:
	        ssh_port = 22
	    else:
		ssh_port = sys.argv[2]

    # if index is out of range then flag options
    except IndexError:
	print("** Auto SSH Dependency Installer by Facerecog Asia **")
	print("** Written by: Muhammad Amrullah (Facerecog Asia) **")
	print("** Visit: https://github.com/facerecog **")
	print("\nTo install: setup.py install")

    # if user specified install then lets proceed to the installation
    if installer is True:

        # install openssh-server with apt for Debian systems
        if platform.system() == "Linux":
            # if we trigger on sources.list then we know its Debian
            if os.path.isfile("/etc/apt/sources.list"):

                # force install of debian packages
                subprocess.Popen("apt-get --force-yes -y install openssh-server", shell=True).wait()
            # if sources.list is not available then we're running something offset
            else: 
                print("[!] You're not running a Debian variant. Installer not finished for this type of Linux distro.")
                print("[!] Install open-ssh server manually for all of autossh dependencies.")
                sys.exit()
	 
        if 'ServerAliveInterval' not in open('/etc/ssh/ssh_config').read():
            writetoSSH = open('/etc/ssh/ssh_config','a')
            writetoSSH.write("    ServerAliveInterval 30\n    ServerAliveCountMax 4")
            writetoSSH.close()

        if 'ClientAliveInterval' not in open('/etc/ssh/sshd_config').read():
            writetoSSH = open('/etc/ssh/sshd_config','a')
            writetoSSH.write("ClientAliveInterval 30\nClientAliveCountMax 4")
            writetoSSH.close()

	
	# if installation is done on client, the autossh automatically kicks in the daemon
	try:
	    rootname = connect.username_ipaddress
            if rootname == "":
                print "Please run configure.py first."
                sys.exit()
                
	    print("[*] Installing autossh client...")

	    print("[*] Installing autossh as startup application...")
	    subprocess.Popen("cd && mkdir .ssh", shell=True)

            if platform.system() == "Linux":
                subprocess.Popen("yes | cp Client/connect.py /etc/init.d/", shell=True).wait()
                subprocess.Popen("chmod +x /etc/init.d/connect.py", shell=True).wait()
                subprocess.Popen("update-rc.d connect.py defaults 100", shell=True).wait()
            elif platform.system() == "Darwin":
                subprocess.Popen("mkdir /System/Library/StartupItems/auto-ssh-tunnel", shell=True)
                subprocess.Popen("yes | cp mac/StartupParameters.plist /System/Library/StartupItems/auto-ssh-tunnel/", shell=True)
                subprocess.Popen("yes | cp Client/connect.py /System/Library/StartupItems/auto-ssh-tunnel/", shell=True)
                subprocess.Popen("chmod +x /System/Library/StartupItems/auto-ssh-tunnel/connect.py", shell=True).wait()

            subprocess.call("printf 'priv_key\n\n' | ssh-keygen -t rsa -b 2048 -v -P ''", shell=True)

	    print("[*] Copying SSH-Keys file over to server...")
            if platform.system() == "Linux":
                subprocess.call(['ssh-copy-id', '-i', 'priv_key.pub', rootname, '-p', ssh_port])
            elif platform.system() == "Darwin":
                subprocess.Popen("cat priv_key.pub | ssh -p" + ssh_port + " " + rootname + " 'cat >> ~/.ssh/authorized_keys'", shell=True).wait()

            print("[*] Installing private keys inside protected folder...")
            subprocess.Popen("yes | cp Client/connect.py /usr/local/bin/", shell=True)
	    subprocess.Popen("chmod +x /usr/local/bin/connect.py", shell=True).wait()

	    print("[*] Moving autossh client into the /usr/local/bin/ directory...")
            
	    print("[*] Moving private key to /etc/auto-ssh-tunnel/")
            subprocess.Popen("mkdir /etc/auto-ssh-tunnel && yes | cp priv_key /etc/auto-ssh-tunnel/priv_key", shell=True)
            # subprocess.Popen("yes | cp priv_key /etc/auto-ssh-tunnel/priv_key", shell=True)
	except subprocess.CalledProcessError as e:
	    pass
	
	# if the installation has been successful
	if os.path.isfile("/usr/local/bin/connect.py"):
	    print("[*] We are now finished! Restart the client to complete the installation. To run autossh, input connect.py on the terminal")
	    subprocess.Popen("sudo python /usr/local/bin/connect.py", shell=True)
	else:
	    print("[!] Installation has failed. Please ensure that connect.py and .pub file is installed")

# if the platform is running on a MAC, a version will be ready soon
# if platform.system() == 'Darwin':
    # print("[!] A version for Mac will be ready soon")

if platform.system() != "Linux" and platform.system() != "Darwin":
	print("[!] Sorry this installer is not designed for any other system other than Linux or Mac. Please install the python dependencies manually.")
