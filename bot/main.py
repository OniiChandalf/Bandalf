import discord
import threading
import asyncio
from bot.config import DISCORD_TOKEN, GUILD_ID

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

_loop = asyncio.new_event_loop()
asyncio.set_event_loop(_loop)

@client.event
async def on_ready():
    print(f"✅ Bot eingeloggt als {client.user}")

def bot_thread():
    _loop.create_task(client.start(DISCORD_TOKEN))
    _loop.run_forever()

async def ban_user_on_discord(user_id):
    guild = client.get_guild(GUILD_ID)
    if not guild:
        print("⚠️ Guild nicht gefunden")
        return
    try:
        member = await guild.fetch_member(user_id)
        await member.ban(reason="Gebannt über Dashboard")
        print(f"🚫 {member.name} wurde gebannt")
    except discord.NotFound:
        print("❌ User nicht auf dem Server")
    except Exception as e:
        print(f"❌ Fehler beim Bannen: {e}")
