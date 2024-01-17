import requests as r
import os
import threading
from fake_useragent import UserAgent

class DiscordGX:
    def __init__(self):
        self.api = r.Session()
        self.ua = UserAgent()

    def claimVOC(self):
        headers = {
            'User-Agent': self.ua.random,
            'Content-Type': 'application/json'
        }

        data = {
            'partnerUserId': '54b6f45f5cfc7d58a39e59b8d0a9f679de53b79b8b8148491827589a2c4d28c8'
        }

        resp = self.api.post('https://api.discord.gx.games/v1/direct-fulfillment', headers=headers, json=data)
        return resp

    def claimLink(self):
        response = self.claimVOC()
        token = response.json().get('token')
        url = f'https://discord.com/billing/partner-promotions/1180231712274387115/{token}'
        print(f'[+] Claimed: {url}')
        with open('newdiscord.txt', 'a') as file:
            file.write(url + '\n')

    def thread(self):
        try:
            jumlah = input('> Jumlah Link: ')
            threads = []
            count = 0
            try:
                while count < int(jumlah):
                    thread = threading.Thread(target=self.claimLink, args=())
                    threads.append(thread)
                    thread.start()
                    count += 1

                for thread in threads:
                    thread.join()

            except Exception as r:
                None

        except Exception as r:
            None

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')  # Use 'clear' for Unix-like systems
    print('[ Discord 1 Month Auto ]')
    discord = DiscordGX()
    discord.thread()
