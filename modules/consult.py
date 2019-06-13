from ravegen import *
import modules.sad as sad
import bm_client
import json

@RaveGen
@Command(description="Get info for all open transactions")
def getOpens(message):
    data = {}
    data[sad._JSON_OPERATION_TYPE_] = sad._GET_OPEN_OPERATION_TYPE_
    res_data = bm_client.sendData(data)
    res_data  = json.loads(res_data)
    if not res_data:
        return "There isn't open transactions"
    return generateMessage(res_data)

def generateMessage(res_data):
    message = ""
    for transaction_id, data in res_data.iteritems():
        message += "Transaction " + str(transaction_id) + '\n'
        message += "\tSymbol: " + data[sad._JSON_SYMBOL_] + '\n'
        message += "\tFunction: " + data[sad._JSON_FUNCTION_] + '\n'
        message += "\tState: " + data[sad._JSON_STATE_] + '\n'
        message += "\tQuantity: " + str(data[sad._JSON_QUANTITY_]) + '\n'
        message += "\tEntry Order:" + '\n'
        message += "\t\tPrice: " + str(data[sad._JSON_ENTRY_]) + '\n'
        message += "\t\tState: " + data[sad._JSON_ENTRY_STATE_] + '\n'
        message += "\tLose Order:" + '\n'
        message += "\t\tPrice: " + str(data[sad._JSON_LOSE_]) + '\n'
        message += "\t\tState: " + data[sad._JSON_LOSE_STATE_] + '\n'
        message += "\tProfit Order:" + '\n'
        message += "\t\tPrice: " + str(data[sad._JSON_PROFIT_]) + '\n'
        message += "\t\tState: " + data[sad._JSON_PROFIT_STATE_] + '\n'
    return message
