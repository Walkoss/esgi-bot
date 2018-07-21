from discord.ext import commands

# This dictionary will contains all user registered to MyGES
# key = discord_client_id
# value = Scraper object with user's session stored
USERS = dict()


def get_user(discord_client_id: str):
    """
    Return Scraper object for the authenticated user
    :param discord_client_id:
    :return:
    """
    return USERS.get(discord_client_id)


def is_authenticated():
    def predicate(ctx):
        if get_user(ctx.message.author.id):
            return True
        return False

    return commands.check(predicate)
