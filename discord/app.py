import os
import asyncio
import requests
import discord
from dotenv import load_dotenv
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_ID = os.getenv('GUILD_ID')

intents = discord.Intents.none()
client = commands.Bot(intents=intents)
slash = SlashCommand(client, sync_commands=True)



client.run(TOKEN)