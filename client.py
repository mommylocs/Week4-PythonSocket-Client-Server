import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 9500
s.connect(('localhost', port))
msg = input('Enter Your Message: ')
s.sendall(msg.encode())

reply = s.recv(1024)
data = reply.decode("utf-8")
print('Reply received:', data)

s.close()