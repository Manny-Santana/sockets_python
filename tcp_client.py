# sends data to the server

import socket

HOST = "127.0.0.1" # server ip
PORT = 8080 # server port

sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

with sock as s: 
    s.connect((HOST, PORT))
    s.sendall(b"Hello, World!") #send byte data
    data = s.recv(1024) # receive response from server 

print(f"received: {data!r}")