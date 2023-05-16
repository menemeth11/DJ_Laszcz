import discord

import os # default module     //do env
from dotenv import load_dotenv #do env
load_dotenv() # load all the variables from the env file

bot = discord.Bot(intents=discord.Intents.all()) #nawiasy dają dostęp do eventow discorda


#------------------------------------------------------------------------#

@bot.event #Sends a message to console on start
async def on_ready():
    print(f"{bot.user} starts the party!")
    print("Version: Pre-alpha 0.1")

#------------------------------------------------------------------------#



@bot.event #New user gets a pm upon joining server 
async def on_member_join(member):
    await member.send(
        f'Welcome to the **{member.guild.name}**, {member.mention}! I believe you have a strong mind :D'
    )

# @bot.event   you can't send messages without a shared server
# async def on_member_remove(member):
#     await member.send(
#         f'You are so disgustingly weak {member.mention}. Never go back to {member.guild.name}! Tfu!'
#     )

#------------------------------------------------------------------------#

#------------------------------------------------------------------------#


@bot.command() #pisze o grze i czeka na odpowiedź
async def gtn(ctx):
    """A Slash Command to play a Guess-the-Number game."""

    await ctx.respond('Guess a number between 1 and 10.')
    guess = await bot.wait_for('message', check=lambda message: message.author == ctx.author)

    if int(guess.content) == 5:
        await ctx.send('You guessed it!')
    else:
        await ctx.send('Nope, try again.')

@bot.slash_command(name = "hello", description = "Say hello to the bot")
async def hello(ctx):
    await ctx.respond("Hey!")

@bot.command(description="Sends the bot's latency.") # this decorator makes a slash command
async def ping(ctx): # a slash command will be created with the name "ping"
    await ctx.respond(f"Pong! Latency is {bot.latency}")

@bot.command() #OP OP OP nazwy/opisy zmiennych 
# pycord will figure out the types for you
async def add(ctx, first: discord.Option(int), second: discord.Option(int)):
  # you can use them as they were actual integers
  sum = first + second
  await ctx.respond(f"The sum of {first} and {second} is {sum}.")

# @bot.message_command(name="Get Message ID")  # creates a global message command. use guild_ids=[] to create guild-specific commands.
# async def get_message_id(ctx, message: discord.Message):  # message commands return the message
#     await ctx.respond(f"Message ID: `{message.id}`")

# @bot.user_command(name="Account Creation Date", guild_ids=[...])  # create a user command for the supplied guilds
# async def account_creation_date(ctx, member: discord.Member):  # user commands return the member
#     await ctx.respond(f"{member.name}'s account was created on {member.created_at}")

# embed = discord.Embed(
#         title="My Amazing Embed",
#         description="Embeds are super easy, barely an inconvenience.",
#         color=discord.Colour.blurple(),
#     )

bot.run(os.getenv('TOKEN')) # run the bot with the token