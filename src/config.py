import os
from dotenv import load_dotenv

load_dotenv()

# Load environment variables
class Config:
    BASE_URL = os.getenv("BASE_URL")
    SSO_USERNAME = os.getenv("SSO_USERNAME")
    SSO_PASSWORD = os.getenv("SSO_PASSWORD")
    EXPECTED_TITLE = os.getenv("EXPECTED_TITLE")
    CLIENT_ID = os.getenv("CLIENT_ID")
    REDIRECT_URI = os.getenv("REDIRECT_URI")
    