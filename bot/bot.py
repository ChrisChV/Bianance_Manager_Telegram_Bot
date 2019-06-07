#HEADERS
#TokenFlag False
import sys
import os
from telegram.ext import Updater
import ravegen.Decorators.functionManager as functionManager
sys.path.insert(0, '.')
import modules
import logging
from telegram import Update
from flask import Flask, request

app = Flask(__name__)
global updater
global TOKEN
TOKEN = '785072582:AAEV8CLcSI3S7j4x7ImaXUEuoC8ldE_8LgI'
updater = Updater(TOKEN)

@app.route('/785072582:AAEV8CLcSI3S7j4x7ImaXUEuoC8ldE_8LgI', methods=['POST'])
def webhook_handler():
	if request.method == 'POST':
		logging.info(request.get_json(force=True))
		update = Update.de_json(request.get_json(force=True), updater.bot)
		updater.dispatcher.process_update(update)
	return 'ok'


@app.route('/set_webhook', methods=['GET', 'POST'])
def set_webhook():
	dispatcher = updater.dispatcher
	functionManager.functionManager.generateHandlers(dispatcher)
	s = updater.bot.setWebhook('https://bm-telegram-bot.appspot.com/785072582:AAEV8CLcSI3S7j4x7ImaXUEuoC8ldE_8LgI')
	if s:
		return 'webhook setup ok'
	else:
		return 'webhook setup failed'


@app.route('/')
def index():
	return 'Hello World'
