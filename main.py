import discord
from discord.ext import commands
from openai import OpenAI

# Set up your OpenAI API key
client = OpenAI(api_key='sk-proj-8uHMLztgsIhBL9QshtAAT3BlbkFJ9s0tdHng2WUtH8YJIVVe')

# Enable privileged intents
intents = discord.Intents.default()
intents.message_content = True

# Create a new bot instance
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command()
async def challenge(ctx):
    # Use OpenAI API to generate a beginner-level C++ coding challenge
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Generate a beginner-level C++ coding challenge."}
        ],
        max_tokens=150
    )
    challenge = response.choices[0].message.content.strip()
    await ctx.send(f"**C++ Coding Challenge**\n{challenge}")

bot.run('MTI0MDg3OTcxODAwNjM5MDg3NQ.GAe-qG.D2BqtXAy17uVQaHBPvL_FbWcbskIEE-FBEPoUc')
