import requests
from colorama import Fore
import random
import time
import os

print("=============================================")
author = "Bg.Pateng"
print("Spesial Thanks To " + author)
telegram = "@bangpateng_group"
print("Telegram: " + telegram)
youtube = "Bang Pateng"
print("Youtube: " + youtube)
print("===========================================")
print('PERINGATAN : TIDAK UNTUK DI PERJUAL-BELIKAN')
print("===========================================\n")
time.sleep(1)

channel_id = input("Masukkan ID channel: ")
delay2 = int(input("Set Delay Kirim Pesan (dalam detik): "))
delay1 = int(input("Set Delay Hapus Pesan (dalam detik): "))

time.sleep(1)
print("Silahkan Tunggu")
time.sleep(1)
print(".............")
time.sleep(5)


os.system('cls' if os.name == 'nt' else 'clear')

with open("pesan.txt", "r") as f:
    words = f.readlines()

with open("token.txt", "r") as f:
    authorization = f.readline().strip()

while True:
        channel_id = channel_id.strip()

        payload = {
            'content': random.choice(words).strip()
        }

        headers = {
            'Authorization': authorization
        }

        r = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", data=payload, headers=headers)
        print(Fore.WHITE + "Sent message: ")
        print(Fore.YELLOW + payload['content'])

        response = requests.get(f'https://discord.com/api/v9/channels/{channel_id}/messages', headers=headers)

        if response.status_code == 200:
            messages = response.json()
            if len(messages) == 0:
                is_running = False
                break
            
            else:
                time.sleep(delay1)

                message_id = messages[0]['id']
                response = requests.delete(f'https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}', headers=headers)
                if response.status_code == 204:
                    print(Fore.GREEN + f'Pesan dengan ID {message_id} berhasil dihapus')
                else:
                    print(Fore.RED + f'Gagal menghapus pesan dengan ID {message_id}: {response.status_code}')
        else:
            print(f'Gagal mendapatkan pesan di channel: {response.status_code}')

        time.sleep(delay2)