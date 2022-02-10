import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Video Stream")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "The_Death_Soul")
ALIVE_NAME = getenv("ALIVE_NAME", "ιτ'ѕ нυѕѕαιи")
BOT_USERNAME = getenv("BOT_USERNAME", "Zara_Vcbot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Zain_Assistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Love_Dear_Comrades")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "ZaraSupport")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/The-Death-Soul-Robot/Zara-Videostream")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/ad86626774492a0d3d255.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/8123d3f102c582480e953.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/8123d3f102c582480e953.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/8123d3f102c582480e953.jpg")
