from pymongo import MongoClient
from datetime import datetime
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

print(checkdate(chatid='476263382'))
