import discord
import random
from discord.ext import commands, tasks
import time
import datetime
import requests
from discord import CategoryChannel

TOKEN = "your-token-here"
client = discord.Client()
client = commands.Bot(command_prefix = "!")


target_channel_id = 771372586457366538

@tasks.loop(seconds=10)
async def called_once_a_day():
    message_channel = client.get_channel(target_channel_id)
    print(f"Got channel {message_channel}")
    await message_channel.send("Your message")

@called_once_a_day.before_loop
async def before():
    await client.wait_until_ready()
    print("Finished waiting")


@client.command()
async def comm(ctx):
    role = discord.utils.get(ctx.guild.roles, name=str(ctx.message.channel))
    await ctx.send(role)
    category = discord.utils.get(ctx.guild.categories,name=str(role))
    channels = category.channels
    for i in channels:
        await ctx.send(i.id)
        await ctx.send(i.name)

@client.command()
async def roles(ctx):
    name = "nice"
    await ctx.guild.create_role(name="nice", mentionable=True)
    ctf_role = discord.utils.get(ctx.guild.roles, name=str(name))
    print(ctf_role)

@client.command()
async def solve(ctx):
    chall_solve = [ctx.message.author.name] + [m.name for m in ctx.message.mentions]
    await ctx.send(str(chall_solve))

@client.command()
async def delete(ctx):
    category = discord.utils.get(ctx.guild.categories,name="try")
    channels = category.channels
    for i in channels:
        await ctx.send(i.name)
        channel = client.get_channel(i.id)
        await channel.delete()
        await ctx.send("deleted " + i.name)
    await category.delete()
    await ctx.send("deleted "+ "try")


@client.event
async def on_member_join(member):
    print("A member has joined the server!!")

@client.event
async def on_member_remove(member):
    print("A member has left the server!!")

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency*1000)}ms")

@client.command()
async def kick(ctx,member : discord.Member, *,reason = None):
    await member.kick(reason = reason)
    await ctx.send(f"Kick {user.mention}")

@client.command()
async def ban(ctx,member : discord.Member, *,reason = None):
    await member.ban(reason = reason)
    await ctx.send(f"Ban {user.mention}")

@client.command()
async def unban(ctx, *,member):
    banned_users = await ctx.guild.bans()
    member_name, member_descr = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name,user.discriminator) == (member_name, member_descr):
            await ctx.guild.unban(user)
            await ctx.send(f"Unbanned {user.mention}")
            return 
    

@client.command(aliases=['8ball','test'])
async def _8ball(ctx, *,question):
    responses = ["because he is a thopp"]
    await ctx.send(f"Question: {question}\nAnswer:{random.choice(responses)}")

@client.command()
async def clear(ctx,amount=5):
    await ctx.channel.purge(limit=amount)

called_once_a_day.start()
client.run(TOKEN)

