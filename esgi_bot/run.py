from esgi_bot import logger
from esgi_bot.scrap import *
from esgi_bot.conf import DISCORD_TOKEN
from discord.ext import commands


def run():
    bot = commands.Bot(command_prefix=commands.when_mentioned_or('!'))

    for extension in ['notes']:
        try:
            bot.load_extension(extension)
        except Exception as e:
            logger.error('{}: {}'.format(type(e).__name__, e))

    bot.run(DISCORD_TOKEN)


if __name__ == '__main__':
    run()
