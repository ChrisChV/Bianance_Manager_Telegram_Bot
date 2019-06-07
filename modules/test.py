from ravegen import *
import socket
import json

@RaveGen
@Command
def test(message):
    data = {}
    data['test'] = "Hola Mundo"
    return sendData(data)
    

def sendData(data):
    HOST = "10.244.222.117"
    PORT = 65432

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall(json.dumps(data))
    msg = s.recv(1024)
    s.close()
    return msg
