import discord
from discord.ext import commands
from esgi_bot.users import is_authenticated, get_user
from esgi_bot.errors import ValueNotFoundError


class Planning:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @is_authenticated()
    async def planning(self, ctx):
        scraper = get_user(ctx.message.author.id)
        if scraper:
            try:
                embed = discord.Embed(colour=0x217bb1)
                embed.set_footer(text="Scrapped from MyGES",
                                 icon_url="https://www.myges.fr/assets/img/icons/favicon.png")
                planning_link = scraper.get_last_planning()

                embed.add_field(name="Planning link",
                                value=planning_link)
                await self.bot.say(embed=embed)
            except ValueNotFoundError as e:
                await self.bot.say(str(e))


def setup(bot):
    bot.add_cog(Planning(bot))
