import os

BASE_DIR = os.path.dirname(__file__)

DISCORD_TOKEN = os.environ['DISCORD_TOKEN']
DIALOGFLOW_PROJECT_ID = os.environ['DIALOGFLOW_PROJECT_ID']
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.join(BASE_DIR, '../google_client_secret.json')
