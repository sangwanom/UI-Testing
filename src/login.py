from playwright.sync_api import Page
from .config import Config
from .auth_url import get_auth_url
import time

def sso_login(page:Page):
    auth_url = get_auth_url()
    page.goto(auth_url)

    ## Entering the username
    page.wait_for_selector('input[type="email"]')
    page.fill('input[type="email"]', Config.SSO_USERNAME)
    page.click('input[type="submit"]')

    # ## Entering the password
    # page.wait_for_selector('input[type="password"]')
    # page.fill('input[type="password"]', Config.SSO_PASSWORD)
    # page.click('input[type="submit"]')

    ## Add a waiting for the redirect to complete
    page.wait_for_url(f"{Config.REDIRECT_URI}*")

    time.sleep(5) # Add a sleep to allow the redirect to complete

    ## Navigate to first tab in navigation pane
    page.click('.stNavigation button:second-child')

    page.wait_for_load_state('networkidle')

