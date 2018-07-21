from discord.ext import commands
from esgi_bot.users import is_authenticated


class Mark:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @is_authenticated()
    async def marks(self, ctx, subject='ALL'):
        if subject == 'ALL':
            await self.bot.say('Getting all marks')
        else:
            await self.bot.say('Marks for subject {}'.format(subject))


def setup(bot):
    bot.add_cog(Mark(bot))
