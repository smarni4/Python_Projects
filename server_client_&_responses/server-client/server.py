import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 8888))
s.listen(5)

while True:
    client_socket, address = s.accept()
    print(f"Connection from {address} has been established!")
    client_socket.send(bytes("Welcome to the server", "utf-8"))
    client_socket.close()


