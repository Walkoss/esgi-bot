from esgi_bot import logger
from esgi_bot.conf import DISCORD_TOKEN, DIALOGFLOW_PROJECT_ID
from discord.ext import commands
import dialogflow
import importlib

COMMANDS = [
    'absence',
    'mark',
    'planning',
    'login',
    'project',
    'deadline',
    'course_support',
    'document'
]


def run():
    bot = commands.Bot(command_prefix=commands.when_mentioned_or('!'))

    for extension in ['commands.' + command for command in COMMANDS]:
        try:
            bot.load_extension(extension)
        except Exception as e:
            logger.error('{}: {}'.format(type(e).__name__, e))

    @bot.event
    async def on_command_error(error, ctx):
        if isinstance(error, commands.errors.CheckFailure):
            await bot.send_message(ctx.message.author, "You're not authenticated")

    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return
        elif bot.user.id in message.raw_mentions:
            # Bot got mentionned
            text = message.clean_content.split(' ', 1)[1]
            session_client = dialogflow.SessionsClient()
            session = session_client.session_path(DIALOGFLOW_PROJECT_ID, message.author.id)
            text_input = dialogflow.types.TextInput(text=text, language_code='fr-FR')
            query_input = dialogflow.types.QueryInput(text=text_input)
            response = session_client.detect_intent(session=session, query_input=query_input)
            await bot.send_message(message.channel, response.query_result.fulfillment_text)
            if response.query_result.all_required_params_present and response.query_result.action:
                action = response.query_result.action.split('.')
                try:
                    if action[0] in COMMANDS:
                        module = importlib.import_module('handlers.{}'.format(action[0]))
                        func = getattr(module, action[1])
                        parameters = dict()
                        for param in response.query_result.parameters:
                            parameters[param] = response.query_result.parameters[param]
                        await func(message, bot, **parameters)
                except Exception as e:
                    logger.error('{}: {}'.format(type(e).__name__, e))
            return

        await bot.process_commands(message)

    bot.run(DISCORD_TOKEN)


if __name__ == '__main__':
    run()
