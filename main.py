####--------------------------------####
#--# Author:   by Umbrellla777      #--#
#--# Telegram: @Umbrellla777        #--#
#--# VK:       @Umbrellla777        #--#
####--------------------------------####

###########################
## Импорт библиотек
###########################
import sys
import asyncio
import time
import emoji
import random


from asyncio import sleep
from collections import deque
from telethon.sync import TelegramClient
from telethon import TelegramClient
from telethon import events

##from telethon                       import functions, types
##from telethon.tl.types              import ChatBannedRights
##from telethon.tl.functions.users    import GetFullUserRequest
##from telethon.tl.functions.channels import EditBannedRequest


###########################
## Цвет консоли
###########################
red = [206, 76, 54]
green = [68, 250, 123]
blue = [253, 127, 233]
yellow = [241, 250, 118]
orange = [255, 184, 107]


def colored(color, text):
    return "\033[38;2;{};{};{}m{}\033[38;2;255;255;255m".format(color[0], color[1], color[2], text)


###########################
## Настройки
###########################
api_id = int(sys.argv[1])
api_hash = str(sys.argv[2])

## Connect
client = TelegramClient('users/current_user', api_id, api_hash)
client.start()

###########################
## Импорт папок|добавить
###########################

###########################
## Информация о аккаунте
###########################
entity = client.get_entity("me")
MY_ID = entity.id
print(
    "["
    + colored(green, "PROFILE: ")
    + str(entity.first_name)
    + " | " + colored(orange, "Id: ") + str(MY_ID)
    + " | " + colored(orange, "Uname: ") + "@" + str(entity.username)
    + "]"
)

###########################
## Помощь по командам
###########################
@client.on(events.NewMessage(pattern='.help'))
async def help(event):
    message = event.message
    await message.edit("Привет! Я - бот с анимированными сообщениями. \nСо мной ты сможешь отправить прекрасное анимированное сообщение.\nСписок команд:\n.ping проверка бота на работоспособность.\n.8 анимация - подарок на 8 марта.\n.lv анимация - сердце.\n@all Упоминание всех участников чата.\n.coin Монетка с вариантами выпадения - Орёл, решка, кант.\n.rtext бегущая полоса текста.\n.roll Случайно число между двумя введёными.\n.type Анимация написания текста.\n.moon Пожелание спокойной ночи, со сменой фазы луны.\n.bunny Анимация с кроликом.\n\nТак же команды будут добавляться, следите за новостями в нашем телеграмм канале t.me/umbrellla777bot \n Author Umbrellla777 \n VK @Umbrellla777\n TG @Umbrellla777")


###########################
## Проверка бота
###########################
@client.on(events.NewMessage(pattern='.ping'))
async def pong(event):
    message = event.message
    await message.edit("pong")




##########################
## Анимация .8|5×10
###########################
@client.on(events.NewMessage(pattern='.8'))
async def draw_matrix(event):
    message = event.message
    matrix = '12221\n21112\n21112\n21112\n12221\n21112\n21112\n21112\n21112\n12221'
    end = '00000000\n00000000\n00000000\n0С праздником! 0\n00000000\n00000000\n00000000'

    matrix = matrix.replace('1', '⬜️').replace('2', '⬛️')

    await message.edit(matrix)

    await asyncio.sleep(1)  # Ждем 1 секунду

    matrix = matrix.replace('⬜️', '◻️').replace('⬛️', '◼️')
    await message.edit(matrix)

    await asyncio.sleep(1)  # Ждем 1 секунду

    matrix = matrix.replace('◻️', '◽️').replace('◼️', '◾️')
    await message.edit(matrix)

    await asyncio.sleep(1)  # Ждем 1 секунду

    matrix = matrix.replace('◽️', '▫️').replace('◾️', '▪️')
    await message.edit(matrix)
    
    await asyncio.sleep(1)
    await message.edit('Это твой день!')
    await asyncio.sleep(2)
    await message.edit('Сияй!')
    await asyncio.sleep(2)
    await message.edit('Действуй!')
    await asyncio.sleep(2)
    await message.edit('Нет ничего невозможного!')
    await asyncio.sleep(2)
    await message.edit('Никогда не сдавайся!')
    await asyncio.sleep(2)
    await message.edit('Будь собой!')
    await asyncio.sleep(2)
    await message.edit('✨✨✨✨✨✨✨✨')
    await asyncio.sleep(2)
    await message.edit('И просто...')
    end = end.replace('0', '❤️')
    await asyncio.sleep(2)
    await message.edit(end)
    end = end.replace('❤️', '❤️‍🔥')
    await asyncio.sleep(2)
    await message.edit(end)



