
from re import I
import telebot
import requests
import json



bot=telebot.TeleBot('6216105741:AAHYPjHGyC-DxIoV-26VvaZdtyLIq-aemUU')
API='a183cbd14041cc461d16dccafe6d1860'


@bot.message_handler(commands=['start'])
def start(message):
    mess=u''f'Привіт,<b>{message.from_user.first_name}<u>{message.from_user.last_name}, Введи місто</u></b>'
    bot.send_message(message.chat.id,mess,parse_mode='html')


@bot.message_handler(content_types=['text'])
def get_weaser(message):
    city=message.text.strip().lower()
    res=requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    
    if res.status_code==200:
        data=json.loads(res.text)
        w=(data["weather"])
        json_formatted_str = json.dumps(w)
        q=(json_formatted_str[-7:-1])
        image=''
        if q=='"01d"}' or q=='"01n"}':
            image='01d2x.png'
        elif q=='"02d"}' or q=='"02n"}':
            image='02d2x.png'
        elif q=='"03d"}' or q=='"03n"}':
            image='03d2x.png'
        elif q=='"04d"}' or q=='"04n"}':
            image='04d2x.png'
        elif q=='"09d"}' or q=='"09n"}':
            image='02d2x.png'
        elif q=='"10d"}' or q=='"10n"}':
            image='10d2x.png'
        elif q=='"11d"}' or q=='"11n}"':
            image='11d2x.png'
        elif q=='"13d"}' or q=='"13n"}':
            image='13d2x.png'
        elif q=='"50d"}' or q=='"50n"}':
            image='50d2x.png'
        else:
            image='04d2x.png'
        bot.reply_to(message, f'Температура: {data["main"]["temp"]},')
        bot.send_photo(message.chat.id, photo=open ('./'+image,'rb'))
    else:
         bot.reply_to(message, f'Місто не існує')
    

def new_func(data):
    pg=data["weather"]["id"]
    return pg
bot.polling(none_stop=True)
