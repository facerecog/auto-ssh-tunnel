#!/bin/bash

#Configuration for ssh keys, port of server and the username with ip address of server
sshfile = "/home/install/Downloads/auto-ssh-tunnel"
#portnumber = 50000:localhost:22
#useripaddress = server@192.168.1.202

createTunnel() {
  /usr/bin/ssh -i $sshfile -N -R 50000:localhost:22 server@192.168.1.202
  if [[ $? -eq 0 ]]; then
    echo Tunnel to jumpbox created successfully
  else
    echo An error occurred creating a tunnel to jumpbox. RC was $?
  fi
}
/bin/pidof ssh
if [[ $? -ne 0 ]]; then
  echo Creating new tunnel connection
  createTunnel
fi
