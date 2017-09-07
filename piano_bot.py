
import discord
import random as rand
from discord.ext.commands import Bot
from discord.ext import commands

bot = commands.Bot(command_prefix="!")
client = discord.Client()

@client.event
async def on_ready():
    print("Bot Online!")
    print("Name: " + client.user.name)
    print("ID: " + client.user.id)

@bot.event
async def on_ready():
    print("Bot Online!")
    print("Name: " + bot.user.name)
    print("ID: " + bot.user.id)

@bot.command(pass_context=True)
async def random(context):
    scales = ["c major","c minor melodic","c minor harmonic","d major",
              "d minor melodic","d minor harmonic","b major","b minor melodic",
              "b minor harmonic","f# major","f# minor melodic",
              "f# minor harmonic","f major","f minor melodic",
              "f minor harmonic","eb major","eb minor melodic",
              "eb minor harmonic","ab major","g# minor melodic",
              "g# minor harmonic","db major","c# minor melodic",
              "c# minor harmonic"]
    await bot.say("**" + test(scales) + "**")

def test(scales):
    return rand.choice(scales)

bot.run("secret key")
