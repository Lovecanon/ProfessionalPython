import socket
s = socket.socket()
s.connect(('59.111.160.195', 80))
request = 'GET / HTTP/1.0\r\n\r\n'
s.send(request.encode())
resp = s.recv(4444)
print(resp)