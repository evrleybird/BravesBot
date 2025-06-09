import discord
from discord.ext import commands
from braves_score import fetch_braves_score

TOKEN = "your-bot-token-here"  # Replace with your actual token
CHANNEL_ID = 123456789012345678  # Replace with your Discord channel ID

intents = discord.Intents.default()
intents.messages = True

class BravesBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="/", intents=intents)

    async def setup_hook(self):
        await self.tree.sync()

bot = BravesBot()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Braves Score Bot is now online!")

@bot.tree.command(name="score", description="Get the current Atlanta Braves score")
async def score(interaction: discord.Interaction):
    current_score = fetch_braves_score()
    # If the score is final, don't prepend "Current Braves Score:"
    if current_score.startswith("Final Score:"):
        await interaction.response.send_message(current_score)
    else:
        await interaction.response.send_message(f"{current_score}")

if __name__ == "__main__":
    bot.run(TOKEN)