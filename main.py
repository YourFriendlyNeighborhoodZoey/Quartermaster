"""Discord Bot

Required 3RD-Party PyPi Packages:
	- discord
	- dotenv
	- schedule (Currently Unimplemented)
"""
# System Modules
import os						# For Directory Navigation
import logging					# For Tracking Execution Flow

# Discord API
import discord
from discord.ext import commands
# DotENV (Local Environment Variables)
from dotenv import load_dotenv  # IMPORT LOAD_DOTENV FUNCTION FROM DOTENV MODULE.


load_dotenv()  # LOADS THE .ENV FILE THAT RESIDES ON THE SAME LEVEL AS THE SCRIPT.
module_logger = logging.getLogger(__name__)


PREFIXES = ["/", "!"]
TOKEN = os.environ['BOT_TOKEN']
bot = commands.Bot(command_prefix=PREFIXES,
	intents=discord.Intents.default())
tree = bot.tree


async def load_cogs(cogs_dir: str = './cogs'):
	for filename in os.listdir(cogs_dir):
		if filename.endswith('.py'):
			await bot.load_extension(f'cogs.{filename[:-3]}')
			module_logger.info("%s loaded." % filename[:-3].title().replace("_", ""))
			print(f'Cog: {filename[:-3].title().replace("_", "")} loaded.')
		elif filename == "__pycache__":
			continue
		else:
			module_logger.warning("Unable to load %s." % filename[:-3])
			print(f'Cog: Unable to load {filename[:-3]}')


#* Module Code
def main():
	"""Main Method"""
	# This prevents Pylance from reporting on "unused" coroutines.
	load_cogs() # pyright: ignore[reportUnusedCoroutine]
	bot.run(TOKEN)


#? Driver Code
if __name__ == "__main__":
	main()
else:
	print(f"{__name__} was successfully imported") #! MUST have Python 3.x for use of f-strings!