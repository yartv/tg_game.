import os
import json
import telebot
import time
from random import randint
TOKEN = '1272008435:AAFaT8lTzF2cmHFqufDnbRPKw_cnqQcnyG8'
keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
yes_btn = telebot.types.KeyboardButton(text='да')
no_btn = telebot.types.KeyboardButton(text='нет')
keyboard.add(yes_btn, no_btn)

xolodilnik = 0
heal = 80
golod = 75
time_day = 120
med = 1
money = 20
sujet = 0
dedline_heal = 1
fight_heal = 1
dedline_attak = randint(1,3)
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, text='ты думаешь что сможешь выйграть?', reply_markup=keyboard)
 
@bot.message_handler(content_types= ['text'])
def send_text(message):
    global xolodilnik
    global heal
    global golod
    global time_day
    global med
    global money
    global sujet
    global dedline_heal
    global fight_heal
    global dedline_attak
    if message.text.lower() in ['да']:
        bot.send_message(message.chat.id, 'хах')
    if message.text.lower() in ['нет']:
        keyboard2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        start_btn = telebot.types.KeyboardButton(text='начинай')
        rools_btn = telebot.types.KeyboardButton(text='правила')
        sik_sik_btn = telebot.types.KeyboardButton(text='мне страшно')
        keyboard2.add(start_btn, rools_btn, sik_sik_btn)
        bot.send_message(message.chat.id, 'думаю это тебе не помешает', reply_markup=keyboard2)
    if message.text.lower() in ['начинай']:
        keyboard3 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        ofiget_btn = telebot.types.KeyboardButton(text='офигеть')
        prosnytsya_btn = telebot.types.KeyboardButton(text='проснуться')
        deistvie_btn = telebot.types.KeyboardButton(text='включить адблок, вслед рассказать...')
        keyboard3.add(ofiget_btn, prosnytsya_btn, deistvie_btn)
        bot.send_message(message.chat.id, 'обычное утро')
        time.sleep(2)
        bot.send_message(message.chat.id, 'ты бежишь по полосе препятствий, но вдруг...')
        time.sleep(2)
        bot.send_message(message.chat.id, 'выбегают бабки из общественного транспорта с гранатометами чтобы припомнить тебе как ты не уступал им место')
        time.sleep(1)
        bot.send_message(message.chat.id, 'а еще прилетает вертолет из которого в тебя стреляют рекламой шампуня "жумайсынба"')
        time.sleep(1)
        bot.send_message(message.chat.id, 'а из под земли вылазиют разумные сосиски которые рассказывают тебе анекдоты про политику')
        bot.send_message(message.chat.id, 'твои дейсвия', reply_markup=keyboard3)
    if message.text.lower() in ['офигеть']:
        bot.send_message(message.chat.id, 'ага, офигеть здесь есть кнопка для офигевания, а теперь уже выбери что нибудь другое')
    if message.text.lower() in ['проснуться']:
        bot.send_message(message.chat.id, 'ну не знаю, я б не отказывался от такого сна')
        keyboard6 = telebot.types.ReplyKeyboardMarkup(resize_keyboard= True, one_time_keyboard= True)
        kushat_btn = telebot.types.KeyboardButton(text='поесть')
        ymitsya_btn = telebot.types.KeyboardButton(text='умыться')
        pofig_btn = telebot.types.KeyboardButton(text='полежать')
        keyboard6.add(kushat_btn, ymitsya_btn, pofig_btn)
        bot.send_message(message.chat.id, 'и что ты теперь будешь делать?', reply_markup= keyboard6)
    if message.text.lower() in ['поесть']:
        bot.send_message(message.chat.id, 'кушать нечего - ты программист')
    if message.text.lower() in ['умыться'] and not message.text.lower() in ['ладно']:
        bot.send_message(message.chat.id, 'вот и все пора работать')
        while True:
            keyboard8 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            magaz_btn = telebot.types.KeyboardButton(text= 'магазин')
            rabota_btn = telebot.types.KeyboardButton(text= 'работать')
            poest_btn = telebot.types.KeyboardButton(text= 'еда')
            med_btn = telebot.types.KeyboardButton(text= 'лекарства')
            keyboard8.add(magaz_btn, rabota_btn, poest_btn, med_btn)
            time_day -= 1
            golod = golod - 15
            if golod < 20 and golod > 0:
                time.sleep(2)
                heal = heal - 3
            elif golod == 0 or golod < 0:
                time.sleep(2)
                heal = heal - 10
            if heal < 0:
                bot.send_message(message.chat.id, 'вы умерли')
                break
            if golod < -50:
                bot.send_message(message.chat.id, 'вы умерли от голода')
                break
            if time_day <= 0:
                bot.send_message(message.chat.id, 'вы не успели')
                break
            if sujet >= 6:
                bot.send_message(message.chat.id, 'у тебя получилось')
                break

            bot.send_message(message.chat.id, f'статистика: голод: {golod}, здоровье: {heal}, деньги: {money}$, холодильник: {xolodilnik}, аптечка: {med}', reply_markup=keyboard8)
            time.sleep(35)


    if message.text.lower() in ['магазин']:
        bot.send_message(message.chat.id, 'ассортимент: 1 - еда, 2 - лекарства')
        bot.send_message(message.chat.id, '20$ еда, 30$ лекарства')
    if message.text.lower() in ['1']:
        bot.send_message(message.chat.id, 'вы успешно приобрели товар')
        xolodilnik += 1
        money -= 20
    if message.text.lower() in ['2']:
        bot.send_message(message.chat.id, 'вы успешно приобрели товар')
        med += 1
        money -= 30
    if message.text.lower() in ['работать']:
        keyboard9 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        pomosh_btn = telebot.types.KeyboardButton(text= 'помощь')
        sujet_btn = telebot.types.KeyboardButton(text= 'сюжет')
        podrobotka_btn = telebot.types.KeyboardButton(text= 'подработка')
        keyboard9.add(pomosh_btn, sujet_btn, podrobotka_btn)
        bot.send_message(message.chat.id, 'выберите действие', reply_markup= keyboard9)
    if message.text.lower() in ['помощь']:
        bot.send_message(message.chat.id, 'есть сюжетные задания за которые ты ничего не получаешь, и собственно проходишь игру, но тебе нужно уложться в полтора часа')
        time.sleep(2)
        bot.send_message(message.chat.id, 'в побочных ты зарабатываешь деньги на пропитание и лекарства')
        time.sleep(2)
        bot.send_message(message.chat.id, 'работа представляет собой викторину где ты пишешь правельный ответ и получаешь деньги или продвигаешься по сюжету')
        time.sleep(2)
        bot.send_message(message.chat.id, 'нажми shift + enter чтобы сделать отступ')
    if message.text.lower() in ['сюжет']:
        bot.send_message(message.chat.id, '1) распечатайте "hello world"')
        bot.send_message(message.chat.id, '2) создайте переменную x чтобы она равнялась 10')
        bot.send_message(message.chat.id, '3) сделайте преременную x строковой')
        bot.send_message(message.chat.id, '4) сделайте функцию func которая ничего не делает')
        bot.send_message(message.chat.id, '5) создайте класс test в котором функция func которая ничего не делает')
        bot.send_message(message.chat.id, '6) сделайте бесконечный цикл который ничего не делает')
    
    if message.text.lower() in ["print('hello world')"]:
        bot.send_message(message.chat.id, 'дальше')
        sujet +=1
        bot.send_message(message.chat.id, f'{sujet} из 6')
    if message.text.lower() in ["x = 10"]:
        bot.send_message(message.chat.id, 'дальше')
        sujet +=1
        bot.send_message(message.chat.id, f'{sujet} из 6')
    if message.text.lower() in ["x = str(x)"]:
        bot.send_message(message.chat.id, 'дальше')
        sujet +=1
        bot.send_message(message.chat.id, f'{sujet} из 6')
    if message.text.lower() in ["def func():\npass"]:
        bot.send_message(message.chat.id, 'дальше')
        sujet +=1
        bot.send_message(message.chat.id, f'{sujet} из 6')
    if message.text.lower() in ["class test:\ndef func():\npass"]:
        bot.send_message(message.chat.id, 'дальше')
        sujet +=1
        bot.send_message(message.chat.id, f'{sujet} из 6')
    if message.text.lower() in ["while True:\npass"]:
        bot.send_message(message.chat.id, 'дальше')
        sujet +=1
        bot.send_message(message.chat.id, f'{sujet} из 6')

    if message.text.lower() in ['подработка']:
        chislo = randint(1,6)
        if chislo == 1:
            bot.send_message(message.chat.id, '2+2*2')
    
        if chislo == 2:
            bot.send_message(message.chat.id, '11*11')

        if chislo == 3:
            bot.send_message(message.chat.id, '56 / 8')

        if chislo == 4:
            bot.send_message(message.chat.id, "print('2*2') напиши ответ")

        if chislo == 5:
            bot.send_message(message.chat.id, "print('help'):")

        if chislo == 6:
            bot.send_message(message.chat.id, "8 + 9")

    if message.text.lower() in ['6']:
        bot.send_message(message.chat.id, 'правильно')
        money += 30
    

    if message.text.lower() in ['121']:
        bot.send_message(message.chat.id, 'правильно')
        money += 20


    if message.text.lower() in ['7']:
        bot.send_message(message.chat.id, 'правильно')


    if message.text.lower() in ['2*2']:
        bot.send_message(message.chat.id, 'правильно')
        money += 40


    if message.text.lower() in ["print('help')"]:
        bot.send_message(message.chat.id, 'правильно')
        money += 60


    if message.text.lower() in ["17"]:
        bot.send_message(message.chat.id, 'правильно')
        money += 10


    if message.text.lower() in ['еда'] and xolodilnik >= 1:
        golod += 30
        xolodilnik -= 1
        bot.send_message(message.chat.id, 'вы покушали')
    if message.text.lower() in ['лекарства'] and med >= 1:
        heal += 20
        med -= 1
        bot.send_message(message.chat.id, 'вам стало лучше')

    if sujet >= 6:
        bot.send_message(message.chat.id, 'у вас получилось')
        bot.send_message(message.chat.id, 'вы прошли игру')

    if message.text.lower() in ['полежать']:
        bot.send_message(message.chat.id, 'куда лежать иди работай')


    if message.text.lower() in ['включить адблок, вслед рассказать...']:
        keyboard4 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        gulyat_btn = telebot.types.KeyboardButton(text='прогуляться')
        zabegalovka_btn = telebot.types.KeyboardButton(text='сходить покушать')
        ne_prosnutsya_btn = telebot.types.KeyboardButton(text='проснуться2')
        keyboard4.add(gulyat_btn, zabegalovka_btn, ne_prosnutsya_btn)
        bot.send_message(message.chat.id, ' ты включил адблок, вслед рассказал анекдот про евреев, а чтоб бабки отстали включил гимн СССР')
        bot.send_message(message.chat.id, 'ты героически отбился от бабок, и все что тебе сейчас хочется это пельмешек', reply_markup=keyboard4)
    if message.text.lower() in ['проснуться2']:
        bot.send_message(message.chat.id, 'не получается, похоже ты не спишь')
    if message.text.lower() in ['сходить покушать']:
        bot.send_message(message.chat.id, 'ты занимаешь место, но оно уже забронировано,и из-за этого на тебя напали официантки убийцы')
        time.sleep(1)
        keyboard5 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        ladno_btn = telebot.types.KeyboardButton(text='ладно')
        nea_btn = telebot.types.KeyboardButton(text='неа')
        keyboard5.add(ladno_btn, nea_btn)
        bot.send_message(message.chat.id, 'но тебя спас администратор макдональса ценой своего бургера, в этой битве вы победили, перед вами выбор: будите платить чаевые?', reply_markup= keyboard5)
    if message.text.lower() in ['ладно']:
        bot.send_message(message.chat.id, 'вы задобрили официанток')
        bot.send_message(message.chat.id, 'дальше вы вышли из кафе, но то с чем вам прийдется столкнуться выходит за все рамки понимания')
        bot.send_message(message.chat.id, 'вы встретили его - "дедлайн"')
        time.sleep(2)
        keyboard10 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        ataka = telebot.types.KeyboardButton(text= 'удар')
        ataka2 = telebot.types.KeyboardButton(text= 'блок')
        ataka3 = telebot.types.KeyboardButton(text= 'супер удар')
        keyboard10.add(ataka, ataka2, ataka3)
        bot.send_message(message.chat.id, 'дедлайн - защита 2000, сила 10, но если ты не успеешь то тебе хана', reply_markup= keyboard10)
    if message.text.lower() in ['удар'] and dedline_attak == 3:
        dedline_heal -= 1
        bot.send_message(message.chat.id, 'вы провели удачную атаку')
        bot.send_message(message.chat.id, f'ваши жизни: {fight_heal}, жизнь босса: {dedline_heal}')
    if message.text.lower() in ['удар'] and dedline_attak == 2:
        bot.send_message(message.chat.id, 'дедлайн блокировал атаку')
        bot.send_message(message.chat.id, f'ваши жизни: {fight_heal}, жизнь босса: {dedline_heal}')
    if message.text.lower() in ['удар'] and dedline_attak == 1:
        bot.send_message(message.chat.id, 'ничья')
        bot.send_message(message.chat.id, f'ваши жизни: {fight_heal}, жизнь босса: {dedline_heal}')
    
    if message.text.lower() in ['блок'] and dedline_attak == 1:
        bot.send_message(message.chat.id, 'ты блокировал удар')
        bot.send_message(message.chat.id, f'ваши жизни: {fight_heal}, жизнь босса: {dedline_heal}')
    if message.text.lower() in ['блок'] and dedline_attak == 2:
        bot.send_message(message.chat.id, 'ничья')
        bot.send_message(message.chat.id, f'ваши жизни: {fight_heal}, жизнь босса: {dedline_heal}')
    if message.text.lower() in ['блок'] and dedline_attak == 3:
        bot.send_message(message.chat.id, 'твой блок пробит')
        fight_heal -= 1
        bot.send_message(message.chat.id, f'ваши жизни: {fight_heal}, жизнь босса: {dedline_heal}')
    
    if message.text.lower() in ['супер удар'] and dedline_attak == 1:
        bot.send_message(message.chat.id, 'дедлайн сумел тебя ударить')
        fight_heal -= 1
        bot.send_message(message.chat.id, f'ваши жизни: {fight_heal}, жизнь босса: {dedline_heal}')
    if message.text.lower() in ['супер удар'] and dedline_attak == 2:
        bot.send_message(message.chat.id, 'ты пробил блок дедлайна')
        dedline_heal -= 1
        bot.send_message(message.chat.id, f'ваши жизни: {fight_heal}, жизнь босса: {dedline_heal}')
    if message.text.lower() in ['супер удар'] and dedline_attak == 3:
        bot.send_message(message.chat.id, 'ничья')
        bot.send_message(message.chat.id, f'ваши жизни: {fight_heal}, жизнь босса: {dedline_heal}')
    
    if fight_heal <= 0:
        bot.send_message(message.chat.id, 'ты проиграл')

    if dedline_heal <= 0:
        bot.send_message(message.chat.id, 'ты одолел его')

    if message.text.lower() in ['неа']:
        bot.send_message(message.chat.id, 'ты очень злой, и за это тебя отпинали все рабочие кафе')
    if message.text.lower() in ['правила']:
        keyboard2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        start_btn = telebot.types.KeyboardButton(text='начинай')
        rools_btn = telebot.types.KeyboardButton(text='правила')
        sik_sik_btn = telebot.types.KeyboardButton(text='мне страшно')
        bot.send_message(message.chat.id, 'следуешь инструкциям, нажимаешь кнопки, в чат фигню не пиши, создатель ленивый, поэтому что нибудь может пойти не так', reply_markup=keyboard2)
    if message.text.lower() in ['мне страшно']:
        bot.send_message(message.chat.id, 'поздравляю, ты проиграл')

    if message.text.lower() in ['qwaszx']:
        bot.send_message(message.chat.id, 'приветствую, создатель')
bot.polling()