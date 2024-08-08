from urllib.parse import urlencode
from .config import Config

def get_auth_url():
    params = {
        "client_id": Config.CLIENT_ID,
        "redirect_uri": Config.REDIRECT_URI,
        "scope": "openid profile email",
        "response_type": "code"
    }
    auth_url = f"https://login.microsoftonline.com/common/oauth2/v2.0/authorize?{urlencode(params)}"
    return auth_url