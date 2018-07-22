import discord
from discord.ext import commands
from esgi_bot.users import is_authenticated, get_user
from esgi_bot.errors import ValueNotFoundError


class CourseSupport:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @is_authenticated()
    async def courses_support(self, ctx):
        scraper = get_user(ctx.message.author.id)
        if scraper:
            try:
                embed = discord.Embed(colour=0x217bb1)
                embed.set_footer(text="Scrapped from MyGES",
                                 icon_url="https://www.myges.fr/assets/img/icons/favicon.png")
                courses_support = scraper.get_last_course_supports()
                for name, link in courses_support.items():
                    embed.add_field(name="Name", value=name, inline=True)
                    embed.add_field(name="Link", value=link, inline=True)
                    await self.bot.say(embed=embed)
                    embed.clear_fields()
            except ValueNotFoundError as e:
                await self.bot.say(str(e))


def setup(bot):
    bot.add_cog(CourseSupport(bot))
