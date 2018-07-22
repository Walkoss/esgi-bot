import discord
from esgi_bot.users import get_user


async def absences(message, bot):
    scraper = get_user(message.author.id)
    if scraper:
        absences = scraper.get_absences()
        embed = discord.Embed(colour=0x217bb1)
        embed.set_footer(text="Scrapped from MyGES",
                         icon_url="https://www.myges.fr/assets/img/icons/favicon.png")
        if absences:
            for absence in absences:
                embed.add_field(name="Date", value=absence["date"], inline=True)
                embed.add_field(name="Type", value=absence["type"], inline=True)
                embed.add_field(name="Justified", value=absence["justified"], inline=True)
                embed.add_field(name="Subject", value=absence["subject"])
                await bot.send_message(message.channel, embed=embed)
                embed.clear_fields()
        else:
            embed.title = "GG You have no absence yet !"
            embed.set_image(url="https://media.giphy.com/media/l0MYJnJQ4EiYLxvQ4/giphy.gif")
            await bot.send_message(message.channel, embed=embed)
