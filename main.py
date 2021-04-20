import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive

client = discord.Client()

bot_on = True

fuck_words = [
    "denis", "jiva", "iubi", "radu", "bombardier", "pita", "paine", "bitch",
    "gaymer", "viasu", "vias", "dick", "discord", "andra", "pan", "bi",
    "romana", "manusa", "Denisa", "Denis", "pula", "nefutut", "andres",
    "drecu", "drq", "adrian", "mom", "ma-ta", "ma ta", "fizica", "nis", "tot",
    "shut up", "taci", "pl","Todo","todo","Paladin",
]

starter_encouragements = [
    "sugator de pula infect.",
    "suck my dick you slut.",
    "your parants should have aborted you.",
    "piss off",
]

if "responding" not in db.keys():
    db["responding"] = True


def update_encouragements(encouraging_message):
    if "encouragements" in db.keys():
        encouragements = db["encouragements"]
        encouragements.append(encouraging_message)
        db["encouragements"] = encouragements
    else:
        db["encouragements"] = [encouraging_message]


def delete_encouragment(index):
    encouragements = db["encouragements"]
    if len(encouragements) > index:
        del encouragements[index]
        db["encouragements"] = encouragements


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "bot_on" not in db.keys():
      db["bot_on"] = True

    msg = message.content

    if message.content == '$nis':
      db["bot_on"] = True

    if message.content == '$stop':
      db["bot_on"] = False

    if db["bot_on"] == True:
      if db["responding"]:
          options = starter_encouragements
          if "encouragements" in db.keys():
              options = options + db["encouragements"]

          if any(word in msg for word in fuck_words):
              await message.channel.send(random.choice(options))

      if msg.startswith("$new"):
          encouraging_message = msg.split("$new ", 1)[1]
          update_encouragements(encouraging_message)
          await message.channel.send("New encouraging message added.")

      if msg.startswith("$del"):
          encouragements = []
          if "encouragements" in db.keys():
              index = int(msg.split("$del", 1)[1])
              delete_encouragment(index)
              encouragements = db["encouragements"]
          await message.channel.send(encouragements)

      if msg.startswith("$list"):
          encouragements = []
          if "encouragements" in db.keys():
              encouragements = db["encouragements"]
          await message.channel.send(encouragements)

      if msg.startswith("$responding"):
          value = msg.split("$responding ", 1)[1]

          if value.lower() == "true":
              db["responding"] = True
              await message.channel.send("Responding is on.")
          else:
              db["responding"] = False
              await message.channel.send("Responding is off.")


keep_alive()
client.run(os.getenv('TOKEN'))
