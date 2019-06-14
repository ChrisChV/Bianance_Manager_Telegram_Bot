from ravegen import *
import sad
import bm_client

@RaveGen
@Command(description="Ping to Binance Manager Server")
def ping(message):
    data = {}
    data[sad._JSON_OPERATION_TYPE_] = sad._PING_OPERATION_TYPE_
    return bm_client.sendData(data)