# Automatic SSH Tunnel

Automatic SSH Tunnel is a **PYTHON** script which can be used to create a reverse ssh tunnel between multiple computers running Linux and a centralized server.

It's written in PYTHON scripting language.

**Why use this script?**

* **Portable:** It's written in PYTHON scripting and only needs *openSSH-server* (openSSH-server is a tool to enable computers to behave as a pseudo server to ensure a successful reverse tunnelling).
* **Secure:** It requires a USB hardware physical transfer of the ssh keys.

## Features

* Unix-enabled
* No password required or stored
* Simple step-by-step configuration wizard
* Takes less than 1 minute to fully set-up

## Getting started

First, clone the repository using git (recommended):

```bash
$ git clone https://github.com/facerecog/auto-ssh-tunnel/
```

Then change the PORT and the IP ADDRESS of the server we are connecting to:

```bash
$ cd Client
$ nano connect.py
```

```bash
location_of_pem_file = "/home/install/Downloads/auto-ssh-tunnel/server"
port_open = "50000"
username_ipaddress = "server@192.168.1.202"
```

Then give the execution permission to the setup.py script and run it:

```bash
$ sudo python setup.py install
```

The first time you run `setup.py install`, you'll be guided through a wizard in order to configure ssh as a [S]erver or a [C]lient.

## Configuration wizard

The configuration wizard is pretty self-explanatory. One thing to notice is that you will generate a `current_directory/<server>`. The file to `current_directory/<server>` is your pem key to enable this client to ssh to the server without the use of password. During the setup.py install, a public key will be pushed to the server and saved in `/.ssh/authorized_keys` You should never exchange your private pem keys to others.

### Configuration as a Client

```bash
Generating public/private rsa key pair.
Enter file in which to save the key (/home/anonymouse/.ssh/id_rsa): server
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in server.
Your public key has been saved in server.pub.
The key fingerprint is:
bb:c6:9c:ee:6b:c0:67:58:b2:bb:4b:44:72:d3:cc:a5 localhost@localhost
The key's randomart image is:
```

#### Configuration as a Server
```bash
$ ifconfig
```
Port forward your IP address to port 22 on your modem or router

## Available commands

* **connect.py**;
Manually connect the client to the server

## Tested Environments
* Raspberry Pi
* Ubuntu 14.04 LTS

## Customer Service and Support

 If you want to support this project, please consider reaching out to me:
  * Email: muhd.amrullah@facerecog.asia
