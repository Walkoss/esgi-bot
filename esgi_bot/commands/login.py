from discord.ext import commands
from esgi_bot.users import USERS
from esgi_bot.scraper import Scraper
from esgi_bot.errors import AuthError


class Login:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def login(self, ctx, login: str, password: str):
        try:
            USERS[ctx.message.author.id] = Scraper(login, password)
            await self.bot.say("You're now connected")
        except AuthError as e:
            await self.bot.say(str(e))


def setup(bot):
    bot.add_cog(Login(bot))
