import discord
import os
import keep_alive

client = discord.Client()

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith("z.hi"):
		await message.channel.send("Привет!")

keep_alive.keep_alive()
client.run(os.environ.get("token"))