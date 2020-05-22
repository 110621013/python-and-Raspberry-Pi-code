import socket
def client_thread(client_socket):
    client_socket.send("Welcome:".encode())
    while 1:
        get_request=client_socket.recv(8192).decode()
        print(get_request)
        if get_request =="quit!":
            break
        client_socket.send(get_request.upper().encode())
    client_socket.close()

server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1",8000))
server_socket.listen(5)

while 1:
    client_socket,addr=server_socket.accept()
    print(addr)
    client_thread(client_socket)