##########################
## Анимация .lv
##########################
@client.on(events.NewMessage(pattern=r"\.lv", outgoing=True))
async def watcher(event):
	message = event
	if message.sender_id == (await message.client.get_me()).id:
		arr = ["🟥", "🟧", "🟨", "🟩", "🟦", "🟪", "🟫", "⬛️", "🔳"]
		h = "⬜️"
		first = ""		
		for i in "".join([h*9, "\n", h*2, arr[0]*2, h, arr[0]*2, h*2, "\n", h, arr[0]*7, h, "\n", h, arr[0]*7, h, "\n", h, arr[0]*7, h, "\n", h*2, arr[0]*5, h*2, "\n", h*3, arr[0]*3, h*3, "\n", h*4, arr[0], h*4]).split("\n"):
			first += i + "\n"
			await message.edit(first)
			await sleep(0.2)		
		for i in arr:
			await message.edit("".join([h*9, "\n", h*2, i*2, h, i*2, h*2, "\n", h, i*7, h, "\n", h, i*7, h, "\n", h, i*7, h, "\n", h*2, i*5, h*2, "\n", h*3, i*3, h*3, "\n", h*4, i, h*4, "\n", h*9]))
			await sleep(0.3)
		for _ in range(8):
			rand = random.choices(arr, k=34)
			await message.edit("".join([h*9, "\n", h*2, rand[0], rand[1], h, rand[2], rand[3], h*2, "\n", h, rand[4], rand[5], rand[6], rand[7], rand[8],rand[9],rand[10], h, "\n", h, rand[11], rand[12], rand[13], rand[14], rand[15], rand[16],rand[17], h, "\n", h, rand[18], rand[19], rand[20], rand[21], rand[22], rand[23],rand[24], h, "\n", h*2, rand[25], rand[26], rand[27], rand[28], rand[29], h*2, "\n", h*3, rand[30], rand[31], rand[32], h*3, "\n", h*4, rand[33], h*4, "\n", h*9]))
			await sleep(0.3)
		fourth = "".join([h*9, "\n", h*2, arr[0]*2, h, arr[0]*2, h*2, "\n", h, arr[0]*7, h, "\n", h, arr[0]*7, h, "\n", h, arr[0]*7, h, "\n", h*2, arr[0]*5, h*2, "\n", h*3, arr[0]*3, h*3, "\n", h*4, arr[0], h*4, "\n", h*9])
		await message.edit(fourth)
		for _ in range(47):
			fourth = fourth.replace("⬜️", "🟥", 1)
			await message.edit(fourth)
			await sleep(0.1)
		for i in range(8):
			await message.edit((arr[0]*(8-i)+"\n")*(8-i))
			await sleep(0.4)
		for i in ["I", "I ❤️", "I ❤️ U", "I ❤️ U!",'i ❤️ U', 'I ❤️ u', 'I ❤️ U']:
			await message.edit(f"<b>{i}</b>", parse_mode='html')
			await sleep(0.5)
##########################
## Анимация .rtext
##########################
@client.on(events.NewMessage(pattern=r"\.rtext", outgoing=True))
async def rtext(event):
    if event.fwd_from:
        return
    try:
        txt1 = event.message.message
    except:
        txt1 = event.original_update.message.message

    text = ' '.join(str(txt1).split(' ')[1:])
    deq = deque(list(text))
    for _ in range(len(deq) + 1):
        await asyncio.sleep(0.1)
        try:
            await event.edit(f'''{"".join(deq)}''')
        except:
            pass
        deq.rotate(1)

