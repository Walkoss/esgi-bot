from discord.ext import commands
from esgi_bot.users import is_authenticated
from esgi_bot.handlers.planning import planning


class Planning:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @is_authenticated()
    async def planning(self, ctx):
        await planning(ctx.message, self.bot)


def setup(bot):
    bot.add_cog(Planning(bot))
