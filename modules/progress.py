from ravegen import *
import sad
import bm_client 

@RaveGen
@Command(description="Create a new Transaction: <symbol> <entry> <lose> <profit> <quantity>")
def new(message):
    args = message.split()
    if len(args) < 5:
        return "Arguments missing <symbol> <entry> <lose> <profit> <quantity>"
    if len(args) > 5:
        return "Only 5 arguments <symbol> <entry> <lose> <profit> <quantity>"
    data = {}
    data[sad._JSON_OPERATION_TYPE_] = sad._PROGRESS_OPERATION_TYPE_
    data[sad._JSON_SYMBOL_] = args[0]
    data[sad._JSON_ENTRY_] = float(args[1])
    data[sad._JSON_LOSE_] = float(args[2])
    data[sad._JSON_PROFIT_] = float(args[3])
    data[sad._JSON_QUANTITY_] = float(args[4])
    return bm_client.sendData(data)