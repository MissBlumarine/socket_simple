import socket


def senter(text: str):
    
    # переводим введенную строку в байты, т.к. сервер принимает данные в виде байт
    b = bytes(text, 'utf-8') 
    
    # создаем сокет
    sock = socket.socket()
    
    # вводим данные хоста и порта сервера
    sock.connect(('', 9090))
    sock.send(b)

    data = sock.recv(1024)
    sock.close()

    print(data)
