import socket
import ch_und as und

sock = socket.socket()
sock.bind(('', 55556)) # ожидаем клиента
sock.listen(1)
while True:
    conn, addr = sock.accept()
    print ('connected:', addr)
    while True:
        data = conn.recv(1024)
        a = str(data, 'utf-8')
        kd = 'PROCESS\n'
        if a == kd:
            FH = und.Fishimage(None, None, None, None)
            try:
                FH.understortV()
                FH.understortN()
            except:
                conn.send(b"ERR\n")
            FH.warpV()
            FH.warpN()
            FH.stitch()
            conn.send(b"OK\n")
        else:
            conn.send(b"ERR\n")
        if not data:
                break

            #print (addr)# команда клиенту
        #data = conn.recv(1024) # нужно получить строго нужную длинну посылки



conn.close()