import discord
import random
import os


class Bot(discord.Client):
    client = discord.Client()

    def __init__(self, token: str, **options):
        super().__init__(**options)
        self.TOKEN = token

    @client.event
    async def on_ready(self):
        print("Login Success")

    @client.event
    async def on_message(self, message: discord.Message):
        replyList = [
            '<:anikoCute:844821652709965834>',
            '<:anikoHello:844821710498955264>',
            '<:anikoLove:844821610515136552>',
            '<:anikoTasukete:844821667490299915>',
            '<:anikodayo:844821688583454730>'
        ]

        if message.author.bot:
            return
        else:
            reply = random.choice(replyList)
            await message.channel.send(reply)


if __name__ == "__main__":
    TOKEN = os.getenv('DISCORD_BOT_TOKEN')
    bot = Bot(token=TOKEN)
    bot.run(bot.TOKEN)
