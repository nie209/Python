import socket
import sys


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

    print("sockte has been bounded")
    return s


def listen_for_incoming_message(bind_socket):
    # allowing the socket handle up to 10 people
    bind_socket.listen(10)
    print("socket is ready ")
    connection, address = bind_socket.accept()
    print("connected with " + address[0] + ": " + str(address[1]))
    receive_data(connection)


def receive_data(connection):
    while True:
        data = connection.recv(4096)
        connection.sendall(data)
        print(data.decode())

    connection.close()


if __name__ == "__main__":
    s = create_socket_connection("", 8888)
    listen_for_incoming_message(s)
    s.close()








