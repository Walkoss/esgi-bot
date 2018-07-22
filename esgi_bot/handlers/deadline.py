import discord
from esgi_bot.users import get_user


async def deadlines(message, bot):
    scraper = get_user(message.author.id)
    if scraper:
        embed = discord.Embed(colour=0x217bb1)
        embed.set_footer(text="Scrapped from MyGES",
                         icon_url="https://www.myges.fr/assets/img/icons/favicon.png")
        deadlines = scraper.get_last_deadlines()

        for deadline in deadlines:
            embed.add_field(name="Name", value=deadline["name"], inline=True)
            embed.add_field(name="Date", value=deadline["date"], inline=True)
        await bot.send_message(message.channel, embed=embed)
        embed.clear_fields()
