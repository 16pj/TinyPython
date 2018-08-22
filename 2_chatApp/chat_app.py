import socket
import threading
import os

SERVERIP = '127.0.0.1'
SERVERPORT = 5000
CLIENTIP = '127.0.0.1'
CLIENTPORT = 5001



def RetrMessage(name, sock):
    message = sock.recv(1024)
    if str(message) == "INITIATE":
            sock.send("BEGIN")
            message = sock.recv(1024)
            print name + ":> " + message
            while message != "":
                message = sock.recv(1024)
                print name + ":> " + message
    else:
        sock.send("ERR")
    sock.close()

def Serveros(serverip = SERVERIP, serverport=SERVERPORT, SFLAG="SERVER"):

        host = serverip
        port = serverport
        s = socket.socket()
        s.bind((host, port))
        s.listen(5)

        print "Server Started."
        while True:
            c, addr = s.accept()
            if SFLAG == "SERVER":
                SFLAG = "CLIENT"
                t = threading.Thread(target=Client, args=(CLIENTIP, CLIENTPORT, "SERVER"))
                t.start()
            print "client connected ip:<" + str(addr) + ">\n"
            t = threading.Thread(target=RetrMessage, args=("Him",c))
            t.start()
        s.close()

def Client(serverip = CLIENTIP, serverport = CLIENTPORT, CFLAG="CLIENT"):
    host = serverip
    port = serverport

    s  = socket.socket()
    s.connect((host,port))

    if CFLAG == "CLIENT":
        CFLAG = "SERVER"
        t = threading.Thread(target=Serveros, args=('127.0.0.1', 5001, "CLIENT"))
        t.start()

    message = raw_input("\ninit You:> ")
    if message != 'q':
        s.send("INITIATE")
        data = s.recv(1024)
        if data[:5] == "BEGIN":
            while message != 'q':
                    message = raw_input("")
                    s.send(message)
    s.close()


if __name__ == '__main__':
    message = raw_input("Wait or connect first? w/c > ")
    if message == 'w':
        Serveros(SERVERIP, SERVERPORT, "SERVER")
    elif message == 'c':
        Client(CLIENTIP, CLIENTPORT, "CLIENT")
    else:
        print "Sorry your option is invalid"

