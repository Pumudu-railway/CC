import os
import telethon
import re
import time
import asyncio
import json
import requests
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon import events

SESSION = '1AZWarzsBuxhLbPMiIMDMn5pz1llURS0tgEO6ealchpbaVyF5rFXvCR-xHHPLrQKH7pj6w_81kAXpnEjMV5geUrGhBjtSRv7jl-HGxvN02jKt4QG7P3hANr5zj04ncKUNpFtlYmHtouW68mRPRRyY2pldSjya4jB-HeSpv63qyFuadcPfjBuq7lpCZJ3_-2MLd8hAXgMy7hvzHqAJ8GgnJjwZ7H0yF_ubcK9SPaPlMFw_yPAMPAM9HNBfKWqOWVNSN0sFpJSrH2kQjXsNyJxGkVuzEQ5BumgE75g5VHTEPx_QUSAKLcMoYdOHuGllqYUSU9bq6lcQhVGHItZvqvoEeu7_hJH3vdU='
API_ID = '7493075'
API_HASH = 'ab7d7ab8d1e8cdb4bcbfdf18fa88e2b5'
LOG_GROUP = -6-673632503


bot = TelegramClient(StringSession(SESSION), API_ID, API_HASH)
bot.start()

def get_cc(amount,bin):
    
    req = requests.get(f'https://rezothcc.herokuapp.com/cc.php?bin={bin}&count={amount}&json')
    if json.loads(req.content)["ok"]:
        return json.loads(req.content)["data"]

@bot.on(events.NewMessage(pattern='/go'))
async def runner(event):
    bin = 500962
    l_bin = 502000
    
    while bin <= l_bin:
        #print(bin)   
        t = get_cc(1,bin)
        for card in t:
            #print(card)
            final_card = f'''/chk {card}
{bin}'''
            await bot.send_message(LOG_GROUP, final_card)
            bin = bin + 1
            time.sleep(20)
    mention = '@asas'
    await bot.send_message(LOG_GROUP, mention)

bot.run_until_disconnected()
