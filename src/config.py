import os

import dotenv


class Config:
    def __init__(self, env_file: str = ".env"):
        dotenv.load_dotenv(dotenv_path=env_file)
        self.REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")