from discord.ext import commands
from esgi_bot.users import is_authenticated


class Teacher:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @is_authenticated()
    async def teachers(self):
        await self.bot.say('Getting all teachers')


def setup(bot):
    bot.add_cog(Teacher(bot))
