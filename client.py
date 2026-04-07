import socket

host = '127.0.0.1'
port = 5001

obj = socket.socket()
obj.connect((host, port))

print("Connected to the server...")

while True:
    message = input("Type message (or 'q' to quit): ")
    if message == 'q':
        break
    obj.send(message.encode())
    
    data = obj.recv(1024).decode()
    print('Received from server: ' + data)

obj.close()