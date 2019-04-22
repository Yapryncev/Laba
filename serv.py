import socket
import ch_und as und

sock = socket.socket()
sock.bind(('127.0.0.1', 55556)) # ожидаем клиента
sock.listen(1)

while True:
    conn, addr = sock.accept()

#print 'connected:', addr

    while True:
        if conn == 'PROCESS':
            FH = und.Fishimage(None, None, None, None)
            FH.understortV()
            FH.understortN()
            FH.warpV()
            FH.warpN()
            FH.stitch()
            conn.send('OK')   # команда клиенту
        #data = conn.recv(1024) # нужно получить строго нужную длинну посылки
        if not conn:
            break


conn.close()