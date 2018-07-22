from discord.ext import commands
from esgi_bot.users import is_authenticated
from esgi_bot.handlers.mark import marks


class Mark:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @is_authenticated()
    async def marks(self, ctx, subject=''):
        await marks(ctx.message, self.bot, subject)


def setup(bot):
    bot.add_cog(Mark(bot))
