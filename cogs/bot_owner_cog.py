"""
Description:
This Cog contains all the events and commands only the bot owner can utilize.
"""
# IMPORTS
#import [Module/Package]
from discord import app_commands
from discord.ext import commands

class BotOwnerCog(commands.GroupCog, group_name="Bot Owner Cog"):
	"""Cog with commands only the bot owner can invoke."""
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	# Hidden means it won't show up on the default help.
	@app_commands.command(name="load",
		description="Loads a cog of the specified name.",
		hidden=True)
	@app_commands.describe(cog="The name of the cog to load.")
	@commands.is_owner()
	async def load_cog(self, ctx, *, cog: str):
		"""Command which Loads a Module.
		   Remember to use dot path. (e.g: cogs.owner)"""
		try:
			self.bot.load_extension(cog)
		except Exception as e:
			await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
		except commands.CommandError as e:
			await ctx.send(e)
			print (e)
		else:
			await ctx.send('**`SUCCESS`**')

	@app_commands.command(name='unload',
		description="Unloads a cog of the specified name.",
		hidden=True)
	@app_commands.describe(cog="The name of the cog to unload.")
	@commands.is_owner()
	async def unload_cog(self, ctx, *, cog: str):
		"""Command which Unloads a Module.
		   Remember to use dot path. (e.g: cogs.owner)"""
		try:
			self.bot.unload_extension(cog)
		except Exception as e:
			await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
		except commands.CommandError as e:
			await ctx.send(e)
			print (e)
		else:
			await ctx.send('**`SUCCESS`**')

	@app_commands.command(name='reload',
		description="Reloads a cog of the specified name.",
		hidden=True)
	@app_commands.describe(cog="The name of the cog to reload.")
	@commands.is_owner()
	async def reload_cog(self, ctx, *, cog: str):
		"""Command which Reloads a Module.
		   Remember to use dot path. (e.g: cogs.owner)"""
		try:
			self.bot.unload_extension(cog)
			self.bot.load_extension(cog)
		except Exception as e:
			await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
		except commands.CommandError as e:
			await ctx.send(e)
			print (e)
		else:
			await ctx.send('**`SUCCESS`**')


def setup(bot):
	bot.add_cog(BotOwnerCog(bot))