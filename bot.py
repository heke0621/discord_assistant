import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

#打指令用的前置字元
bot = commands.Bot(command_prefix= '!',intents = intents)

#機器人的事件
@bot.event
async def on_ready():
    print(">>你的最強助理已上線<<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(948141658598428702)
    await channel.send(F'{member} 加入了，夾道歡迎🥳！')
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(948141658598428702)
    await channel.send(F'{member} 退出群組，離我們而去🥺！')
bot.run('OTQ4MTQwMzA0MjQwODY5Mzk2.Yh3eeA.MlqxcdYskA0T9sXQ3oiKI_alJOg')