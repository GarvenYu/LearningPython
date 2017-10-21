import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('112.74.167.157', 9999))
print(s.recv(1024).decode('UTF-8'))
for data in [b'YY', b'KK', b'BB']:
    s.send(data)
    print(s.recv(1024).decode('UTF-8'))
s.send(b'bye')
s.close()