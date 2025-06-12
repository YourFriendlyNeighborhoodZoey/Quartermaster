"""Discord Bot

Required 3RD-Party PyPi Packages:
	- discord
	- dotenv
	- schedule (Currently Unimplemented)
"""
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv  # IMPORT LOAD_DOTENV FUNCTION FROM DOTENV MODULE.

load_dotenv()  # LOADS THE .ENV FILE THAT RESIDES ON THE SAME LEVEL AS THE SCRIPT.

PREFIXES = ["!"]
TOKEN = os.environ['BOT_TOKEN']
bot = commands.Bot(command_prefix=PREFIXES,
	intents=discord.Intents.default())
tree = bot.tree

for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		bot.load_extension(f'cogs.{filename[:-3]}')
		print(f'Cog: {filename[:-3].title().replace("_", "")} loaded.')
	elif filename == "__pycache__":
		continue
	else:
		print(f'Cog: Unable to load {filename[:-3]}')


#* Module Code
def main():
	"""Main Method"""
	bot.run(TOKEN)
	
#? Driver Code
if __name__ == "__main__":
	main()
else:
	print(f"{__name__} was successfully imported") #! MUST have Python 3.x for use of f-strings!