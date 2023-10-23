from os import environ

from logging import getLogger, FileHandler, StreamHandler, INFO, basicConfig

from dotenv import load_dotenv

from telegram import Bot

from telegram.ext import Updater as tgUpdater

from faulthandler import enable as faulthandler_enable

faulthandler_enable()

basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',

                    handlers=[FileHandler('log.txt'), StreamHandler()],

                    level=INFO)

LOGGER = getLogger(__name__)

load_dotenv('config.env', override=True)

def getConfig(name: str):

    return environ[name]

SUDO_USERS = set()

try:

    aid = getConfig('SUDO_USERS')

    aid = aid.split(' ')

    for _id in aid:

        SUDO_USERS.add(int(_id))

except:

    pass

try:

    BOT_TOKEN = getConfig('BOT_TOKEN')

    OWNER_ID = int(getConfig('OWNER_ID'))

    TELEGRAM_API = getConfig('TELEGRAM_API')

    TELEGRAM_HASH = getConfig('TELEGRAM_HASH')

except:

    LOGGER.error("One or more env variables missing! Exiting now")

    exit(1)

bot = Bot(token='BOT_TOKEN') # Replace 'YOUR_BOT_TOKEN' with your actual Telegram bot token

bot.request.read_timeout = 20
bot.request.connect_timeout = 15

updater = Updater(bot=bot, request_kwards=defaults)

bot = updater.bot

dispatcher = updater.dispatcher

job_queue = updater.job_queue
