# getenv для того чтобы достать значение переменных из .env
from os import getenv
# load_dotenv для того чтобы связать config с .env
from dotenv import load_dotenv
load_dotenv()

# Все что касается телеграм бота 
TOKEN = getenv("TOKEN")
ADMIN = getenv("ADMMIN_USER")

# Все что касается базы данных
PGHOST = getenv("PGHOST")
PGDATABASE = getenv("PGDATABASE")
PGUSER = getenv("PGUSER")
PGPASSWORD = getenv("PGPASSWORD")
PGPORT =getenv("PGPORT")

PARSURL = getenv("URL")
PARSDOMAIN = getenv("DOMAIN")

HEADERS = {
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
}

IMAGE = [
    "source/image/img1.jpg",
    "source/image/img2.jpg",
    "source/image/img3.jpeg",
    "source/image/img4.jpg",
]

