import socket

host='127.0.0.1'

port=9000
#Creating Server Socket
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((host,port))

server_socket.listen(5)

print(f"Listening From {host},{port}")

#load balancer to act as medium between client and backend server
while True:
    client_socket,client_addr= server_socket.accept()
    print(f"Recieved comms from {client_addr}")
    #Recieving Data From Client Side
    req_data=client_socket.recv(1024)

    #Creating Backend Socket
    backend_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    backend_socket.connect(('127.0.0.1',8001)) #connection to the server on port 8001
    #Sending Request to Backend Server
    backend_socket.sendall(req_data)
    #capturing Response from Backend Server
    response_data=backend_socket.recv(4096)
    #Sending response back to client
    client_socket.sendall(response_data)
    
    client_socket.close()
    backend_socket.close()
