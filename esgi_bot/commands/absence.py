import discord
from discord.ext import commands
from esgi_bot.users import is_authenticated, get_user


class Absence:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @is_authenticated()
    async def absences(self, ctx):
        scraper = get_user(ctx.message.author.id)
        if scraper:
            absences = scraper.get_absences()
            if absences:
                embed = discord.Embed(colour=0x217bb1)
                embed.set_footer(text="Scrapped from MyGES",
                                 icon_url="https://www.myges.fr/assets/img/icons/favicon.png")
                for absence in absences:
                    embed.add_field(name="Date", value=absence["date"], inline=True)
                    embed.add_field(name="Type", value=absence["type"], inline=True)
                    embed.add_field(name="Justified", value=absence["justified"], inline=True)
                    embed.add_field(name="Subject", value=absence["subject"])
                    await self.bot.say(embed=embed)
                    embed.clear_fields()
            else:
                await self.bot.say("You don't have absence :)")


def setup(bot):
    bot.add_cog(Absence(bot))
