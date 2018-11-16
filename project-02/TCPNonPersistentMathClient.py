from socket import *

serverName = 'localhost'
serverPort = 5000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
checker = True

while checker:
    num1 = input("Input first number: ")
    if num1 == "quit":
        clientSocket.send(num1.encode())
        break
    
    num2 = input("Input second number: ")
    if num2 == "quit":
        clientSocket.send(num1.encode())
        clientSocket.send(num2.encode())
        break
    
    expression = input("Input math expression: ")
    if expression == "quit":
        clientSocket.send(num1.encode())
        clientSocket.send(num2.encode())
        clientSocket.send(expression.encode())
        break
    
    clientSocket.send(num1.encode())
    clientSocket.send(num2.encode())
    clientSocket.send(expression.encode())

    result = clientSocket.recv(1024)
    print(result.decode())

print("Client is closed. Bye!")
clientSocket.close()
