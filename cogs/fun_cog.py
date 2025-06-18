"""
Description:
This Cog contains all the events and commands used for fun and hat-tricks.
"""
# IMPORTS
#import [Module/Package]
from discord import app_commands
from discord.ext import commands        # IMPORT COMMANDS FROM THE DISCORD.EXT MODULE.


class FunCog(commands.Cog):
	"""Cog for fun/wacky commands & events."""
	def __init__(self, bot):
		"""Initializes the cog, passing in a bot to associate itself with."""
		self.bot = bot
	
	# Commands
	@app_commands.command(name="echo",
		description="Echoes a message into the channel the command is triggered in.",
		aliases=["Echo", "ECHO"])
	@app_commands.describe(message="The message to echo.")
	@commands.guild_only()
	async def echo(self, ctx, message):
		"""Insults random users."""
		#TODO: Implement scheduling.
		try:
			await ctx.send(message)
		except commands.CommandError as e:
			await ctx.send(e)
			print (e)


def setup(bot):
	"""Adds The Cog To The Client."""
	bot.add_cog(FunCog(bot))