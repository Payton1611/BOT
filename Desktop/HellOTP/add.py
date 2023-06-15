from telegram.ext import *
from telegram import *
from pymongo import *
from pymongo import MongoClient
from datetime import datetime

cluster = MongoClient("mongodb+srv://TOP:TOPSMS@bot.kqphwt1.mongodb.net/?retryWrites=true&w=majority")
db = cluster["users"]
collection = db["users"]


def add(update:Update, context:CallbackContext):
    if update.message.chat_id == "476263382" or "1755608503":
        chatid = str(context.args[0])
        duration = str(context.args[1])


        if "Day" in duration:
            emp_rec1 = {
                "chat_id":f"{chatid}",
                "creationdate":datetime.now().strftime("%H:%M:%S"),
                "expirationdate":datetime.now().strftime("%H:%M:%S"),
                "duration":f"{duration}",
                "isadmin":"False"
                }
        else:
            emp_rec1 = {
                "chat_id":f"{chatid}",
                "creationdate":datetime.now().strftime('%d/%m/%Y'),
                "expirationdate":datetime.now().strftime('%d/%m/%Y'),
                "duration":f"{duration}",
                "isadmin":"False"
                }

        rec_id2 = collection.insert_one(emp_rec1)
            
        print("Data inserted with record ids",rec_id2)
        context.bot.send_message(chat_id=update.message.chat_id, text=f"<b>Added Succedful {chatid} \nduratiom : {duration}</b>", parse_mode='html')
