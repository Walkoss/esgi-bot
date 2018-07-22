from discord.ext import commands
from esgi_bot.users import is_authenticated
from esgi_bot.handlers.course_support import courses_support


class CourseSupport:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @is_authenticated()
    async def courses_support(self, ctx):
        await courses_support(ctx.message, self.bot)


def setup(bot):
    bot.add_cog(CourseSupport(bot))
