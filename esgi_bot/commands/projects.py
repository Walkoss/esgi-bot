import discord
from discord.ext import commands
from esgi_bot.users import is_authenticated, get_user
from esgi_bot.errors import ValueNotFoundError


class Project:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @is_authenticated()
    async def projects(self, ctx):
        scraper = get_user(ctx.message.author.id)
        if scraper:
            try:
                embed = discord.Embed(colour=0x217bb1)
                embed.set_footer(text="Scrapped from MyGES",
                                 icon_url="https://www.myges.fr/assets/img/icons/favicon.png")
                projects = scraper.get_projects()

                def chunks(l, n):
                    """Yield successive n-sized chunks from l."""
                    for i in range(0, len(l), n):
                        yield l[i:i + n]

                for projects_chunk in chunks(projects, 6):
                    for project in projects_chunk:
                        embed.add_field(name="Subject", value=project["subject"], inline=True)
                        embed.add_field(name="Title", value=project["title"], inline=True)
                        embed.add_field(name="Syllabus", value=project["syllabus"])
                        embed.add_field(name="Manage", value=project["manage_url"])
                    await self.bot.say(embed=embed)
                    embed.clear_fields()
            except ValueNotFoundError as e:
                await self.bot.say(str(e))


def setup(bot):
    bot.add_cog(Project(bot))
