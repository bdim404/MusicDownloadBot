from dotenv import load_dotenv
import logging,os

# Configure the logging;
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logging.info("Loading the environment variables...")

# Load the environment variables;
load_dotenv()

# Get the environment variables;
try:
    TELEGRAM_BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
    logging.info(f"TELEGRAM_BOT_TOKEN: {TELEGRAM_BOT_TOKEN}")
except:
    logging.error("The TELEGRAM_BOT_TOKEN environment variable is not set.")
    exit(1)
if not TELEGRAM_BOT_TOKEN:
    logging.error("The TELEGRAM_BOT_TOKEN environment variable is empty.")
    exit(1)

try:
    ADMIN_USER_IDS = list(map(int, os.getenv("ADMIN_USER_IDS").split(",")))
    logging.info(f"ADMIN_USER_IDS: {ADMIN_USER_IDS}")
except:
    logging.error("The ADMIN_USER_IDS environment variable is not set.")
    exit(1)
if not ADMIN_USER_IDS:
    logging.error("The ADMIN_USER_IDS environment variable is empty.")
    exit(1)


try:
    ALLOWED_TELEGRAM_USER_IDS = list(map(int, os.getenv("ALLOWED_TELEGRAM_USER_IDS").split(",")))
    logging.info(f"ALLOWED_TELEGRAM_USER_IDS: {ALLOWED_TELEGRAM_USER_IDS}")
except:
    ALLOWED_TELEGRAM_USER_IDS = []

if not ALLOWED_TELEGRAM_USER_IDS:
    logging.error("The ALLOWED_TELEGRAM_USER_IDS environment variable is empty.")
    exit(1)

try:
    COOKIES_LOCATION = os.getenv("COOKIES_LOCATION")
    logging.info(f"COOKIES_LOCATION: {COOKIES_LOCATION}")
except:
    logging.error("The COOKIES_LOCATION environment variable is not set.")
    exit(1)
if not COOKIES_LOCATION:
    logging.error("The COOKIES_LOCATION environment variable is empty.")
    exit(1)

try:
    WVD_LOCATION = os.getenv("WVD_LOCATION")
    logging.info(f"WVD_LOCATION: {WVD_LOCATION}")
except:
    logging.error("The WVD_LOCATION environment variable is not set.")
    exit(1)
if not WVD_LOCATION:
    logging.error("The WVD_LOCATION environment variable is empty.")
    exit(1)

try:
    SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
    logging.info(f"SPOTIPY_CLIENT_ID: {SPOTIPY_CLIENT_ID}")
except:
    logging.error("The SPOTIPY_CLIENT_ID environment variable is not set.")
    exit(1)
if not SPOTIPY_CLIENT_ID:
    logging.error("The SPOTIPY_CLIENT_ID environment variable is empty.")
    exit(1)

try:
    SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
    logging.info(f"SPOTIFY_CLIENT_SECRET: {SPOTIFY_CLIENT_SECRET}")
except:
    logging.error("The SPOTIPY_CLIENT_SECRET environment variable is not set.")
    exit(1)
if not SPOTIFY_CLIENT_SECRET:
    logging.error("The SPOTIFY_CLIENT_SECRET environment variable is empty.")
    exit(1)

try:
    TELEGRAM_CHANNEL_ID = os.getenv("TELEGRAM_CHANNEL_ID")
    logging.info(f"TELEGRAM_CHANNEL_ID: {TELEGRAM_CHANNEL_ID}")
except:
    logging.error("The TELEGRAM_CHANNEL_ID environment variable is not set.")
    exit(1)
if not TELEGRAM_CHANNEL_ID:
    logging.error("The TELEGRAM_CHANNEL_ID environment variable is empty.")
    exit(1)


logging.info("Environment variables loaded.")
# Set the Apple Music API hostname; 
AMP_API_HOSTNAME = "https://amp-api.music.apple.com"

# Set the Apple Music API endpoints;
MP4_TAGS_MAP = {
    "album": "\xa9alb",
    "album_artist": "aART",
    "album_id": "plID",
    "album_sort": "soal",
    "artist": "\xa9ART",
    "artist_id": "atID",
    "artist_sort": "soar",
    "comment": "\xa9cmt",
    "composer": "\xa9wrt",
    "composer_id": "cmID",
    "composer_sort": "soco",
    "copyright": "cprt",
    "date": "\xa9day",
    "genre": "\xa9gen",
    "genre_id": "geID",
    "lyrics": "\xa9lyr",
    "media_type": "stik",
    "rating": "rtng",
    "storefront": "sfID",
    "title": "\xa9nam",
    "title_id": "cnID",
    "title_sort": "sonm",
    "xid": "xid ",
}

