import socket
import sys

try:
    # AF_INET mean that it is using IPV4
    # SOCKET_STREAM it tell the function use the TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

except socket.error:
    print ("Failed to connected")
print ("Socket created")
host = "www.google.ca"
port = 80
try:
    # gethostbyname it will do a look up and return the IP address of the host
    remote_ip  = socket.gethostbyname(host)
except socket.gaierror:
    print("no IP address found for the host ")

print("IP address of " + host + "is " + remote_ip)
s.connect((remote_ip, port))
print("socket connected to host")

