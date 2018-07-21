from discord.ext import commands
from esgi_bot.users import is_authenticated


class Absence:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @is_authenticated()
    async def absences(self):
        await self.bot.say('Getting all absences')


def setup(bot):
    bot.add_cog(Absence(bot))
