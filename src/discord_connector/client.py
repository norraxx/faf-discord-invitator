
import discord

import config

client = discord.Client()


@client.event
async def on_ready():
    print('Logged on as', client.user)
    print(client.guilds)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'ping':
        await message.channel.send('pong')

    command, args = (message.content + " ").split(" ", 1)

    if command == 'create':
        guild: discord.client.Guild = client.guilds[0]
        role = None
        everyone = None

        for guild_role in guild.roles:
            if guild_role.name == "player":
                role = guild_role

        channel: discord.channel.VoiceChannel = await guild.create_voice_channel(
            args,
            overwrites={"id": role.id, "type": "role", "allow": 0, "deny": 1048576},
            category=guild.categories[1]
        )

    if command == "remove":
        guild: discord.client.Guild = client.guilds[0]
        for channel in guild.channels:
            if channel.name == args:
                await channel.delete(reason="end")
    # TODO: make proper rights


client.run(config.DISCORD_TOKEN)
