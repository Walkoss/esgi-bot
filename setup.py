from setuptools import setup, find_packages

LONG_DESCRIPTION = """
    ESGI Discord BOT allows you to retrieve some information from MyGES including:
        -   Your marks
        -   Your projects
        -   Your courses files
        -   and so on..
"""

setup(
    name='esgi_bot',
    version='0.1.0',
    description='ESGI Discord BOT',
    long_description=LONG_DESCRIPTION,
    author='Walid EL BOUCHIKHI, Pierre SIMON, Alexis PETRILLO',
    author_email='walid.elbouchikhi@gmail.com',
    url='https://github.com/Walkoss/esgi-bot',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['run_bot=esgi_bot.run:run']
    },
)
