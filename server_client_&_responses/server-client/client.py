import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 8888))

full_msg = ''
new_msg = True
while True:
    msg = s.recv(20)
    if len(msg) <= 0:
        break
    else:
        full_msg += msg.decode("utf-8")

print(full_msg)
