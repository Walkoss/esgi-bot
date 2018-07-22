import discord
from discord.ext import commands
from esgi_bot.users import is_authenticated, get_user
from esgi_bot.errors import ValueNotFoundError


class Deadline:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @is_authenticated()
    async def deadlines(self, ctx):
        scraper = get_user(ctx.message.author.id)
        if scraper:
            embed = discord.Embed(colour=0x217bb1)
            embed.set_footer(text="Scrapped from MyGES",
                             icon_url="https://www.myges.fr/assets/img/icons/favicon.png")
            deadlines = scraper.get_last_deadlines()

            for deadline in deadlines:
                embed.add_field(name="Name", value=deadline["name"], inline=True)
                embed.add_field(name="Date", value=deadline["date"], inline=True)
            await self.bot.say(embed=embed)
            embed.clear_fields()


def setup(bot):
    bot.add_cog(Deadline(bot))
