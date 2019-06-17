from ravegen import *
import modules.sad as sad
import bm_client
import json

@Command(description="Get info for all open transactions")
def getOpens(bot, update):
    if not bm_client.verifyAdmin(update):
        update.effective_message.reply_text("You don't have permissions")
        return
    data = {}
    data[sad._JSON_OPERATION_TYPE_] = sad._GET_OPEN_OPERATION_TYPE_
    res_data = bm_client.sendData(data)
    res_data  = json.loads(res_data)
    if not res_data:
        return "There isn't open transactions"
    message = generateMessage(res_data)
    update.effective_message.reply_text(message)
    #return generateMessage(res_data)

def generateMessage(res_data):
    message = ""
    for transaction_id, data in res_data.iteritems():
        message += "Transaction " + str(transaction_id) + '\n'
        message += "Symbol: " + data[sad._JSON_SYMBOL_] + '   '
        message += "Function: " + data[sad._JSON_FUNCTION_] + '   '
        message += "State: " + data[sad._JSON_STATE_] + '   '
        message += "Quantity: " + str(data[sad._JSON_QUANTITY_]) + '\n'
        message += "Entry Order:" + '\n'
        message += "Price: " + str(data[sad._JSON_ENTRY_]) + '   '
        message += "State: " + data[sad._JSON_ENTRY_STATE_] + '\n'
        message += "Lose Order:" + '\n'
        message += "Price: " + str(data[sad._JSON_LOSE_]) + '   '
        message += "State: " + data[sad._JSON_LOSE_STATE_] + '\n'
        message += "Profit Order:" + '\n'
        message += "Price: " + str(data[sad._JSON_PROFIT_]) + '   '
        message += "State: " + data[sad._JSON_PROFIT_STATE_] + '\n\n'
    return message
