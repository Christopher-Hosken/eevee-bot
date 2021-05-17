import discord
from discord.ext import commands
import random
import re

class Activities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Activities loaded')

    @commands.command(aliases=['8ball'])
    async def blenderball(self, ctx, *, question):
        responses = [
            'The Blender Gods agree.',
            'Yes.',
            'You will find your answer in the shader editor.',
        ]

        embed = discord.Embed(title="Blender Ball", color=discord.Color.blue())
        embed.add_field(name="Question", value=question, inline=False)
        embed.add_field(name="Answer", value=random.choice(responses), inline=False)

        await ctx.send(embed=embed)
    
    @commands.Cog.listener()
    async def on_message(self, message):
        emoji_pattern = ":(.*?):"
        if message.content.startswith("<") and message.content.endswith(">"):
            msg = str(message.content)[1:][:-1]
            for e in self.bot.emojis:
                f = re.search(emoji_pattern, str(e)).group(1)
                if (f == msg):
                    print(f"Found '{f}': {str(e)}")
                    break
            else:
                e = None

            if e is not None:
                await message.delete()
                await message.channel.send(str(e))


def setup(bot):
    bot.add_cog(Activities(bot))