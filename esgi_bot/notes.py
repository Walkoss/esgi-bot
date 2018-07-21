from discord.ext import commands


class Notes:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def marks(self, subject='ALL'):
        if subject == 'ALL':
            await self.bot.say('Getting all marks')
        else:
            await self.bot.say('Marks for subject {}'.format(subject))


def setup(bot):
    bot.add_cog(Notes(bot))
