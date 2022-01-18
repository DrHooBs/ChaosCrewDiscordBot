from discord.ext import commands
import discord
import discord.utils

class good_morning(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.lower().startswith("good morning"):
            if message.author.id != 932687176997687316:
                await message.reply("Good morning")


def setup(bot):
    bot.add_cog(good_morning(bot))