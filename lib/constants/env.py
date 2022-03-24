from dotenv import load_dotenv
from os import environ

load_dotenv(".env")

DRIVER_EXEC_PATH  = environ.get("DRIVER_EXEC_PATH", None)
DRIVER_USER_AGENT = environ.get("DRIVER_USER_AGENT", None)