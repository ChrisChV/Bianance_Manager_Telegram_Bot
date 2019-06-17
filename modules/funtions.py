from ravegen import *
import sad
import bm_client

@Command(description="Creates a new Transaction with simple function", passArgs=True)
def simple(bot, update, args):
    #args = message.split()
    if not bm_client.verifyAdmin(update):
        update.effective_message.reply_text("You don't have permissions")
        return
    message = generateData(args, sad._FUNCTION_SIMPLE_)
    update.effective_message.reply_text(message)
    #return generateData(args, sad._FUNCTION_SIMPLE_)

@Command(description="Creates a new Transaction with half function", passArgs=True)
def half(bot, update, args):
    #args = message.split()
    if not bm_client.verifyAdmin(update):
        update.effective_message.reply_text("You don't have permissions")
        return
    message = generateData(args, sad._FUNCTION_HALF_)
    update.effective_message.reply_text(message)
    #return generateData(args, sad._FUNCTION_HALF_)

@Command(description="Creates a new Transaction with infiniteP function", passArgs=True)
def infinitep(bot, update, args):
    #args = message.split()
    if not bm_client.verifyAdmin(update):
        update.effective_message.reply_text("You don't have permissions")
        return
    message = generateData(args, sad._FUNCTION_INFINITE_P_)
    update.effective_message.reply_text(message)
    #return generateData(args, sad._FUNCTION_INFINITE_P_)

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
