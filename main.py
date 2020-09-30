#!/usr/bin/env python3

import discord
from discord.ext import commands

with open("tokenfile","r") as tokenfile:
	token = tokenfile.read()

client = commands.Bot(command_prefix="ui!")
client.remove_command("help")

@client.event
async def on_ready():
	print(f"logged in as {client.user}")
	print(f"https://discord.com/oauth2/authorize?client_id={client.user.id}&permissions=536870912&scope=bot")
	for guild in client.guilds:
		print(f"In guild: {guild.name}") 

@client.event
async def on_guild_join(guild):
	print(f"Joined guild: {guild.name}")

@client.command()
async def help(ctx):
	await ctx.send("use `ui!imitate <user> <*text>` to imitate a user")

@client.command()
async def imitate(ctx,person,*text):
	msg = " ".join(text)
	imitated = ctx.message.mentions[0]
	avatar = await imitated.avatar_url_as(format="png").read()
	await ctx.send(f"imitating {ctx.message.mentions[0].name}: {msg}")
	hook = await ctx.channel.create_webhook(name=imitated.name,avatar=avatar)
	await hook.send(f"{msg}")
	await hook.delete()

client.run(token)
