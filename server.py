import socket

# создаем сокет
sock = socket.socket()

# определяем хост и порт
sock.bind(('', 9090))

# запускаем режим прослушивания порта
# в качестве аргумента передаем максимальное количество подключений в очереди
sock.listen(5)

# подключение для приема и посылки данных клиенту
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

