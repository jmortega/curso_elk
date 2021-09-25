import socket
 
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind(('localhost', 8081))
mySocket.listen(5)
 
while True:
    print('Esperando conexiones...')
    (recvSocket, address) = mySocket.accept()
    print('Petición HTTP recibida:')
    print(recvSocket.recv(1024))
    recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n <html><body><h1>Hello World!</h1></body></html> \r\n",'utf-8'))
    recvSocket.close()
