# -*- coding:utf-8 -*-
import socket
import sys


def main():
    host = "localhost"
    port = 12345
    address = (host, int(port))

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(address)

    while True:
        mes = raw_input("please input what you want to say:")
        s.send(str(mes))
        try:
            buf = s.recv(1024)
            print buf
        except socket.error, e:
            print "Error receiving :", e
            sys.exit(1)
        if not len(buf):
            break
    s.shutdown(socket.SHUT_WR)
    s.close()


if __name__ == '__main__':
    main()
