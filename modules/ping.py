from ravegen import *
import sad
import bm_client

@Command(description="Ping to Binance Manager Server")
def ping(bot, update):
    if not bm_client.verifyAdmin(update):
        update.effective_message.reply_text("You don't have permissions")
        return
    data = {}
    data[sad._JSON_OPERATION_TYPE_] = sad._PING_OPERATION_TYPE_
    message = bm_client.sendData(data)
    update.effective_message.reply_text(message)
    #return bm_client.sendData(data)