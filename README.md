# ESGI Bot

ESGI Bot allows you to retrieve some information from MyGES including:
*   Your marks
*   Your projects
*   Your courses files
*   Your absences
*   and so on..

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Docker if you want to use it.


### Installing and running with Docker

Create a `.env` file which will contains all environment variables that are required by this application and edit it to set variables.

```sh
cp .env.example
<YOUR_EDITOR> .env
```

Note: this project use dialogflow so you have to set path to google credentials file (JSON) under `GOOGLE_APPLICATION_CREDENTIALS` variable.

Note also that `/opt/project` will be the base directory of this project under Docker. So put your file under this base directory and change `GOOGLE_APPLICATION_CREDENTIALS` value to `/opt/projects/google_client_secret.json`

```sh
# Build Docker image
docker build -t esgi_bot:v1 .
```

```sh
# Run application
docker run --env-file .env esgi_bot:v1
```

### Installing and running without Docker

Export all environment variables under `.env.example` into your local environment variables

`GOOGLE_APPLICATION_CREDENTIALS` must be the path to your google credentials file (JSON). e.g. `/opt/project/google_client_secret.json`

```sh
# Install requirements
pip install -r requirements.txt
```

```sh
# Install project
python setup.py install
```

```sh
# Run application
python esgi_bot/run.py
```

## Built With

* [Discord.py](https://github.com/Rapptz/discord.py) - Discord Python Library
* [Dialogflow](https://dialogflow.com) - NLP framework
* [PyCharm](https://www.jetbrains.com/pycharm/) - IDE

## Authors

* **Walid El Bouchikhi**  - [Walkoss](https://github.com/Walkoss)
* **Pierre Simon** - [Rypall](https://github.com/rypall)
* **Alexis Petrillo** - [Alexis-Petrillo](https://github.com/Alexis-Petrillo)
