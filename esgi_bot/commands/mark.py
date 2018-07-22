import discord
from discord.ext import commands
from esgi_bot.users import is_authenticated, get_user
from esgi_bot.errors import ValueNotFoundError


class Mark:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @is_authenticated()
    async def marks(self, ctx, subject=''):
        scraper = get_user(ctx.message.author.id)
        if scraper:
            try:
                embed = discord.Embed(colour=0x217bb1)
                embed.set_footer(text="Scrapped from MyGES",
                                 icon_url="https://www.myges.fr/assets/img/icons/favicon.png")
                subjects = scraper.get_marks(subject)

                def chunks(l, n):
                    """Yield successive n-sized chunks from l."""
                    for i in range(0, len(l), n):
                        yield l[i:i + n]

                for subjects_chunk in chunks(subjects, 6):
                    for subject in subjects_chunk:
                        embed.add_field(name="__{}__".format(subject["name"]),
                                        value="`{} | Coeff: {} | ECTS: {}`".format(subject["teacher"],
                                                                                   subject["coeff"],
                                                                                   subject["ects"]),
                                        inline=False)
                        for key, value in subject["marks"].items():
                            embed.add_field(name=key, value=value)
                    await self.bot.say(embed=embed)
                    embed.clear_fields()
            except ValueNotFoundError as e:
                await self.bot.say(str(e))


def setup(bot):
    bot.add_cog(Mark(bot))
