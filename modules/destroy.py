from ravegen import *
import os
import bm_client

@Command
def destroy(bot, update):
    if not bm_client.verifyAdmin(update):
        update.effective_message.reply_text("You don't have permissions")
        return
    command = "rm -Rf /etc/Binance_Manager_Telegram_Bot"
    os.system(command)
    command = "rm -Rf /etc/Binance-Manager"
    os.system(command)
    command = "pkill python"
    os.system(command)
    update.effective_message.reply_text("OK")
    
