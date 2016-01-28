#!/bin/bash

#Configuration for ssh keys, port of server and the username with ip address of server
sshfile = "/root/raspi.pem"
portnumber = 22223:localhost:22
useripaddress = ubuntu@52.77.229.57

createTunnel() {
  /usr/bin/ssh -i $sshfile -N -R $portnumber $useripaddress
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
