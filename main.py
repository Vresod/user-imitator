#!/usr/bin/env python3

import discord
from discord.ext import commands
from asyncio import sleep as aiosleep

with open("tokenfile","r") as tokenfile:
	token = tokenfile.read()

client = commands.Bot(command_prefix="ui!")
client.remove_command("help")

repo_embed = discord.Embed(title="Repo",description="https://github.com/Vresod/user-imitator")

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
	await ctx.send(embed=repo_embed)

@client.command()
async def repo(ctx):
	await ctx.send(embed=repo_embed)

@client.command()
async def imitate(ctx,person,*text):
	msg = " ".join(text)
	imitated = ctx.message.mentions[0]
	avatar = await imitated.avatar_url_as(format="png").read()
	confirm_message = await ctx.send(f"imitating {ctx.message.mentions[0].name}: {msg}")
	hook = await ctx.channel.create_webhook(name=imitated.display_name,avatar=avatar)
	await ctx.message.add_reaction(u"\U00002705")
	await hook.send(f"{msg}")
	await hook.delete()
	await aiosleep(3)
	await confirm_message.delete()

client.run(token)
