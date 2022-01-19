from email import message
import discord
from discord.ext import commands
import time
import asyncio
import random
import os
import sys
client = commands.Bot(command_prefix="?",owner_ids=[386826952599928842, 427822985102098434] )

TOKEN = "OTMyNjg3MTc2OTk3Njg3MzE2.YeWmnw.dp23z_eX2g_bNB1qkXYf_QRGXqM"

@client.event
async def on_ready():
    print("Ready")



@client.event
async def on_member_join(ctx):
    print("member has joined")
    extension = "membercount"
    try:
        msg = await ctx.send(f'Reloading {extension}...')
        client.reload_extension(f'cogs.{extension}')
        await msg.edit(content=f"Reloaded {extension} succesfully")
    except Exception as error:
        await ctx.send(f'Error:\n```py\n{error}\n```')

@client.event
async def on_member_remove(ctx):
    os.system("python main.py")

@client.command(name="restart", aliases=["r"])
@commands.is_owner()
async def restart(ctx):
    await ctx.send("Restarting")
    os.system("python main.py")
    time.sleep(1)
    

@client.event
async def on_member_join(member, ctx):
    await ctx.send('ello')

@client.command(name='kill', aliases=['k'])
@commands.is_owner()
async def unloadall(ctx):
    await ctx.send("Breaking")
    exit()




@client.command(name='reload')
#@commands.is_owner()
async def reload(ctx, extension):
    try:
        msg = await ctx.send(f'Reloading {extension}...')
        client.reload_extension(f'cogs.{extension}')
        await msg.edit(content=f"Reloaded {extension} succesfully")
    except Exception as error:
        await ctx.send(f'Error:\n```py\n{error}\n```')



@client.command(name='load', aliases=['l'])
#@commands.is_owner()
async def load(ctx, extension):
    try:
        msg = await ctx.send(f'Loading {extension}...')
        client.load_extension(f'cogs.{extension}')
        await msg.edit(content=f"Loaded {extension} succesfully")
    except Exception as error:
        await ctx.send(f'Error:\n```py\n{error}\n```')



@client.command(name='unload', aliases=['u'])
#@commands.is_owner()
async def unload(ctx, extension):
    try:
        msg = await ctx.send(f'Unloading {extension}...')
        client.unload_extension(f'cogs.{extension}')
        await msg.edit(content=f"Unloaded {extension} succesfully")
    except Exception as error:
        await ctx.send(f'Error:\n```py\n{error}\n```')


@client.command(name='loadall', aliases=['la'])
#@commands.is_owner()
async def loadall(ctx):
    try:
        msg = await ctx.send(f"Loading")
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                client.load_extension(f'cogs.{filename[:-3]}')
        await msg.edit(content="Loaded all extensions successfully")
    except Exception as error:
        await ctx.send(f'Error:\n```py\n{error}\n```')


@client.command(name='unloadall', aliases=['ula'])
#@commands.is_owner()
async def unloadall(ctx):
    try:
        msg = await ctx.send(f"Unloading")
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                client.unload_extension(f'cogs.{filename[:-3]}')
        await msg.edit(content="Unloaded all extensions successfully")
    except Exception as error:
        await msg.edit(f'Error:\n```py\n{error}\n```')


@client.command()
async def ping(ctx):
     await ctx.send(f'Pong! In {round(client.latency * 1000)}ms')

@client.command(name='reloadall', aliases=['rla'])
#@commands.is_owner()
async def reloadall(ctx):
    try:
        msg = await ctx.send(f"Reloading")
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                client.reload_extension(f'cogs.{filename[:-3]}')
        await msg.edit(content="Reloaded all extensions successfully")

    except Exception as error:
        await ctx.send(f'Error:\n```py\n{error}\n```')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        print(f'loading cogs.{filename[:-3]}')
        client.load_extension(f'cogs.{filename[:-3]}')
        print(f'loaded cogs.{filename[:-3]}')

client.run(TOKEN)