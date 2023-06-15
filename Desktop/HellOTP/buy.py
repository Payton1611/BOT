from telegram.ext import *
from telegram import *
import os


def buy(update:Update, context:CallbackContext):
    keyb = InlineKeyboardMarkup([
    [InlineKeyboardButton("Profile ",url="https://t.me/Real_Pageforyou")]
    ])
    context.bot.send_message(chat_id=update.message.chat_id, text=f'<b>ChatID: {update.effective_chat.id} \n[+] Plan : \n 20$ - 1 Day \n60$ - 1 week\n150$ - 1 month\n500$ - 1 year \n700$  -  lifetime \nTo order Please Send The Amout of money 💰 and in description of the payment Send Your Chat ID or Send it here @Real_Pageforyou ❤️</b>\n/BTC\n/ETH\n/USDT (trc20)\n/LTC\n<b>[+] Other Payment Methode click On The button Below 💰👀 (Paypal…)</b>', parse_mode='html', reply_markup=keyb)

def btc(update: Update, context: CallbackContext):
    keyb = InlineKeyboardMarkup([
    [InlineKeyboardButton("Profile ",url="https://t.me/Real_Pageforyou")]
    ])
    dirr = open(os.getcwd() + '/Extra/qrs/bitcoinwallet.jpg', 'rb')
    context.bot.send_photo(chat_id=update.message.chat_id,photo=dirr,caption=f'<b>ChatID: {update.effective_chat.id} \n[+] Address: bc1q2fxju4lze9dder0g4qtnwlc79rmd50yqtct82q</b>', parse_mode='html', reply_markup=keyb)

def USDT(update: Update, context: CallbackContext):
    keyb = InlineKeyboardMarkup([
    [InlineKeyboardButton("Profile ",url="https://t.me/Real_Pageforyou")]
    ])
    dirr = open(os.getcwd() + '/Extra/qrs/usdtwallet.jpg', 'rb')
    context.bot.send_photo(chat_id=update.message.chat_id,photo=dirr,caption=f'<b>ChatID: {update.effective_chat.id} \n[+] Address: THzxDVn3m3AuS4NHxExZi3BYoPeWLMPA2p (TRC 20)</b>', parse_mode='html', reply_markup=keyb)

def eth(update: Update, context: CallbackContext):
    keyb = InlineKeyboardMarkup([
    [InlineKeyboardButton("Profile ",url="https://t.me/Real_Pageforyou")]
    ])
    dirr = open(os.getcwd() + '/Extra/qrs/ethwallet.jpg', 'rb')
    context.bot.send_photo(chat_id=update.message.chat_id,photo=dirr,caption=f'<b>ChatID: {update.effective_chat.id} \n[+] Address: 0x7EC2A25A66B2856e88CCaFd53a4B8C660c0543df </b>', parse_mode='html', reply_markup=keyb)
