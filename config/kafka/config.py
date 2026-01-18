import os
from pathlib import Path

from dotenv import load_dotenv

dotenv_path = Path.cwd() / ".env"

load_dotenv(
    dotenv_path=dotenv_path
)

KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS")

KAFKA_GROUP_ID = os.getenv("KAFKA_GROUP_ID")
