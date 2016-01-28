#!/usr/bin/env python
#
# Python Installer
#
import subprocess
import sys
import os
import platform

# if nix then run installer
if platform.system() == "Linux":
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

    # if index is out of range then flag options
    except IndexError:
	print("** Auto SSH Dependency Installer by Facerecog Asia **")
	print("** Written by: Muhammad Amrullah (Facerecog Asia) **")
	print("** Visit: https://github.com/facerecog **")
	print("\nTo install: setup.py install")

    # if user specified install then lets proceed to the installation
    if installer is True:

	# if we trigger on sources.list then we know its ubuntu
	if os.path.isfile("/etc/apt/sources.list"):

	    # force install of debian packages
	    subprocess.Popen("apt-get --force-yes -y install openssh-server", shell=True).wait()
	 
	    if 'ServerAliveInterval' not in open('/etc/ssh/ssh_config').read():
    		writetoSSH = open('/etc/ssh/ssh_config','a')
    		writetoSSH.write("    ServerAliveInterval 30\n    ServerAliveCountMax 4")
    		writetoSSH.close()

	    if 'ClientAliveInterval' not in open('/etc/ssh/sshd_config').read():
	        writetoSSH = open('/etc/ssh/sshd_config','a')
    		writetoSSH.write("ClientAliveInterval 30\nClientAliveCountMax 4")
    		writetoSSH.close()

	# if sources.list is not available then we're running something offset
	else: 
	    print("[!] You're not running a Debian variant. Installer not finished for this type of Linux distro.")
	    print("[!] Install open-ssh server manually for all of autossh dependencies.")
	    sys.exit()
	
	# if installation is done on client, the autossh automatically kicks in the daemon
	try:
	    ClientorServer = raw_input("Is this a client[C] or a server[S]? [C]/[S]: ")
	    if ClientorServer == 'C':
		print("[*] Moving autossh client into the /usr/local/bin/ directory...")
		subprocess.Popen("yes | cp Client/connect.sh /usr/local/bin/", shell=True).wait()
		print("[*] Installing autossh client...")
		subprocess.Popen("chmod +x /usr/local/bin/connect.sh", shell=True).wait()
		print("[*] Installing autossh as startup application...")
		subprocess.Popen("yes | cp Client/connect.sh /etc/init.d/", shell=True).wait()
                subprocess.Popen("chmod +x /etc/init.d/connect.sh", shell=True).wait()
		
		# if the link of the .pem security file is provided, an automatic download is made
		DownloadPEM = raw_input("What is the link to download the .PEM file. If no download link, input [N]: ")
		DownloadFile = "wget %s" % DownloadPEM

		# automatic installation will kick-in followed by a request to restart the PC
		try:
		    subprocess.Popen(DownloadPEM, shell=True).wait()
		    print("[*] Downloading ssh .PUB file from site and installing...")
		    subprocess.Popen("chmod 400 *.pub", shell=True).wait()
                    subprocess.Popen("yes | cp *.pub /etc/init.d/", shell=True).wait()
                    subprocess.Popen("yes | cp *.pub /usr/local/bin/", shell=True).wait()
		except subprocess.CalledProcessError as e:
		    pass

            if ClientorServer == 'S':
                subprocess.call("ssh-keygen -t rsa -b 2048 -v", shell=True)

	except ValueError:
	    print("[!] Please input C or S.")
        except subprocess.CalledProcessError as e:
            print("[!] Installation has failed. Please retry again")
	
	# if the installation has been successful
	if os.path.isfile("/usr/local/bin/connect.sh"):
            if os.path.isfile("/usr/local/bin/server.pub"):
		print("[*] We are now finished! Restart the client to complete the installation. To run autossh, input connect.sh on the terminal")
		subprocess.call("connect.sh", shell=True)
	if os.path.isfile("server.pub") and ClientorServer == 'S':
                print("[*] Certificate successfully generated. Please insert a physical USB to transfer the server.pub file to the Client")
	else:
	    print("[!] Installation has failed. Please ensure that connect.sh and .pub file is installed")

# if the platform is running on a MAC, a version will be ready soon
if platform.system() == 'Darwin':
    print("[!] A version for Mac will be ready soon")

if platform.system() != "Linux":
   if platform.system() != "Darwin":
	print("[!] Sorry this installer is not designed for any other system other than Linux or Mac. Please install the python dependencies manually.")
