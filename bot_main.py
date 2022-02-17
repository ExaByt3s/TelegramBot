from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from forex_python.converter import CurrencyRates

c = CurrencyRates()

TOKEN="ABCDEFGH12345678" #Qua impostare il token dato da botfather


def extract_number(text):
     return text.split()[1].strip()

#USD
def from_usd_to_eur(currency_1):
	return currency_1/c.get_rate('USD', 'EUR')

def from_eur_to_usd(currency_1):
	return currency_1*c.get_rate('USD', 'EUR')

#RUB
def from_rub_to_eur(currency_1):
    return currency_1/c.get_rate('RUB', 'EUR')

def from_eur_to_rub(currency_1):
    return currency_1*c.get_rate('RUB', 'EUR')

#USD
def convert_usd(update, context):
     usd=float(extract_number(update.message.text))
     eur=from_usd_to_eur(usd)
     print(f'Eseguita conversione da {usd} USD a {eur} EUR')
     update.message.reply_text(f'{eur} EUR')

#RUB
def converter_rub(update, context):
    rub=float(extract_number(update.message.text))
    eur=from_rub_to_eur(rub)
    print(f'Eseguita conversione da {rub} RUB a {eur} EUR')
    update.message.reply_text(f'{eur} EUR')

#EUR
def convert_eur_to_usd(update, context):
     eur=float(extract_number(update.message.text))
     usd=from_eur_to_usd(eur)
     print(f'Eseguita conversione da {eur} EUR a {usd} USD')
     update.message.reply_text(f'{usd} USD')

def converter_eur_to_rub(update, context):
    eur=float(extract_number(update.message.text))
    rub=from_eur_to_rub(eur)
    print(f'Eseguita conversione da {eur} EUR a {rub} USD')
    update.message.reply_text(f'{rub} USD')


def main():
   
   upd=Updater(TOKEN, use_context=True)
   disp=upd.dispatcher
   
   disp.add_handler(CommandHandler("usd", convert_usd))
   disp.add_handler(CommandHandler("eur_usd", convert_eur_to_usd))
   disp.add_handler(CommandHandler("rub", converter_rub))
   disp.add_handler(CommandHandler("eur_rub", converter_rub))
   
   upd.start_polling()
   
   upd.idle()
   
if __name__=='__main__':
   main()
