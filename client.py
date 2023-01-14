import socket


def senter(text):
    b = bytes(text, 'utf-8')
    sock = socket.socket()
    sock.connect(('', 9090))
    sock.send(b)

    data = sock.recv(1024)
    sock.close()

    print(data)