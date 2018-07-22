from discord.ext import commands
from esgi_bot.users import is_authenticated
from esgi_bot.handlers.absence import absences


class Absence:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @is_authenticated()
    async def absences(self, ctx):
        await absences(ctx.message, self.bot)


def setup(bot):
    bot.add_cog(Absence(bot))
