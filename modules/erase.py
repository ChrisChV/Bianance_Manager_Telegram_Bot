from ravegen import *
import sad
import bm_client

@RaveGen
@Command(description="Cancel Transaction")
def cancel(message):
    args = message.split()
    return generateData(args, sad._CANCEL_OPERATION_TYPE_)

@RaveGen
@Command(description="Disable Transaction")
def disable(message):
    args = message.split()
    return generateData(args, sad._DISABLE_OPERATION_TYPE_)

def generateData(args, oper_type):
    if len(args) < 1:
        return "Arguments missing <transaction_id>"
    if len(args) > 1:
        return "Only 1 argument <transaction_id>"
    data = {}
    data[sad._JSON_OPERATION_TYPE_] = oper_type
    data[sad._JSON_TRANSACTION_ID_] = int(args[0])
    return bm_client.sendData(data)
