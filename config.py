import os
from dotenv import load_dotenv

# Load .env into environment variables
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL environment variable not set")

APP_NAME = "mypasskeys"
