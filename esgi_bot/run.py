from esgi_bot import logger
from esgi_bot.conf import DISCORD_TOKEN
from discord.ext import commands

COMMANDS = [
    'absence',
    'mark',
    'planning',
    'login',
    'project',
    'deadline',
    'course_support',
    'document'
]


def run():
    bot = commands.Bot(command_prefix=commands.when_mentioned_or('!'))

    for extension in ['commands.' + command for command in COMMANDS]:
        try:
            bot.load_extension(extension)
        except Exception as e:
            logger.error('{}: {}'.format(type(e).__name__, e))

    @bot.event
    async def on_command_error(error, ctx):
        if isinstance(error, commands.errors.CheckFailure):
            await bot.send_message(ctx.message.author, "You're not authenticated")

    bot.run(DISCORD_TOKEN)


if __name__ == '__main__':
    run()
