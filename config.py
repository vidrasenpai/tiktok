# (©)Codexbotz
# Recode by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de

import logging
import os
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv("config.env")

# Bot token dari @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5709794720:AAFZYXjbV52ryx_KmTQRzUdgQEvc5m7sKk4")

# API ID Anda dari my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "7375040"))

# API Hash Anda dari my.telegram.org
API_HASH = os.environ.get("API_HASH", "4166e18db5a7880136d41ceb0aa20971")

# ID Channel Database
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001870420030"))

# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5574755137"))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "onlybtpm")

# Database
DB_URI = os.environ.get("DATABASE_URL", "postgres://xhmvgrqs:TLFacIu6tb24LfQrkg9ePfj2dB-9g4gZ@satao.db.elephantsql.com/xhmvgrqs")

# Username CH & Group
CHANNEL = os.environ.get("asupantiktokbokep")

# ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001594601781"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Pesan Awalan /start
START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>Hello {first}</b>\n\n<b>Saya dapat menyimpan file pribadi di Channel Tertentu dan pengguna lain dapat mengaksesnya dari link khusus.</b>",
)
try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "").split())]
except ValueError:
    raise Exception("Daftar Admin Anda tidak berisi User ID Telegram yang valid.")

# Pesan Saat Memaksa Subscribe
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "<b>Hello {first}\n\nAnda harus bergabung di Channel saya Terlebih dahulu untuk Melihat File yang saya Bagikan\n\nSilakan Join Ke Channel Terlebih Dahulu</b>",
)

# Atur Teks Kustom Anda di sini, Simpan (None) untuk Menonaktifkan Teks Kustom
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Setel True jika Anda ingin Menonaktifkan tombol Bagikan Kiriman Saluran Anda
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == "True"

ADMINS.append(OWNER_ID)
ADMINS.append(1880970848)
ADMINS.append(1819982256)
ADMINS.append(2108493355)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
