import config
from discord.ext import commands


# https://discord.gg/asZSYa   rainbow_land invite link

client = commands.Bot('!')


@client.event
async def on_ready():
    """
    Prints a message if the bot is ready to work
    :return:
    """
    print('Bot is ready')


@client.command()
async def bought(msg):
    trades_channel = client.get_channel(config.trades_channel_id)
    # Buy
    if msg.message.content.startswith('!bought'):
        await trades_channel.send(f'{msg.author.mention} just scooped up ${msg.message.content.split(" ")[1].upper()} '
                                  f'at {msg.message.content.split(" ")[2]}')


@client.command()
async def sold(msg):
    trades_channel = client.get_channel(config.trades_channel_id)
    if msg.message.content.startswith('!sold'):
        await trades_channel.send(f'{msg.author.mention} just dumped ${msg.message.content.split(" ")[1].upper()}'
                                  f' at {msg.message.content.split(" ")[2]}')


client.run(config.bot_key)    # Bot token
