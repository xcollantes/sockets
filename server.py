import socket

SERVER_HOST = "127.0.0.1"

# Between 1 and 65535
SERVER_PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # SO_REUSEADDR for not getting error "Address already in use"
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((SERVER_HOST, SERVER_PORT))

    # If your server receives lots of connection requests simultaneously,
    # increasing the backlog value
    sock.listen(2)
    print(f"Listening on {SERVER_HOST}:{SERVER_PORT}")
    while True:
        conn, address = sock.accept()
        res = conn.recv(1024)

        if res:
            text = "From server: {res}".format(res=res)
            print(text)
            conn.sendall(bytes(text, encoding="utf-8"))
