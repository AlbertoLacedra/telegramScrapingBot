from telethon.sync import TelegramClient
import requests

# Configura i tuoi dati qui
api_id = 'API_ID'
api_hash = 'API_HASH'
bot_token = 'bot_token'  # il token che hai ottenuto da @BotFather
chat_id = 'chat_id'  # chat_id che hai ottenuto

# Inizializzazione del client
client = TelegramClient('session', api_id, api_hash)

# Parole chiave da cercare (case insensitive)
keywords = ['errore di prezzo', 'minimo storico']

# Funzione per inviare messaggi al tuo bot
def send_to_telegram(text):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML"  # puoi usare anche Markdown
    }
    requests.post(url, data=payload)

# Avvia il client
with client:
    for message in client.iter_messages('scontierrati'):  # es: 'offertetop'
        if message.text:
            testo = message.text.lower()
            if any(keyword in testo for keyword in keywords):
                send_to_telegram(message.text)
