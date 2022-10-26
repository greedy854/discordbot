import discord
intents = discord.Intents.default()
intents.messages= True
client = discord.Client(intents=intents)
bottoken=open("c:\geheim\discordbot.txt", "r").readline()
client.run("MTAzNDg1OTA1Nzc5MTYzNTUyNw.G0yNh_.X-i7ScHgP4iKc21zHXa1u-2vNDOCLHTMctYL6U")
@client.event
async def on_ready():
    guild = client.guilds[0]
    print(guild.name, "is the name of the server")
    print(client.user, "has connected to the client")
    channel = guild.text_channels[0]
    print(channel.name, "is the name of the channel")
    await channel.send("I'm online!")
@client.event
async def on_message(message):
    print(message.channel.name, "the message was posted from this channel")
    print(message.content)
    print(message.author,"is the user who wrote the message")
    print(message.created_at,"is when the message was posted")
    print(message.channel,"is the channel this message was posted in")
    await message.channel.send("Hello " + message.author)
    if message.author.bot == False:
        message.channel.send