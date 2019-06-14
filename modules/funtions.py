from ravegen import *
import sad
import bm_client

@RaveGen
@Command(description="Creates a new Transaction with simple function")
def simple(message):
    args = message.split()
    return generateData(args, sad._FUNCTION_SIMPLE_)

@RaveGen
@Command(description="Creates a new Transaction with half function")
def half(message):
    args = message.split()
    return generateData(args, sad._FUNCTION_HALF_)

@RaveGen
@Command(description="Creates a new Transaction with infiniteP function")
def infinitep(message):
    args = message.split()
    return generateData(args, sad._FUNCTION_INFINITE_P_)

def generateData(args, function):
    if len(args) < 5:
        return "Arguments missing <symbol> <entry> <lose> <profit> <quantity>"
    if len(args) > 5:
        return "Only 5 arguments <symbol> <entry> <lose> <profit> <quantity>"
    data = {}
    data[sad._JSON_OPERATION_TYPE_] = sad._NEW_OPERATION_TYPE_
    data[sad._JSON_SYMBOL_] = args[0]
    data[sad._JSON_ENTRY_] = float(args[1])
    data[sad._JSON_LOSE_] = float(args[2])
    data[sad._JSON_PROFIT_] = float(args[3])
    data[sad._JSON_QUANTITY_] = float(args[4])
    data[sad._JSON_FUNCTION_] = function
    return bm_client.sendData(data)
