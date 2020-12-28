import discord
from discord.ext import commands
import random
import asyncio
import datetime
from urllib import parse, request
import re
import os

from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix='>', description="This is a Helper Bot")

bot.remove_command('help')

@bot.listen()
async def on_message(message):
	word_list = ['hello', 'hi', 'hey']

	messageContent = message.content
	if len(messageContent) > 0:
		for word in word_list:
			if word in messageContent:
				await message.channel.send('Hello :)')
				# await message.delete()


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('with your mom'))



bot.run(DISCORD_TOKEN)
