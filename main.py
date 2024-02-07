import discord
from discord.ext import commands
import random
from image_finder import *
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions
from api_repsonce import *
import datetime
from discord import FFmpegPCMAudio
Bot_Token = "MTIwMzUzOTUwNDA0NTIzMjE3OQ.GSHv1J.64kz5fjzszJeQSx-SW4-Iz78IPb4bR6XW3h4Us"
Channel_ID = 1203764768012243006

client = commands.Bot(command_prefix="!",intents= discord.Intents.all())


@client.event
async def on_ready():
    print("**BOT IS READY**")
    print("---------------------------------")
    

@client.command()
async def hello(ctx):
    await ctx.send("**HADIIIIII IS HERE !!!!!**")

@client.command()
async def goodbye(ctx):
    await ctx.send("**GOOBYE HANJI !!!!!**")

@client.event
async def on_member_join(member):
    channel = client.get_channel(Channel_ID)
    await channel.send("**You dare enter**")

@client.event
async def on_member_remove(member):
    channel = client.get_channel(Channel_ID)
    await channel.send("Goodbye.... **never return...**")

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")
@client.command(aliases =['Calcultae','CALCULATE','calculate'])
async def math(ctx,expression):
    Calculated =  eval(expression)
    await ctx.send(Calculated)

#
@client.command(pass_context = True)
async def hadi(ctx):
    await ctx.send("Prime Hadi", file=discord.File(getHadi()))

@client.command()
async def scheduleEvents(ctx, date, time):
    event_datetime = datetime.datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
    current_datetime = datetime.datetime.now()
    print(event_datetime, current_datetime)

    if event_datetime <= current_datetime:
        channel = client.get_channel(Channel_ID)
        await channel.send("**GET ON**")
    else:
        await ctx.send(f"Event scheduled for {event_datetime}.")

@client.event
async def on_message(message):
    # Prevent the bot from reacting to its own messages
    if message.author == client.user:
        return

    # Don't react to messages that start with "!"
    if not message.content.startswith('!'):
        # Check the content of the message and react accordingly
        if "sad" in message.content.lower():
            await message.add_reaction("\U0001F622")  # This will add a crying face emoji

    # This line is necessary if you also have commands
    await client.process_commands(message)
#Voice Channel Commands
@client.command(pass_context = True)
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.message.author.voice.channel
        await channel.connect()  # This line makes the bot join the channel
        await ctx.send("You have summoned me. **You are here to serve me.**")
    else:
        await ctx.send("You are not in a voice channel. **Be Gone**")

@client.command(pass_context = True)
async def play(ctx):
    try:
        channel = ctx.message.author.voice.channel
        if ctx.voice_client is not None:
            await ctx.voice_client.move_to(channel)
            voice = ctx.voice_client
        else:
            voice = await channel.connect()

        if voice.is_playing():
            voice.stop()

        source = FFmpegPCMAudio('one-night-with-you-background-romantic-music-sax-jazz-for-video-166529.mp3')
        voice.play(source)
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")

#Disabling Voice Channels    
@client.command(pass_context = True)
async def leave(ctx):
    if(ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("I have left")
    else:
        await ctx.send("I am not in a voice channel")




#kick command
@client.command()
@has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"{member} has been banned")

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send("You do not have that power to kick. **I AM HADII**")



#band command
@client.command()
@has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"{member} has been banned")
@ban.error
async def kick_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send("You do not have that power to ban. **I AM HADII**")


#Quote Command
@client.command()
async def quote(ctx):
    await ctx.send(getResponce())

@client.command()
async def feed_me(ctx):
    await ctx.send(":banana:")  # Replace "emoji_name" and "emoji_id" with your emoji's name and ID

client.run(Bot_Token)
