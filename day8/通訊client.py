import socket
client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1",8000))
while 1:
    try:
        get_request = client_socket.recv(8192).decode()
        print(get_request)
        request=input()
        client_socket.send(request.encode())
        if request=="!quit":
            break
    except KeyboardInterrupt:
        client_socket.send("quit!".encode)
        break
client_socket.close()

    