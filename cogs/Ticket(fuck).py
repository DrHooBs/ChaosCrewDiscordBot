from discord.ext import commands
import discord
import discord.utils

class Ticket(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # @commands.command(name='CreateTicket',aliases= ["createTicket","Createticket","createticket", "ct"],brief='"?ct #your question" Creates a channel with you\'re suggestion/problem')
    # async def createticket(self, ctx, *, text):
    #     guild = ctx.guild
    #     text_channel_list = []
    #     for channel in guild.text_channels:
    #         text_channel_list.append(channel)
    #     channelname = (f"{ctx.author.name}-{ctx.author.id}")#random.randint(100000,999999)
    #     channel = await guild.create_text_channel(channelname)
    #     #print(text_channel_list)
    #     await channel.send(f"{ctx.author.name}'s Ticket message: {text}")
    #     await ctx.message.delete()
    #     await ctx.send("Ticket created")
    
                        #await create_thread(*, name, auto_archive_duration=in-minutes)

def setup(bot):
    bot.add_cog(Ticket(bot)) 