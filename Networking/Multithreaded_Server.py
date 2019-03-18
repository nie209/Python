import socket
import sys
from _thread import *


def create_socket_connection(host, port):
    # AF_INET is telling the function use IPV4
    # SOCKET_STREAM is telling the function use TCP
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error:
        print("socket can not be created")
        sys.exit()
    print("socket has been created")
    try:
        s.bind((host, port))
    except socket.error:
        print("fail to bind the socket to the host")
        sys.exit()

    print("socket has been bounded")
    return s


def client_thread(connection):
    welcome_message = "Welcome to the server.\n"
    connection.send(welcome_message.encode())
    while True:
        data = connection.recv(1024)
        replay = "OK. " + data.decode()
        print(replay)
        if not data:
            break
        connection.sendall(data)
    connection.close()


def listen_for_incoming_message(bind_socket):
    # allowing the socket handle up to 10 people
    bind_socket.listen(10)
    print("socket is ready ")
    while True:
        connection, address = bind_socket.accept()
        print("connected with " + address[0] + ": " + str(address[1]))
        start_new_thread(client_thread, (connection, ))
    receive_data(connection)
    return connection


if __name__ == "__main__":
    s = create_socket_connection("", 8888)
    conn = listen_for_incoming_message(s)
    s.close()





