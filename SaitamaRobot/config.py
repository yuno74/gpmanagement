# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open('{}/SaitamaRobot/{}'.format(os.getcwd(), config),
              'r') as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    #Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 2566765  # integer value, dont use ""
    API_HASH = "de1b01834ac0a3b3b6d36f5e0937e99e"
    TOKEN = "1673206007:AAEpFTeMn9qcui42BWyqyM0uP81aBtkPcE4"  #This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 1490418027  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "Arata74"
    SUPPORT_CHAT = 'AnimeChat74'  #Your own group for support, do not add the @
    JOIN_LOGGER = -1001456301545  #Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = -1001456301545  #Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    #RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'postgres://kirito1:123@0.0.0.0:5432/bot1'  # needed for any database modules
    LOAD = []
    NO_LOAD = []
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = "txqzRz6rp3xPEfhCgIfe_Vgp0pdPfbQJdeagtb9P183dVBpHC_O6xP2QSDeYVBOP"  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

    #OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list('elevated_users.json', 'sudos')
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list('elevated_users.json', 'devs')
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list('elevated_users.json', 'supports')
    #List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list('elevated_users.json', 'tigers')
    WOLVES = get_user_list('elevated_users.json', 'whitelists')
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  #Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = 8  # Number of subthreads to use. Set as number of threads your processor uses
    BAN_STICKER = 'CAACAgUAAxkBAAICd1-iL5mTDAN4jU5B0LZVMeDpBw-XAAIlAQACUeQRVd-ZjzEIDOBqHgQ'  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = 'RDU95J3B4T0AB46J'  # Get your API key from https://www.alphavantage.co/support/#api-key
    TIME_API_KEY = 'H150IJX04CDX'  # Get your API key from https://timezonedb.com/api
    WALL_API = 'awoo'  #For wallpapers, get one from https://wall.alphacoders.com/api.php
    AI_API_KEY = 'b98ff117c9d1de9e5c8d4f531eb1987863a93c499b46506332bbdff5283205e4248a2f1c333e3fb3aa26da689db110ab197b6c7a1048c83439d33ab7352ce35c'  #For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
