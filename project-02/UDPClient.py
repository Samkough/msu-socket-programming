from socket import *

serverName = 'localhost'
serverPort = 5000
clientSocket = socket(AF_INET, SOCK_DGRAM)
num1 = 0
num2 = 0
expression = ""

while True:
    num1 = input("Input first number: ")
    if num1 == "quit":
        clientSocket.sendto(num1.encode(), (serverName, serverPort))
        break
    
    num2 = input("Input second number: ")
    if num2 == "quit":
        clientSocket.sendto(num1.encode(), (serverName, serverPort))
        clientSocket.sendto(num2.encode(), (serverName, serverPort))
        break
    
    expression = input("Input math expression: ")
    if expression == "quit":
        clientSocket.sendto(num1.encode(), (serverName, serverPort))
        clientSocket.sendto(num2.encode(), (serverName, serverPort))
        clientSocket.sendto(expression.encode(), (serverName, serverPort))
        break
    
    clientSocket.sendto(num1.encode(), (serverName, serverPort))
    clientSocket.sendto(num2.encode(), (serverName, serverPort))
    clientSocket.sendto(expression.encode(), (serverName, serverPort))
    
    if expression == "quit":
        break
    result, serverAddress = clientSocket.recvfrom(2048)
    print(result.decode())

print("Client is closed. Bye!")
clientSocket.close()
