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