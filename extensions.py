import telebot
import requests
from bs4 import BeautifulSoup    # для упорядоченного получения данных с сервера сайта
from time import sleep    # что бы не перегружать сервер


geldwechsel = {'💸 Рубль': 'RUB',
               '💵 Доллар': 'USD',
               '💶 Евро': 'EUR'}

bot = telebot.TeleBot('5886981757:AAFAVKKKMAZdBNBsXPhavYpBFtkTwMMswXo')

@bot.message_handler(commands=['start'])    # ответ на комманды с обращение по имени пользователя
def repeat(message: telebot.types.Message):
    name_user = f"Здравствуйте <b><u>{message.chat.username}</u></b>. Я бот, " \
                f"С помощью меня Вы можете узнать курс основной мировой валюты по Центробанку - Доллара и Евро. " \
                f"Так же конвертировать валюту: доллары в рубли, евро в рубли, рубли в доллары, рубли в евро, " \
                f"доллары в евро, евро в доллары"    # курсив(<b></b>), подчеркивание(<u></u>)
    sleep(3)
    bot.send_message(message.chat.id, name_user, parse_mode='html')    # с ответом определенному пользователю
    sleep(2)
    bot.send_message(message.chat.id, "<b>Основные команды: </b>", parse_mode='html')
    bot.send_message(message.chat.id, f"/start - приветствие, список основных команд, правило конвертации")
    bot.send_message(message.chat.id, f"/валюта - волюта доступная для конвертации")
    bot.send_message(message.chat.id, f"/доллар - курс доллара")
    bot.send_message(message.chat.id, f"/евро - курс евро")
    sleep(2)
    bot.send_message(message.chat.id, f"Пример конвертации: ")
    sleep(2)
    bot.send_message(message.chat.id, f"1 рубль долларов")
    bot.send_message(message.chat.id, f"2-4 рубля долларов")
    bot.send_message(message.chat.id, f"5 или больше рублей: 5 рублей долларов")
    bot.send_message(message.chat.id, f"1 рубль евро")
    bot.send_message(message.chat.id, f"2-4 рубля евро")
    bot.send_message(message.chat.id, f"5 или больше рублей: 5 рублей евро")

@bot.message_handler(commands=['валюта'])    # показ имеющейся валюты для обмена
def values(message: telebot.types.Message):
    text = '⚖ Доступная валюта для обмена ⚖'
    for geld in geldwechsel.keys():
        text = '\n'.join((text, geld))
    bot.reply_to(message, text)    # отправляем в ответ письмо прикрепленное к команде

@bot.message_handler(commands=['доллар'])
def usd(message: telebot.types.Message):
    d = f'💵 {USD_1} {USD} {round_USD_course} рублей.'
    bot.reply_to(message, d)

@bot.message_handler(commands=['евро'])
def eur(message: telebot.types.Message):
    e = f'💶 {EUR_1} {EUR} {round_EUR_course} рублей.'
    bot.reply_to(message, e)

