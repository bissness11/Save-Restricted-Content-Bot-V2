# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "6534707"))
API_HASH = getenv("API_HASH", "4bcc61d959a9f403b2f20149cbbe627a")
BOT_TOKEN = getenv("BOT_TOKEN", "5502855202:AAGW3MYUov5Gb2wWgpcaNTgxDjZ98IFh4P8")
OWNER_ID = int(getenv("OWNER_ID", "1430593323"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "mongodb+srv://bissness958:lsYsQQByKXaOPRUP@cluster0.dj7yv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = int(getenv("LOG_GROUP", "-1001843564893"))
FORCESUB = getenv("FORCESUB", "Animecolony")
