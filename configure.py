#!/usr/bin/env python

import argparse
parser = argparse.ArgumentParser(description="Configure auto-ssh-tunnel")
parser.add_argument("port", metavar="port", type=int, nargs=1, help="Port number of the ssh server")
parser.add_argument("username", metavar="username", type=str, nargs=1, help="Username with which log in to the server")
parser.add_argument("server", metavar="server", type=str, nargs=1, help="Server IP address")
args = parser.parse_args()

port = args.port[0]
username = args.username[0]
server = args.server[0]

server_str = username + "@" + server

port_open_str = "port_open"
username_ipaddress_str = "username_ipaddress"

connect_file = open("Client/connect.py", "r")
lines = connect_file.readlines()

port_open_line = None
username_ipaddress_line = None
i = 1
for line in lines:
    if line.startswith(port_open_str):
        port_open_line = i
    if line.startswith(username_ipaddress_str):
        username_ipaddress_line = i

    i += 1

lines[port_open_line - 1] = "port_open = \"" + str(port) +"\"" + "\n"
lines[username_ipaddress_line - 1] = "username_ipaddress = \"" + str(server_str) +"\"" + "\n"

edited_lines = ""
for line in lines:
    edited_lines += line

connect_file.close()

print "Writing to connect.py..."
connect_file = open("Client/connect.py", "w")
connect_file.write("".join(edited_lines))
connect_file.close()

print "Configuration successful."
