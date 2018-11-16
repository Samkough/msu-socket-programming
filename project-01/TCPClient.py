from socket import *

serverName = 'localhost'
serverPort = 5000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = ""

while sentence != "quit":
    sentence = input("Input a lowercase sentence: ")
    clientSocket.send(sentence.encode())
    modifiedSentence = clientSocket.recv(1024)
    print(modifiedSentence.decode())

print("Client is closed. Bye!")
clientSocket.close()
