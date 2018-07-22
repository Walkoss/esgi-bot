import discord
from esgi_bot.users import get_user
from esgi_bot.errors import ValueNotFoundError


async def planning(message, bot):
    scraper = get_user(message.author.id)
    if scraper:
        try:
            embed = discord.Embed(colour=0x217bb1)
            embed.set_footer(text="Scrapped from MyGES",
                             icon_url="https://www.myges.fr/assets/img/icons/favicon.png")
            planning_link = scraper.get_last_planning()

            embed.add_field(name="Planning link",
                            value=planning_link)
            await bot.send_message(message.channel, embed=embed)
        except ValueNotFoundError as e:
            await bot.send_message(message.channel, str(e))
