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
OWNER_NAME = getenv("OWNER_NAME", "@Q_X_I_T")
ALIVE_NAME = getenv("ALIVE_NAME", "FIRE")
BOT_USERNAME = getenv("BOT_USERNAME", "fir_musbot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Q_X_I_O")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "supfire205")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "BU_QH")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/f23ca2711643da6f61eb3.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "50000"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/levina-lab/video-stream")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/f23ca2711643da6f61eb3.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/f23ca2711643da6f61eb3.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f23ca2711643da6f61eb3.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/f23ca2711643da6f61eb3.jpg")
