import socket
import time

SERVER_HOST = "127.0.0.1"

# Between 1 and 65535
#
SERVER_PORT = 65432

# AF_INET is IPv4
# AF_INET6 is IPv6
# SOCK_STREAM is TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((SERVER_HOST, SERVER_PORT))
    time.sleep(10)
    sock.sendall(b"THIS IS FROM CLIENTXXX")
    res = sock.recv(1024)

print(res)