print("Attemping start") # I just like to have this so I can know it actually started at all, before anything else happens

# Needs members and message content intents

import discord
from discord.ext import commands

import time

import logging
from dotenv import load_dotenv
import os

def botlog(): # Set up logging
    logging.basicConfig(filename="logs.txt",
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)
    time.sleep(1)
    logging.info("Runnin' the bot")

botlog() # Log
print("Logging started") # So the logs know that the logged attemped to log the logs for the log

# .env stuff
# Make sure you change all this in .env so the bot can actually run!
load_dotenv()
TOKEN = os.getenv("TOKEN")
BANNER = os.getenv("BANNER")
CHANNEL = os.getenv("CHANNEL")
FILE = os.getenv("FILE") #The file we're sending

# describe bot
description = """Sends messages from a file to a channel with a custom banner above."""

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def send(ctx):
        leaderboardsend = open(FILE, "r")
        if ctx.channel.id == CHANNEL: # Registry channel
            await ctx.channel.purge() # Get rid of previous messages before sending the new leaderboard
            print("Messages cleared")
            await ctx.send(BANNER) # You can comment out this line if you want
            time.sleep(1) # Just to give it time to load
            await ctx.send(leaderboardsend.read()) # Read from file & send that
            leaderboardsend.close() # Don't leave the file open
            print("Sent file")
        else:
            print("ERROR: Channel did not match")

@bot.command()
async def ping(ctx):
    await ctx.send('Pong')
    print("Pinged")

@bot.command()
async def say(ctx, userMessage):
        # Message must be surrounded by quotes if contains spaces
        # There's probably a way around that
        # I don't know that way
        await ctx.send(userMessage)
        print(userMessage)

print("Running")
bot.run(TOKEN)
