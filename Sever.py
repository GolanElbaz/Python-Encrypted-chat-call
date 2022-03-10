from threading import Thread
import socket

class SendingThread(Thread):
    def __init__(self, clientSocket):
        Thread.__init__(self)
        self.cSocket = clientSocket
    def run(self):
        while True:
            msg = input()
            self.cSocket.send(bytes(msg, "utf-8"))

class ReceivingThread(Thread):
    def __init__(self, clientSocket):
        Thread.__init__(self)
        self.cSocket = clientSocket
    def run(self):
        while True:
            msg = self.cSocket.recv(1024)
            caesarDis=msg[len(msg)-1]-96
            print(caesarDis)
            new_text=""
            i=0
            while(i<=len(msg)-2):
                cipher_text=msg[i]
                if cipher_text > ord('z') or (cipher_text < ord('a') and cipher_text > ord('Z')):
                    cipher_text -= 26
                new_text+=chr(cipher_text-caesarDis)
                i+=1
            print(msg.decode('utf-8'))
            print(new_text)
            self.cSocket.send(bytes(input("return message to client : "), "utf-8"))

s = socket.socket();
host = socket.gethostname()
portServer = 2003
s.bind((host, portServer))#הגדרת פורט של השרת
#s.listen()#האזנה
print(socket.gethostbyname(host))
print("Server...")

while True:
    s.listen()  # האזנה
    clientSocket, clientAddress = s.accept()  # <---- waiting for request

    sendThread = SendingThread(clientSocket)
    receiveThread = ReceivingThread(clientSocket)

    sendThread.start()
    receiveThread.start()



