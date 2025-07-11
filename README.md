# Marketdome
import requests

BOT_TOKEN = "הטוקן שלך"
URL = "https://532653b2-8531-47bd-a33e-e02010bbd07d-00-i9s4ekq3tq1i.pike.replit.dev/"

res = requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/setWebhook?url={URL}")
print(res.json())