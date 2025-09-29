from pathlib import Path
from dotenv import load_dotenv
env_path = Path(__file__).parent.parent/".env"
load_dotenv(dotenv_path=env_path)






class Settings:
    PROJECT_TITLE: str ="Blog 🚀"
    PROJECT_VERSION: str ="0.1.0 "

settings=Settings()

Path(__file__).resolve()