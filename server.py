import socket


sock = socket.socket()

sock.bind(('', 9090))
sock.listen(5)
conn, addr = sock.accept()

print('connected:', addr)

while True:
    data = conn.recv(1024)
    udata = data.decode("utf-8")
    if not data:
        break
    print('data:', udata)
    conn.send(data.upper())

conn.close()

