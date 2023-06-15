from telegram import *
from telegram.ext import *
from pymongo import MongoClient
from datetime import datetime

cluster = MongoClient("mongodb+srv://TOP:TOPSMS@bot.kqphwt1.mongodb.net/?retryWrites=true&w=majority")
db = cluster["users"]
collection = db["users"]

def updatecommand(update: Update, context:CallbackContext):
    if update.message.chat_id == "476263382" or "1755608503":
        chatid = str(context.args[0])
        duration = str(context.args[1])
        if "Day" in duration:

            result = collection.update_many(
                {"chatid":f"{chatid}"},
                {
                        "$set":{
                                "expirationdate":datetime.now().strftime("%H:%M:%S"),
                                "duration":f"{duration}"
                                },
                        "$currentDate":{"lastModified":True}
                        
                            }
                    )
        else:
            result = collection.update_many(
                {"chatid":f"{chatid}"},
                {
                        "$set":{
                                "expirationdate":datetime.now().strftime('%d/%m/%Y'),
                                "duration":f"{duration}"
                                },
                        "$currentDate":{"lastModified":True}
                        
                            }
                    )

            
        context.bot.send_message(chat_id='476263382', text=result)
        context.bot.send_message(chat_id=update.message.chat_id, text=f"<b>Done</b>", parse_mode='html')
