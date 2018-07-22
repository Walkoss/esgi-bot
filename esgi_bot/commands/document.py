from discord.ext import commands
from esgi_bot.users import is_authenticated
from esgi_bot.handlers.document import documents


class Document:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @is_authenticated()
    async def documents(self, ctx):
        await documents(ctx.message, self.bot)


def setup(bot):
    bot.add_cog(Document(bot))
