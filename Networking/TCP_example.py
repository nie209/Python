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
print("socket connected to host: " + host + " it's ip address is: "+ remote_ip)


# try to send a message using GET method
message = "GET / HTTP/1.1\r\n\n\n"

try:
    s.sendall(message.encode())
except socket.error:
    print("unable to send request to google")
    sys.exit()
print("message has been send")
# get the reply back from the host and it need it to
reply = s.recv(4096)

# using the decode function it will print in a more readable format for the replay message
print(reply.decode())
s.close()
