import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 9500
s.bind(('0.0.0.0', port))
print ('Port 9500 Connected')
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print ('Connection Established')
    msg =  clientsocket.recv(1024)
    data = msg.decode("utf-8")
    print('Message recieved, Response sent')
    if data == 'Hello':
        reply = 'Hi'
        clientsocket.send(reply.encode())
        
    else:
        reply = 'Goodbye'
        clientsocket.send(reply.encode())
        

clientsocket.close()