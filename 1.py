import datetime
import socket

print(datetime.datetime.now())

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:    # ??
    s.bind((HOST, PORT))                        ## Associate with spesific Host and Port
    s.listen()
    conn, addr = s.accept()                     ## Server accepts connection and Listen
    with conn:
        print('Connected by IP: ', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
            # socket.close()

