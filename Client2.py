from threading import Thread
import socket
import random

class SendingThread(Thread):
    def __init__(self, serverSocket):
        Thread.__init__(self)
        self.cSocket = serverSocket

    def run(self):
        while True:
            caesarRandom = (random.randint(1, 8))
            cipher_text = chr(caesarRandom + 96)
            msg = input()
            new_text=""
            for c in msg:
                 cipher_text1 = ord(c) + caesarRandom
                 if cipher_text1 > ord('z') or (cipher_text1 < ord('a') and cipher_text1 > ord('Z')):
                     cipher_text1 -= 26
                 new_text += (chr(cipher_text1))

            self.cSocket.send(bytes(new_text+cipher_text, "utf-8"))


class ReceivingThread(Thread):
    def __init__(self, serverSocket):
        Thread.__init__(self)
        self.cSocket = serverSocket

    def run(self):
        while True:
            msg = self.cSocket.recv(1024)
            print(msg.decode('utf-8'))


print("Client")

s = socket.socket();
hostServer = socket.gethostname()  # IP Server
hostClient = socket.gethostname()# IP Client
portServer = 2003
portClient = 3004

s.bind((hostClient, portClient))
s.connect((hostServer, portServer))  # Request to server

print(socket.gethostbyname(hostServer))
sendThread = SendingThread(s)
receiveThread = ReceivingThread(s)

sendThread.start()
receiveThread.start()


