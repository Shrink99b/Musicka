from os import getenv
from dotenv import load_dotenv

load_dotenv()

que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQA4FTZ751Myg1b0DScUsIBhNdhX-312qIU3sPx1cc19TiZH6rsBCexf5K0XJf-SwpHnoc5DZfqfXT65ZUjq0z_oBxI35cruHA3oDFRXcfiq7STJQB6UOO9i7tV45ry4RDJCHqug9pCmBMqiKLRoBaHlZMqvrb_Ml-wEqK9IVKm48yFCFGVmJZadvyLKkalN4GYfK33P7aEAmcHsMZH2kMbrWIl-n4r1l-C5CuqfozON7RlcZlBxQoyKalAy9XtAc90dyMR6L3tgsh1dDqwquB9T99XqcGfV26__jEycEnsMj-x3iZl8LzoKgRYuhbFVfByTgJDGGHkYEkNAv1BFXMyle7fKQAA")
BOT_TOKEN = getenv("BOT_TOKEN","5544474027:AAG4gH91He35vMs4LMZfu_aqAhXneGzeALA")
CLONER_TOKEN = getenv("CLONER_TOKEN")
BOT_NAME = getenv("BOT_NAME","TUSHAR  X ROBOT" )
BOT_USERNAME = getenv("BOT_USERNAME","Tushar_op_bot")
ASSID = int(getenv("ASSID","2075642432"))
ASSNAME = getenv("ASSNAME","TUSHAR MUSIC")
ASSUSERNAME = getenv("ASSUSERNAME","Tushar_op_bolte")
BOT_ID = int(getenv("BOT_ID","5544474027"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
MONGO_DB_URI = getenv("MONGO_DB_URI","mongodb+srv://ziddiboy1763:ziddiboy1763@cluster0.ilw31mx.mongodb.net/?retryWrites=true&w=majority")
API_ID = int(getenv("API_ID","13791948"))
API_HASH = getenv("API_HASH","b4534a8924232e4c6bd171da36251094")
OWNER_ID = int(getenv("OWNER_ID","5099353600"))
UPDATE = getenv("UPDATE", "TheUpdatesChannel","https://t.me/hjhvvl")
SUPPORT = getenv("SUPPORT", "TheSupportChat","https://t.me/hjhvvl")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "9999"))
CMD_MUSIC = list(getenv("CMD_MUSIC", "/ !").split())
BG_IMG = getenv("BG_IMG", "https://telegra.ph/file/f2a2d31f60a9e0f3dbe94.png")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5099353600").split()))
START_PIC = getenv("START_PIC", "https://telegra.ph/file/f2a2d31f60a9e0f3dbe94.png")
OWNER_USERNAME = getenv("OWNER_USERNAME")
IMG_1 = "https://telegra.ph/file/3505f3c0abf6008b3f6b9.jpg"
