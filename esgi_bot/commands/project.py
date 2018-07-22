from discord.ext import commands
from esgi_bot.users import is_authenticated
from esgi_bot.handlers.project import projects


class Project:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @is_authenticated()
    async def projects(self, ctx):
        await projects(ctx.message, self.bot)


def setup(bot):
    bot.add_cog(Project(bot))
