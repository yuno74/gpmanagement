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

    API_ID = 1669770  # integer value, dont use ""
    API_HASH = "05c5b9c075375e5199f684d86f165829"
    TOKEN = "BOT_TOKEN"  #This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 1290773503  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "Yuno74"
    SUPPORT_CHAT = 'AnimeChat74'  #Your own group for support, do not add the @
    JOIN_LOGGER = -1001456301545  #Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = -1001456301545  #Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    #RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'postgres://kirito:1234@0.0.0.0:5432/bot'  # needed for any database modules
    LOAD = []
    NO_LOAD = []
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = ""  # go to support.spamwat.ch to get key
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
    AI_API_KEY = '0bb17f78ca4cf24468b6aa43897ba928b548bc7d11ea6eb3d99d5aa20f41c85571ca825c1279b47c9f816d9e1e413cb6eb5480e39f6ae407df106809b8df7454'  #For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
