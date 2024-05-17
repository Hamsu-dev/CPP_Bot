import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Set up your OpenAI API key
openai_api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=openai_api_key)

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
    usage = response.usage

    # Send the challenge and usage information
    await ctx.send(f"**C++ Coding Challenge**\n{challenge}\n\n**Usage**\nPrompt tokens: {usage.prompt_tokens}\nCompletion tokens: {usage.completion_tokens}\nTotal tokens: {usage.total_tokens}")

bot.run(os.getenv('DISCORD_BOT_TOKEN'))
