from socket import *

serverName = 'localhost'
serverPort = 5000
clientSocket = socket(AF_INET, SOCK_DGRAM)
num1 = 0
num2 = 0
expression = ""

while (num1 or num2) != "quit":
    num1 = input("Input first number: ")
    num2 = input("Input second number: ")
    expression = input("Input math expression: ")
    clientSocket.sendto(num1.encode(), (serverName, serverPort))
    clientSocket.sendto(num2.encode(), (serverName, serverPort))
    clientSocket.sendto(expression.encode(), (serverName, serverPort))
    if expression == "quit":
        break
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print(modifiedMessage.decode())

print("Client is closed. Bye!")
clientSocket.close()
