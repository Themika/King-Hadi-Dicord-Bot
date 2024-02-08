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

queues = {}

def check_queue(ctx, id):
    if queues[id] != []:
        voice = ctx.guild.voice_client
        source = queues[id].pop(0)
        voice.play(source, after=lambda x=None: check_queue(ctx, id))  

@client.command()
async def clearQueue(ctx):
    guild_id = ctx.message.guild.id
    if(guild_id in queues):
        queues[guild_id] = []
        await ctx.send("Queue has been cleared")
    else:
        await ctx.send("There is no queue to clear")

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
        if message.content.lower() == "hey" or message.content.lower() == "hi" or message.content.lower() == "hello" or message.content.lower() == "sup" or message.content.lower() == "yo":
            await message.add_reaction("\U0001F44B")  # This will add a wave emoji      
        if message.content.lower() == "bye" or message.content.lower() == "goodbye" or message.content.lower() == "cya":
            await message.add_reaction("\U0001F44B")
        if message.content.lower()== "monis":
            await message.add_reaction("\U0001F435")  # This will add a monkey face emoji
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
async def play(ctx, arg):
    try:
        voice = ctx.guild.voice_client
        if voice is None:
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()
        source = FFmpegPCMAudio('music/' + arg +'.mp3')
        player = voice.play(source,after=lambda x=None: check_queue(ctx, ctx.message.guild.id)) 
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")

@client.command(pass_context = True)
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if(voice.is_playing()):
        voice.pause()
    else:
        await ctx.send("I am not playing anything")

@client.command(pass_context = True)
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if(voice.is_paused()):
        voice.resume()
    else:
        await ctx.send("I am not playing anything")

@client.command(pass_context = True)
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()

@client.command(pass_context = True)
async def volume(ctx, volume: int):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if(voice.is_playing()):
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = volume / 100
        await ctx.send(f"Volume has been set to {volume}%")
    else:
        await ctx.send("I am not playing anything")

@client.command(pass_context = True)
async def queue(ctx, arg):
    voice = ctx.guild.voice_client
    song = 'music/' + arg +'.mp3'
    source = FFmpegPCMAudio(song)

    guild_id = ctx.message.guild.id

    if(guild_id in queues):
        queues[guild_id].append(source)
    else:
        queues[guild_id] = [source]
    await ctx.send(f"{arg} has been added to the queue")

@client.command(pass_context=True)
async def skip(ctx):
    voice = ctx.guild.voice_client
    if voice.is_playing():
        voice.stop()
        # If there are more songs in the queue, start playing the next one
        if queue:
            source = FFmpegPCMAudio('music/' + queue.pop(0) + '.mp3')
            voice.play(source)


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
@client.command()
async def unban(ctx, *, member):    
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"{user.mention} has been unbanned")
            return
@unban.error
async def kick_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send("You do not have that power to unban. **I AM HADII**")

@client.command()
async def mute (ctx, member: discord.Member):
    try:
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.add_roles(role)
        await ctx.send(f"{member.mention} has been muted")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

#Quote Command
@client.command()
async def quote(ctx):
    await ctx.send(getResponce())

@client.command()
async def feed_me(ctx):
    await ctx.send(":banana:")  # Replace "emoji_name" and "emoji_id" with your emoji's name and ID

client.run(Bot_Token)
