from telegram.ext import *
from telegram import *
from twilio.rest import Client
from pymongo import MongoClient
from datetime import datetime
import json

import add
import call
import buy
import update

cluster = MongoClient("mongodb+srv://TOP:TOPSMS@bot.kqphwt1.mongodb.net/?retryWrites=true&w=majority")
db = cluster["users"]
collection = db["users"]

with open("config.json", "r") as jsonfile:
    data = json.load(jsonfile)
    token = data['tokenbot']
    account_sid = data['twiliosid']
    auth_token = data['twilioauth']
    ngrok = data['ngrok']

cluster = MongoClient("mongodb+srv://TOP:TOPSMS@bot.kqphwt1.mongodb.net/?retryWrites=true&w=majority")
db = cluster["users"]
collection = db["users"]

def checkdate(chatid):
    cursor = collection.find({'chat_id': f'{chatid}'})
    for doc in cursor:
        duration = doc['duration']
        if duration == "1Day":

            expirationhour = doc['expirationdate']
            hh = int(str(expirationhour).split(':')[0])
            mm = int(str(expirationhour).split(':')[1])
            ss = int(str(expirationhour).split(':')[2])
            formula = int(hh) * 3600 + int(mm) * 60 + ss
            now = datetime.now().strftime("%H:%M:%S")
            nowhh = now.split(':')[0]
            nowmm = now.split(':')[1]
            nowss = now.split(':')[2]
            formula1 = int(nowhh) * 3600 + int(nowmm) * 60 + int(nowss)
            if formula - formula1 >= 0:
                return True
                print(formula1 - formula)

            else:
                
                return False
        elif duration == "1Week":
            expirationdate = doc['expirationdate']
            dd = int(str(expirationdate).split('/')[0])
            m = int(str(expirationdate).split('/')[1])
            yy = int(str(expirationdate).split('/')[2])
            formula = int(yy) + int(m) + dd
            noww = datetime.now().strftime('%d/%m/%Y')
            nowdd = int(str(noww).split('/')[0])
            nowm = int(str(noww).split('/')[1])
            nowyy = int(str(noww).split('/')[2])

            formula1 = int(nowyy) + int(nowm) + int(nowdd)
            dt1 = datetime(yy,m,dd)
            dt2 = datetime(yy,nowm,nowdd)
            tdelta = dt2 - dt1 
            if str(tdelta) == "7 days, 0:00:00":
                print(tdelta)
            elif str(tdelta) == '0:00:00':
                return True
            elif '-' in str(tdelta):
                return False 
            else:
                return True
        elif duration == "1Month":
            expirationdate = doc['expirationdate']
            dd = int(str(expirationdate).split('/')[0])
            m = int(str(expirationdate).split('/')[1])
            yy = int(str(expirationdate).split('/')[2])
            formula = int(yy) + int(m) + dd
            noww = datetime.now().strftime('%d/%m/%Y')
            nowdd = int(str(noww).split('/')[0])
            nowm = int(str(noww).split('/')[1])
            nowyy = int(str(noww).split('/')[2])

            formula1 = int(nowyy) + int(nowm) + int(nowdd)
            dt1 = datetime(yy,m,dd)
            dt2 = datetime(yy,nowm,nowdd)
            tdelta = dt2 - dt1 
            if str(tdelta) == "30 days, 0:00:00":
                print(tdelta)
            elif str(tdelta) == '0:00:00':
                return True
            elif '-' in str(tdelta):
                return False 
            else:
                return True
        elif duration == "1Year":
            expirationdate = doc['expirationdate']
            dd = int(str(expirationdate).split('/')[0])
            m = int(str(expirationdate).split('/')[1])
            yy = int(str(expirationdate).split('/')[2])
            formula = int(yy) + int(m) + dd
            noww = datetime.now().strftime('%d/%m/%Y')
            nowdd = int(str(noww).split('/')[0])
            nowm = int(str(noww).split('/')[1])
            nowyy = int(str(noww).split('/')[2])

            formula1 = int(nowyy) + int(nowm) + int(nowdd)
            dt1 = datetime(yy,m,dd)
            dt2 = datetime(yy,nowm,nowdd)
            tdelta = dt2 - dt1 
            if str(tdelta) == "365 days, 0:00:00":
                print(tdelta)
            elif str(tdelta) == '0:00:00':
                return True
            elif '-' in str(tdelta):
                return False 
            else:
                return True
        elif duration == "Permanent":
            return True
        else:
            return False



updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher
tclient = Client(account_sid, auth_token)

def start(update:Update, context:CallbackContext):
    
    if checkdate(chatid=update.effective_chat.id) == True:
        
        context.bot.send_message(chat_id=update.message.chat_id, text='<b>Welcome to ☎️OTP BOT\nYou have the access to all the commands of the bot, thank you for subscription 💖\n</b>', parse_mode='html')
    else:
        context.bot.send_message(chat_id=update.message.chat_id, text='<b>Welcome to ☎️OTP BOT\nYou can buy access to the otp service using </b><code>/buy</code>\n<b></b>', parse_mode='html')


def chatid(update:Update, context:CallbackContext):
     context.bot.send_message(chat_id=update.message.chat_id, text=f'<b> Your  ID is: </b><code>{update.effective_chat.id}</code>', parse_mode='html')

def error(update, context):
    print(f"[Error] caused error » {context.error}")




call_handler = CommandHandler('call', call.call, run_async=True)
buy_handler = CommandHandler('buy', buy.buy, run_async=True)
start_handler = CommandHandler('start', start, run_async=True)
add_handler = CommandHandler('add', add.add, run_async=True)
chatid_handler = CommandHandler('chatid', chatid, run_async=True)
updatecommand_handler = CommandHandler('update', update.updatecommand, run_async=True)
btc_handler = CommandHandler('btc', buy.btc, run_async=True)
usdt_handler = CommandHandler('usdt', buy.USDT, run_async=True)
eth_handler = CommandHandler('eth', buy.eth, run_async=True)

dispatcher.add_handler(call_handler)
dispatcher.add_handler(buy_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(add_handler)
dispatcher.add_handler(chatid_handler)
dispatcher.add_handler(updatecommand_handler)
dispatcher.add_handler(btc_handler)
dispatcher.add_handler(usdt_handler)
dispatcher.add_handler(eth_handler)


dispatcher.add_error_handler(error)

dispatcher.run_async
updater.start_polling()
print("[TELEGRAM BOT] NOW IN ACTION!!")