##########################
## Упоминание @all
##########################
@client.on(events.NewMessage(pattern=r"\@all", outgoing=True))
async def tagallcmd(event):
	global args
	args = ''
	try:
		txt1 = event.message.message
	except:
		txt1 = event.original_update.message.message
	if len(txt1.split(' ')) != 1:
		args = txt1.split(' ')[1]
	global tag_
	tag_ = 10
	notext = False
	if args:
		if args.isdigit():
			tag_ = int(args)

				
	await event.delete()
	chat = await event.get_chat()
	all = client.iter_participants(chat.id)
	chunk = []
	def chunks(lst, n):
		for i in range(0, len(lst), n):
			yield lst[i:i + n]

	notifies = []
	async for user in all:
		notifies.append("<a href=\"tg://user?id="+ str(user.id) +"\">\u206c\u206f</a>")
	chunkss = list(chunks(notifies, tag_))
	await event.delete()
	for chunk in chunkss:
		await client.send_message(chat.id, '\u206c\u206f'.join(chunk), parse_mode='html')
##########################
## Анимация .type
##########################
@client.on(events.NewMessage(pattern=r"\.type", outgoing=True))
async def type(event):
    orig_text = event.raw_text.split(".type ", maxsplit=1)[1]
    text = orig_text
    tbp = ""  # to be printed
    typing_symbol = "▒"

    while tbp != orig_text:
        try:
            await event.edit(tbp + typing_symbol)
            await asyncio.sleep(0.05)  # 50 ms

            tbp = tbp + text[0]
            text = text[1:]

            await event.edit(tbp)
            await asyncio.sleep(0.05)

        except FloodWait as e:
            await asyncio.sleep(e.x)
##########################
## Подкидывание монетки .coin
##########################
@client.on(events.NewMessage(pattern=r"\.coin"))
async def coin_flip(event):
    message = event.message
    await message.edit("Подкидываю монетку...")
    await asyncio.sleep(3)  # Имитация подкидывания
    result = random.choices(["орел", "решка", "кант"], weights=[0.4995, 0.4995, 0.001])[0]  # Вероятность канта 0.1
    await message.edit(f"Ловлю монетку...")
    await asyncio.sleep(3)
    await message.edit(f"Результат: {result}")
##########################
## Случайное число .roll
##########################
@client.on(events.NewMessage(pattern=r"\.roll\s+(\d+)\s+(\d+)"))
async def roll_dice(event):
    message = event.message
    min_num = int(event.pattern_match.group(1))
    max_num = int(event.pattern_match.group(2))
    if min_num > max_num:
        await message.edit("Ошибка: минимальное число больше максимального.")
        return
    result = random.randint(min_num, max_num)
    await message.edit(f"Случайное число между {min_num} и {max_num} (включительно): {result}")
##########################
## Пожелание спокойной ночи со сменой фазы луны .moon
##########################
@client.on(events.NewMessage(pattern=r"\.moon", outgoing=True))
async def moon_animation(event):
    moon_message = event.message
    moon_stickers = ["🌖", "🌗", "🌘", "🌑", "🌒", "🌓", "🌔","🌕"]
    
    await moon_message.edit("Спокойной ночи!🌕")
    for sticker in moon_stickers:
        await asyncio.sleep(0.5)
        await moon_message.edit(f"Спокойной ночи!{sticker}")
##########################
## Анимация кролик и сердечко .bunny
##########################
@client.on(events.NewMessage(pattern=r"\.bunny"))
async def bunny_heart(event):
    message = event.message
    await message.edit("/) /)\n( •. •)\n (  づ🌹 Хочешь розу?")
    await asyncio.sleep(2) 
    await message.edit(f"/) /)\n( •. •)\n (  づ🍓 Может клубничку?)")
    await asyncio.sleep(2)
    await message.edit(f"(\ (\ \n(• .• )\n🍓⊂) Нет, клубничку я сам схомячу!😋")
    await asyncio.sleep(2)
    await message.edit(f"/) /)\n( •. •)\n (  づ❤️ Лучше возьми моё сердечко!")


client.run_until_disconnected()
