import os
from discord import Intents
from discord.ext import commands
from dotenv.main import dotenv_values

prefix = '/'
bot = commands.Bot(command_prefix = prefix, help_command=None, intents=Intents(members=True))

try:
    config = dotenv_values("./.env")
    token = config['WORKBENCH_BOT_TOKEN']
except:
    token = os.getenv('WORKBENCH_BOT_TOKEN')

for file in os.listdir('bot/cogs'):
    if file.endswith('.py'):
        bot.load_extension(f'cogs.{file[:-3]}')

bot.run(token)

# This is a template for when writing a 'section' of commands. (Eg. Activies, RoleChanging)

#   import discord
#   from discord.ext import commands
#
#   class Template(commands.Cog):
#       def __init__(self, bot):
#           self.bot = bot
#
#       @commands.Cog.listener()
#       async def on_ready(self):
#           print('CYCLES-X: template loaded')
#
#       @commands.command()
#       async def test(self, ctx):
#           await ctx.send("This is a template!")
#
#   def setup(bot):
#       bot.add_cog(Template(bot))