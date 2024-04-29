import socket


""" server that just accepts any message over the network
and echos back the message on the terminal """

HOST = "127.0.0.1" # string representation of ip address
PORT = 8080 # must actually be a number passed into the bind function as a tuple according to docs

# AF_INET = ipv4  ip address required - the default socket is af_inet with type sock_stream eg: tcp
sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)


with sock as s:

    # bind listen accept instantiation of socket 
    s.bind((HOST,PORT))
    s.listen() # listens for connections and determines how many connections can be in backlog
    conn, addr = s.accept() # blocking - returns a connection and an the address of the incomming connection

    # the connection must be what contains the recv function to get the data from the network
    with conn: 
        print(f"Connected by {addr}") # addr is a tuple (interface/ip, port)

        # continue unpacking data of the given buffersize passed to the conn.recv function until there is no data left
        while True:
            data = conn.recv(1024)
            if not data: 
                break
            conn.sendall(data) # why do i need this??? - sends data back to the connection socket as a byte response! 
