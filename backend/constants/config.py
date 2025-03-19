import os
from dotenv import load_dotenv

# Load environment variables at once.
load_dotenv()

# Open API Key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Dropbox Keys
DBX_APP_KEY = os.getenv('DBX_APP_KEY')
DBX_APP_SECRET = os.getenv('DBX_APP_SECRET')
DBX_TOKEN_FILE = os.getenv('DBX_TOKEN_FILE')

# Database Keys
DB_CONNECTION_STR = os.getenv('DB_CONNECTION_STR')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')

# JWT keys
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')


if not OPENAI_API_KEY:
    raise ValueError('OpenAI api key not found in .env file.')

if not DBX_APP_KEY:
    raise ValueError('Dropbox App key not found in .env file.')

if not DBX_APP_SECRET:
    raise ValueError('Dropbox App secret not found in .env file.')

if not DBX_TOKEN_FILE:
    raise ValueError('Dropbox Token file not found in .env file.')

if not DB_CONNECTION_STR:
    raise ValueError('Database Connection string not found in .env file.')

if not DB_NAME:
    raise ValueError('Database Name not found in .env file.')

if not DB_USER:
    raise ValueError('Database Username not found in .env file.')

if not DB_PASSWORD:
    raise ValueError('Database Password not found in .env file.')

if not DB_HOST:
    raise ValueError('Database Host not found in .env file.')

if not JWT_SECRET_KEY:
    raise ValueError('JWT secret key not found in .env file.')
