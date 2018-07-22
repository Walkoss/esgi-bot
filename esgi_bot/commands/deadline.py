from discord.ext import commands
from esgi_bot.users import is_authenticated
from esgi_bot.handlers.deadline import deadlines


class Deadline:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @is_authenticated()
    async def deadlines(self, ctx):
        await deadlines(ctx.message, self.bot)


def setup(bot):
    bot.add_cog(Deadline(bot))
