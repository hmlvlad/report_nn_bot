import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
root_path = os.path.dirname(os.path.abspath(__file__))


def get_path(*path):
    return os.path.join(root_path, *path)
