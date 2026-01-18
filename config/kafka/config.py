import os

from dotenv import load_dotenv

# dotenv_path = Path(__file__).parent / ".env"
dotenv_path = r"C:\Users\kubaj\Desktop\Studia\VII semestr\[BLOK OBIERALNY] Big Data (3 ECTS)\backend\.env"

load_dotenv(
    dotenv_path=dotenv_path
)

KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS")

KAFKA_GROUP_ID = os.getenv("KAFKA_GROUP_ID")
