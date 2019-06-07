from ravegen import *

@RaveGen
@Command
def buttons(message):
	menu = [[('Hello', 'command::caps, args::Hello World'), ('GitHub', 'url::https://github.com/ChrisChV')], [('Test me', 'function::funcTest, message::Test:, num::10')]]
	return 'This is a test of buttons:', menu

@RaveGen
@RaveFunction
def funcTest(message, num):
	num = int(num)
	for _ in range(0,num):
		message += 'O'
	return message
