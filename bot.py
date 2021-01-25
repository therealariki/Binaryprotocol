import discord
import logging
from discord.ext import commands
from config import discordToken
from discord.utils import get

logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


bot = commands.Bot(command_prefix="0xa ")
bot.remove_command('help')
cogs = []
cogs.append('cogs.SQLCog')
cogs.append('cogs.discordCog')


if __name__ == '__main__':
    for ext in cogs:
        bot.load_extension(ext)

@bot.event
async def on_ready():
    print("Ready to assist :)")
    await bot.change_presence(activity=discord.Game(name=" with 🍺"))

@bot.event
async def on_member_join(member):
    message = '''
Welcome to Binary Protocol, before you can start chatting, you need to introduce yourself.
So when you are ready, head to the introductions channel :)
We hope you hear from you soon'''
    await member.create_dm()
    channel = member.dm_channel
    await channel.send(message)
    role = get(member.guild.roles, name="Unverified")
    await member.add_roles(role)


    
                

       
bot.run(discordToken)
