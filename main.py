import discord 
import os 
import requests
import json
import random
from keep_alive import keep_alive

client = discord.Client()

fuck_words = ["jiva","bich","bitch","dick"]

starter_encouragements = [
  "your parants should have aborted you.",
  "shut up you bitch.",
  "piss off.",
  "suck my dick bitch.",
  "you are a slut.",
]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

    if message.author == client.user:
      return

    msg = message.content

    if message.content.startswith('$what did you fuck today?'):
      await message.channel.send('I FUCK YOUR MOM!') 

    if any(word in msg for word in fuck_words):
      await message.channel.send(random.choice(starter_encouragements))

keep_alive()

client.run(os.getenv('TOKEN')) 
