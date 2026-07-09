import requests

# 1. Update this with your NEW revoked/generated token
TELEGRAM_TOKEN = '8641368431:AAGTuBnWaK-EihRs-zJQYRvw0aRZl05xtv4' 
CHAT_ID = 8698503355

def send_telegram_alert(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {'chat_id': CHAT_ID, 'text': message}
    requests.post(url, data=payload)

# 2. Meteoblue API
METEOBLUE_URL = "https://my.meteoblue.com/packages/basic-1h_basic-day?apikey=Pv1z2bAu3t5RE0i8&lat=30.0626&lon=31.2497&asl=23&format=json"
response = requests.get(METEOBLUE_URL).json()

times = response['data_1h']['time']
precip = response['data_1h']['precipitation']
print(response)
# 3. Logic to check for rain in the next 12 hours
rain_found = False
for i in range(12):
    if precip[i] > 0:
        print(f"Rain predicted at {times[i]}: {precip[i]} mm")
        rain_found = True

# 4. Send only ONE alert if rain is found at any point in the 12 hours
if rain_found:
    send_telegram_alert("Rain is expected in Cairo within the next 12 hours. Prepare accordingly!")
else:
    print("No rain predicted for the next 12 hours.")