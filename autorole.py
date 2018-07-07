import discord
from discord.ext import commands

TOKEN = 'NDY0OTI4MDQwNjI4MjU2NzY5.DiGFiQ.lQkJXOok9fXccEg8O4L6-12DBfs'

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='Verified')
    await client.add_roles(member, role)

@client.command(pass_context=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount) + 1):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say('Message deleted.')

client.run(TOKEN)
