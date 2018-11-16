from socket import *

count = 0
serverPort = 5000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The server is ready to receive.")
option = 0
result = 0

while True:
    if count == 0:
        connectionSocket, addr = serverSocket.accept()
    count = 1
    
    num1 = connectionSocket.recv(1024).decode()  
    num2 = connectionSocket.recv(1024).decode()
    expression = connectionSocket.recv(1024).decode()
    
    # pre-processing
    expression = str(expression)
    expression = expression.lstrip()
    expression = expression.rstrip()
    
    if expression in ("+", "add", "addition"):
        result = int(num1) + int(num2)
        option = 1
    elif expression in ("-", "subtract", "subtraction"):
        result = int(num1) - int(num2)
        option = 2
    elif expression in ("*", "multiply", "multiplication"):
        result = int(num1) * int(num2)
        option = 3
    elif expression in ("/", "divide", "division"):
        result = int(num1) / int(num2)
        option = 4
    else:
        print("Didn't understand your expression...please try again.")
        resultString = "Try again!"
        connectionSocket.send(resultString.encode())
        continue

    print("Expression #" + str(count) + " Message to be sent back: " + str(result))
    connectionSocket.send(str(result).encode())

print("Server is closed. Bye!")
connectionSocket.close()
