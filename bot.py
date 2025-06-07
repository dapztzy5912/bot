import time
import requests
import signal
import sys

# Masukkan TOKEN dan ID kamu
TOKEN = "7776401602:AAHAPvj35u6MbITYDh29oUM9a-v03JLlcBw"
CHAT_ID = "7341190291"

def kirim_pesan(pesan):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": pesan}
    try:
        requests.post(url, data=data)
    except Exception as e:
        print(f"Gagal mengirim pesan: {e}")

def ketika_exit(signum, frame):
    kirim_pesan("🔴 BOT TERPUTUS")
    sys.exit(0)

# Pasang signal untuk menangani CTRL+C atau stop script
signal.signal(signal.SIGINT, ketika_exit)
signal.signal(signal.SIGTERM, ketika_exit)

# Kirim pesan ON
kirim_pesan("🟢 BOT TERSAMBUNG")

# Loop dummy (biar bot tetap jalan)
while True:
    time.sleep(10)