# Set the Apple Music Storefront IDs;
STOREFRONT_IDS = {
    "AE": "143481-2,32",
    "AG": "143540-2,32",
    "AI": "143538-2,32",
    "AL": "143575-2,32",
    "AM": "143524-2,32",
    "AO": "143564-2,32",
    "AR": "143505-28,32",
    "AT": "143445-4,32",
    "AU": "143460-27,32",
    "AZ": "143568-2,32",
    "BB": "143541-2,32",
    "BE": "143446-2,32",
    "BF": "143578-2,32",
    "BG": "143526-2,32",
    "BH": "143559-2,32",
    "BJ": "143576-2,32",
    "BM": "143542-2,32",
    "BN": "143560-2,32",
    "BO": "143556-28,32",
    "BR": "143503-15,32",
    "BS": "143539-2,32",
    "BT": "143577-2,32",
    "BW": "143525-2,32",
    "BY": "143565-2,32",
    "BZ": "143555-2,32",
    "CA": "143455-6,32",
    "CG": "143582-2,32",
    "CH": "143459-57,32",
    "CL": "143483-28,32",
    "CN": "143465-19,32",
    "CO": "143501-28,32",
    "CR": "143495-28,32",
    "CV": "143580-2,32",
    "CY": "143557-2,32",
    "CZ": "143489-2,32",
    "DE": "143443-4,32",
    "DK": "143458-2,32",
    "DM": "143545-2,32",
    "DO": "143508-28,32",
    "DZ": "143563-2,32",
    "EC": "143509-28,32",
    "EE": "143518-2,32",
    "EG": "143516-2,32",
    "ES": "143454-8,32",
    "FI": "143447-2,32",
    "FJ": "143583-2,32",
    "FM": "143591-2,32",
    "FR": "143442-3,32",
    "GB": "143444-2,32",
    "GD": "143546-2,32",
    "GH": "143573-2,32",
    "GM": "143584-2,32",
    "GR": "143448-2,32",
    "GT": "143504-28,32",
    "GW": "143585-2,32",
    "GY": "143553-2,32",
    "HK": "143463-45,32",
    "HN": "143510-28,32",
    "HR": "143494-2,32",
    "HU": "143482-2,32",
    "ID": "143476-2,32",
    "IE": "143449-2,32",
    "IL": "143491-2,32",
    "IN": "143467-2,32",
    "IS": "143558-2,32",
    "IT": "143450-7,32",
    "JM": "143511-2,32",
    "JO": "143528-2,32",
    "JP": "143462-9,32",
    "KE": "143529-2,32",
    "KG": "143586-2,32",
    "KH": "143579-2,32",
    "KN": "143548-2,32",
    "KR": "143466-13,32",
    "KW": "143493-2,32",
    "KY": "143544-2,32",
    "KZ": "143517-2,32",
    "LA": "143587-2,32",
    "LB": "143497-2,32",
    "LC": "143549-2,32",
    "LK": "143486-2,32",
    "LR": "143588-2,32",
    "LT": "143520-2,32",
    "LU": "143451-2,32",
    "LV": "143519-2,32",
    "MD": "143523-2,32",
    "MG": "143531-2,32",
    "MK": "143530-2,32",
    "ML": "143532-2,32",
    "MN": "143592-2,32",
    "MO": "143515-45,32",
    "MR": "143590-2,32",
    "MS": "143547-2,32",
    "MT": "143521-2,32",
    "MU": "143533-2,32",
    "MW": "143589-2,32",
    "MX": "143468-28,32",
    "MY": "143473-2,32",
    "MZ": "143593-2,32",
    "NA": "143594-2,32",
    "NE": "143534-2,32",
    "NG": "143561-2,32",
    "NI": "143512-28,32",
    "NL": "143452-10,32",
    "NO": "143457-2,32",
    "NP": "143484-2,32",
    "NZ": "143461-27,32",
    "OM": "143562-2,32",
    "PA": "143485-28,32",
    "PE": "143507-28,32",
    "PG": "143597-2,32",
    "PH": "143474-2,32",
    "PK": "143477-2,32",
    "PL": "143478-2,32",
    "PT": "143453-24,32",
    "PW": "143595-2,32",
    "PY": "143513-28,32",
    "QA": "143498-2,32",
    "RO": "143487-2,32",
    "RU": "143469-16,32",
    "SA": "143479-2,32",
    "SB": "143601-2,32",
    "SC": "143599-2,32",
    "SE": "143456-17,32",
    "SG": "143464-19,32",
    "SI": "143499-2,32",
    "SK": "143496-2,32",
    "SL": "143600-2,32",
    "SN": "143535-2,32",
    "SR": "143554-2,32",
    "ST": "143598-2,32",
    "SV": "143506-28,32",
    "SZ": "143602-2,32",
    "TC": "143552-2,32",
    "TD": "143581-2,32",
    "TH": "143475-2,32",
    "TJ": "143603-2,32",
    "TM": "143604-2,32",
    "TN": "143536-2,32",
    "TR": "143480-2,32",
    "TT": "143551-2,32",
    "TW": "143470-18,32",
    "TZ": "143572-2,32",
    "UA": "143492-2,32",
    "UG": "143537-2,32",
    "US": "143441-1,32",
    "UY": "143514-2,32",
    "UZ": "143566-2,32",
    "VC": "143550-2,32",
    "VE": "143502-28,32",
    "VG": "143543-2,32",
    "VN": "143471-2,32",
    "YE": "143571-2,32",
    "ZA": "143472-2,32",
    "ZW": "143605-2,32",
}