@bot.message_handler(content_types=['text'])
def converter(message: telebot.types.Message):
    try:
        amount, geld, geld_2 = message.text.split()
        geld = str(geld)
        geld_2 = str(geld_2)
        amount = int(amount)

        if amount == 1 and geld == 'доллар' and geld_2 == 'рублей':
            r = float(USD_course) * int(amount)
            r = round(r, 1)
            bot.send_message(message.chat.id, f"💵{int(amount)} доллар равен {r} 💸pублей")
        elif 2 <= amount <= 4 and geld == 'доллара' and geld_2 == 'рублей':
            r = float(USD_course) * int(amount)
            r = round(r, 1)
            bot.send_message(message.chat.id, f"💵{int(amount)} доллара равны {r} 💸pублям")
        elif 5 <= amount and geld == 'долларов' and geld_2 == 'рублей':
            r = float(USD_course) * int(amount)
            r = round(r, 1)
            bot.send_message(message.chat.id, f"💵{int(amount)} долларов равны {r} 💸pублям")

        elif amount == 1 and geld == 'евро' and geld_2 == 'рублей':
            r = float(EUR_course) * int(amount)
            r = round(r, 1)
            bot.send_message(message.chat.id, f"💶{int(amount)} евро равен {r} 💸pублям")
        elif 5 <= amount and geld == 'евро' and geld_2 == 'рублей':
            r = float(EUR_course) * int(amount)
            r = round(r, 1)
            bot.send_message(message.chat.id, f"💶{int(amount)} евро равны {r} 💸pублям")

        elif amount == 1 and geld == 'рубль' and geld_2 == 'евро':
            e = int(amount) / float(EUR_course)
            e = round(e, 3)
            bot.send_message(message.chat.id, f"💸{int(amount)} рубль равен {e} 💶евро.")
        elif 2 <= amount <= 4 and geld == 'рубля' and geld_2 == 'евро':
            e = int(amount) / float(EUR_course)
            e = round(e, 3)
            bot.send_message(message.chat.id, f"💸{int(amount)} рубля равны {e} 💶евро.")
        elif 5 <= amount and geld == 'рублей' and geld_2 == 'евро':
            e = int(amount) / float(EUR_course)
            e = round(e, 2)
            bot.send_message(message.chat.id, f"💸{int(amount)} рублей равны {e} 💶евро.")

        elif amount == 1 and geld == 'рубль' and geld_2 == 'долларов':
            d = int(amount) / float(USD_course)
            d = round(d, 3)
            bot.send_message(message.chat.id, f"💸{int(amount)} рубль равен {d} 💵доллара.")
        elif 2 <= amount <= 4 and geld == 'рубля' and geld_2 == 'долларов':
            d = int(amount) / float(USD_course)
            d = round(d, 3)
            bot.send_message(message.chat.id, f"💸{int(amount)} рубля равны {d} 💵доллара.")
        elif 5 <= amount and geld == 'рублей' and geld_2 == 'долларов':
            d = int(amount) / float(USD_course)
            d = round(d, 2)
            bot.send_message(message.chat.id, f"💸{int(amount)} рублей равны {d} 💵доллара(-ов).")

        elif amount == 1 and geld == 'доллар' and geld_2 == 'евро':
            e = float(USD_course) / float(EUR_course)
            e = round(e, 3)
            bot.send_message(message.chat.id, f"💵{int(amount)} доллар равен {e} 💶евро.")
        elif 2 <= amount <= 4 and geld == 'доллара' and geld_2 == 'евро':
            e = float(USD_course) / float(EUR_course)
            e = round(e, 3)
            bot.send_message(message.chat.id, f"💵{int(amount)} доллара равны {e} 💶евро.")
        elif 5 <= amount and geld == 'долларов' and geld_2 == 'евро':
            e = float(USD_course) / float(EUR_course)
            e = round(e, 3)
            bot.send_message(message.chat.id, f"💵{int(amount)} долларов равны {e} 💶евро.")

        elif amount == 1 and geld == 'евро' and geld_2 == 'долларов':
            d = float(EUR_course) / float(USD_course)
            d = round(d, 3)
            bot.send_message(message.chat.id, f"💶{int(amount)} евро равен {d} 💵доллара(-ов).")
        elif 5 <= amount and geld == 'евро' and geld_2 == 'долларов':
            d = float(EUR_course) / float(USD_course)
            d = round(d, 3)
            bot.send_message(message.chat.id, f"💶{int(amount)} евро равны {d} 💵долларов.")

        else:
            bot.send_message(message.chat.id, f"Вы не правильно ввели запрос!")
            sleep(1)
            bot.send_message(message.chat.id, f"Вот пример: 1 рубль долларов")
            bot.send_message(message.chat.id, f"2-4 рубля долларов")
            bot.send_message(message.chat.id, f"5 или больше рублей: 5 рублей долларов")
            bot.send_message(message.chat.id, f"1 рубль евро")
            bot.send_message(message.chat.id, f"2-4 рубля евро")
            bot.send_message(message.chat.id, f"5 или больше рублей: 5 рублей евро")

    except ValueError as e:
        bot.send_message(message.chat.id, f"Ошибка в команде:\n{e} ")
        bot.send_message(message.chat.id, f"Вы не правильно ввели запрос!")
        sleep(1)
        bot.send_message(message.chat.id, f"Вот пример: 1 рубль долларов")
        bot.send_message(message.chat.id, f"2-4 рубля долларов")
        bot.send_message(message.chat.id, f"5 или больше рублей: 5 рублей долларов")
        bot.send_message(message.chat.id, f"1 рубль евро")
        bot.send_message(message.chat.id, f"2-4 рубля евро")
        bot.send_message(message.chat.id, f"5 или больше рублей: 5 рублей евро")

url = 'https://www.banki.ru/products/currency/cb/'    # создаем переменную содержащая ссылку на сайт

r = requests.get(url)    # отправляем запрос на сервер с помощью команды get

soup = BeautifulSoup(r.text, 'lxml')    # возвращаем данные с сервера в нормальном виде в формате lxml, с помощью

# библиотеки BeautifulSoup
soup.find('table', class_='standard-table standard-table--row-highlight')    # с помощью метода find, тэг div и class_
# находим определенную информацию на странице сайта

USD_1 = soup.find('table', class_='standard-table standard-table--row-highlight'). \
    find('tbody').findAll('tr')[0].findAll('td')[1].text

USD = soup.find('table', class_='standard-table standard-table--row-highlight'). \
    find('tbody').findAll('tr')[0].findAll('td')[2].find('a').find('strong').text

USD_course = soup.find('table', class_='standard-table standard-table--row-highlight'). \
    find('tbody').findAll('tr')[0].findAll('td')[3].text
round_USD_course = round(float(USD_course), 1)


EUR_1 = soup.find('table', class_='standard-table standard-table--row-highlight'). \
    find('tbody').findAll('tr')[1].findAll('td')[1].text

EUR = soup.find('table', class_='standard-table standard-table--row-highlight'). \
    find('tbody').findAll('tr')[1].findAll('td')[2].find('a').find('strong').text

EUR_course = soup.find('table', class_='standard-table standard-table--row-highlight'). \
    find('tbody').findAll('tr')[1].findAll('td')[3].text
round_EUR_course = round(float(EUR_course), 1)

bot.polling(none_stop=True)    # Запуск бота на постоянной основе