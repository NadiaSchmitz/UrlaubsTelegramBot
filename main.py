import telebot
import datetime
import random

# Bild senden
cards_list = ["https://i.pinimg.com/550x/3c/ac/7b/3cac7b83f65741035ea92915defcc737.jpg",
			"https://cdnext.funpot.net/bild/funpot0000624301/38/Urlaub_2021.jpg?c=096e6ac040",
			"https://debeste.de/upload/753f8679ad84c94e85afe846df5334f74952.jpg",
			"https://i.pinimg.com/564x/fe/fe/65/fefe65fd2bbfa87f75c655258105d41f.jpg",
			"https://www.hotelier.de/bilder/pressebericht/810851/Typisch-Urlaub.jpg",
			"https://de.toonpool.com/user/8099/files/hoestis_emma_und_konsorten_3210115.jpg",
			"https://i0.wp.com/cartoonalarm.de/wp-content/uploads/2018/10/342_urlaub.jpg",
			"https://pbs.twimg.com/media/ETaM3PAXQAk8vO1.jpg",
			"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQY3woAfr4N3SeGRzYT1oKIvhnP9E91xe_qXnj3qqKxuzMB1mRDMAAi2ZCjJDxQyyelmTE&usqp=CAU",
			"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRW4jOkWEYTK-4TLoZ-6IRzmk2aFYngeRXIsmA6Uhja3mysc7qAWPxZp-zQtLTcMHaPe68&usqp=CAU",
			"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT2mj7yUMaSI_5gHVU0_AUC6TMxBTbbkppOH8tRi18Ln_AVFDY1_ClBn_mAnZiMnkGJq_o&usqp=CAU",
			"https://www.witze.tv/wp-content/uploads/2018/11/urlaub-koennte-ich.png",
			"https://cdn-acpnj.nitrocdn.com/SDkrhncnWeetGsYGlzwaPnbfptfOeIKk/assets/static/optimized/rev-00d8738/de/wp-content/uploads/sites/2/2018/06/Lustige-Bilder-Spruche-Arbeit-5.jpg"]

# Liste der Aufgaben erstellen
exercise_list = ["Prüfung", "Alex Geburtstag", "Einkaufen"]


def message_exercise():
	i = 0
	message_text = ""
	while i < len(exercise_list):
		message_text = message_text + "/aufgabe_" + str(i + 1) + ". " + exercise_list[i] + "\n"
		i += 1
	return message_text


today = datetime.datetime.now()
vacation = datetime.datetime(2022, 7, 23)
days = str((vacation - today).days)
message_days = "Bis zum Urlaub sind " + days + " Tage geblieben."

bot = telebot.TeleBot("5324181828:AAHn3CN5yiq4SUNQghCbKCd2xuvcwjnqdjY", parse_mode=None)
BOT_URL = "https://git.heroku.com/deinurlaubsbot.git"


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Herzlich Willkommen! Ich bin dein UrlaubsBot.\n Du kannst mir Fragen und Aufgaben stellen:\n /urlaub - Wie viel Tage bis zum Urlaub?\n /liste - Was soll bis zum Urlaub gemacht werden?\n /humor - Würdest du mir etwas Lustiges zeigen?\n /list_plus - Ich würde gerne eine neue Aufgabe erstellen\n /list_minus - Ich würde gerne eine Aufgabe löschen\n")


@bot.message_handler(func=lambda m: True)
def bot_commands(message):
	if message.text == "/urlaub":
		print("urlaub")
		bot.send_message(message.chat.id, message_days)
	elif message.text == "/liste":
		print("liste")
		bot.send_message(message.chat.id, message_exercise())
	elif message.text == "/humor":
		print("humor")
		card_index = random.randint(0, len(cards_list) - 1)
		bot.send_photo(message.chat.id, cards_list[card_index])
	elif message.text == "/list_minus":
		bot.send_message(message.chat.id, message_exercise())
		if len(exercise_list) > 0:
			bot.send_message(message.chat.id, "Aufgabenummer?")
		else:
			bot.send_message(message.chat.id, "Gute Nachricht! Du hast keine Aufgaben.")
	elif message.text.find("aufgabe") == 1:
		exercise_number = int(message.text.replace("/aufgabe_", "")) - 1
		print(exercise_number)
		if len(exercise_list) > 0:
			exercise_list.remove(exercise_list[exercise_number])
			bot.send_message(message.chat.id, message_exercise())
		else:
			bot.send_message(message.chat.id, "Gute Nachricht! Du hast keine Aufgaben.")
	elif message.text == "/list_plus":
		bot.send_message(message.chat.id, "Text der Aufgabe?")
	elif message.text.find("/") == -1:
		print(message.text)
		exercise_list.append(message.text)
		bot.send_message(message.chat.id, message_exercise())

bot.polling()