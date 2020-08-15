from __future__ import print_function
from telethon import TelegramClient, sync, events
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
from telethon.errors import SessionPasswordNeededError
from telethon.errors import FloodWaitError
import sys, os,time

#-----Check folder-----#
os.system("clear")
if not os.path.exists("session"):
	os.mkdir("session")

#-----Login Telegram----#
print('Please Login: ')
print
api_id = 1752454   #Don't Edit !!
hash_id = "851e8463de239f1deab123e1c428dee1"  #Don't Edit !!!
telpon = str(input('Input Your Number (use +): '))
client = TelegramClient("session/"+telpon, api_id, hash_id)
client.connect()
if not client.is_user_authorized():
	try:
		client.send_code_request(telpon)
		user = client.sign_in(telpon, input("Input Code OTP: "))
	except SessionPasswordNeededError:
		password = input("Please input Your Password 2FA: ")
		user = client.sign_in(telpn, password)
print
print('----Login Success----')
time.sleep(3)
os.system('clear')
info = client.get_me()
print
os.system("figlet -w 100  Bradz")
print
print("Contact:email - dimasiqball087@gmail.com")
print("	Telegram - t.me/bradz_rezpector")
print
print("Donate : LTC - MAxq16v6ZuyCdvh6jhTcsj6ACgzKitHkXh")
print(" Script v.1.0")
print("-------------------")
print("Username: ",info.username)
print("ID	: ",info.id)
print("Phone	: ",telpon)
print("-------------------")

#----Get Channel----
channel_username = '@freelite_coin_bot'
channel_entity = client.get_entity(channel_username)
i=0
while True:
	i+=1
	client.send_message(entity=channel_entity, message='💥 litecoin Bonus')
	msg = client(GetHistoryRequest(
				peer=channel_entity,
				limit=999,
				offset_date=None,
				offset_id=0,
				max_id=0,
				min_id=0,
				add_offset=0,
				hash=0))

	total=65
	while True:
		print(i,"Please Wait... ",total,end='\r')
		total -=1
		time.sleep(1)
		if total == -1:
			print(end='\n')
			break

