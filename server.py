from socket import *
import threading

def on_new_client(clientsocket, addr):
    while True:
        msg = clientsocket.recv(1024)
        print(addr, ' >> ', msg)
        msg = input('SERVER >> ')
        clientsocket.send(msg)
    clientsocket.close()

serverPort = 5000
serverSocket = socket(AF_INET, SOCK_STREAM)

print('Server started!')
print('Waiting for clients...')

serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print('Got connection from', serverSocket)
while True:
   c, addr = serverSocket.accept()
   thread.start_new_thread(on_new_client,(c, addr))

s.close()
