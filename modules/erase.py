from ravegen import *
import sad
import bm_client

@Command(description="Cancel Transaction", passArgs=True)
def cancel(bot, update, args):
    #args = message.split()
    if not bm_client.verifyAdmin(update):
        update.effective_message.reply_text("You don't have permissions")
        return
    message = generateData(args, sad._CANCEL_OPERATION_TYPE_)
    update.effective_message.reply_text(message)
    #return generateData(args, sad._CANCEL_OPERATION_TYPE_)

@Command(description="Disable Transaction", passArgs=True)
def disable(bot, update, args):
    #args = message.split()
    if not bm_client.verifyAdmin(update):
        update.effective_message.reply_text("You don't have permissions")
        return
    message = generateData(args, sad._DISABLE_OPERATION_TYPE_)
    update.effective_message.reply_text(message)
    #return generateData(args, sad._DISABLE_OPERATION_TYPE_)

def generateData(args, oper_type):
    if len(args) < 1:
        return "Arguments missing <transaction_id>"
    if len(args) > 1:
        return "Only 1 argument <transaction_id>"
    data = {}
    data[sad._JSON_OPERATION_TYPE_] = oper_type
    data[sad._JSON_TRANSACTION_ID_] = int(args[0])
    return bm_client.sendData(data)
