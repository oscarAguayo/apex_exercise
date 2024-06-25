import os
from typing import Final
from dotenv import load_dotenv

load_dotenv()

BASE_URL: Final[str] = os.getenv('BASE_URL')
USER_EMAIL: Final[str] = os.getenv('USER_EMAIL')
USER_PASSWORD: Final[str] = os.getenv('USER_PASSWORD')