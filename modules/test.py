from ravegen import *
import bm_client

@RaveGen
@Command
def test(message):
    data = {}
    data['test'] = "Hola Mundo"
    return bm_client.sendData(data)
    

