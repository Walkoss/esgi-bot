import discord
from esgi_bot.users import get_user
from esgi_bot.errors import ValueNotFoundError


async def courses_support(message, bot):
    scraper = get_user(message.author.id)
    if scraper:
        try:
            embed = discord.Embed(colour=0x217bb1)
            embed.set_footer(text="Scrapped from MyGES",
                             icon_url="https://www.myges.fr/assets/img/icons/favicon.png")
            courses_support = scraper.get_last_course_supports()
            for name, link in courses_support.items():
                embed.add_field(name="Name", value=name, inline=True)
                embed.add_field(name="Link", value=link, inline=True)
                await bot.send_message(message.channel, embed=embed)
                embed.clear_fields()
        except ValueNotFoundError as e:
            await bot.send_message(message.channel, str(e))
