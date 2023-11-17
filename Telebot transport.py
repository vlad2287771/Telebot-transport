import telebot
#transportbot

bot = telebot.TeleBot("5855984332:AAHAtndgjlOSs7peqmrV_J2N2UbfGwHl0nA")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	b = 0
	bus = '24, 25, 27, 28, 36, 37, 43, 50, 54, ' \
		  '57, 57а, 58, 59, 60, 61, 65, 69, 71, 75, 76, 85, 88, ' \
		  '90, 91, 91м, 95, 96, 97, 99'.split(
		', ')
	tram = '1, 2, 3, 4, 5, 5а, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 32, 33, 34'.split(
		', ')
	trolleybus = '1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 33'.split(', ')
	minibus = '53, 68, 80, 81, 09, ' \
			  '44, 48, 92, 047, 053, ' \
			  '05, 012, 019, 26, 46, ' \
			  '06, 014, 56, 73, 082, 083, ' \
			  '40, 12, 38, 042, 070, ' \
			  '016, 030, 42, 052, 94, 077, ' \
			  '45, 63, 056, 054, 79'.split(
		', ')
	for number in bus:
		if number == message.text:
			b += 1
			answer = "Автобус "
		if b == 0:
			answer = ""
	for number in tram:
		if number == message.text:
			b += 1
			answer += "Трамвай "
		if b == 0:
			answer = ""
	for number in trolleybus:
		if number == message.text:
			b += 1
			answer += "Троллейбус "
		if b == 0:
			answer = ""
	for number in minibus:
		if number == message.text:
			b += 1
			answer += "Маршрутка "
		if b == 0:
			answer = ""
	if b == 0:
		answer = "Нет маршрута"

	bot.send_message(message.chat.id, answer)

bot.infinity_polling()