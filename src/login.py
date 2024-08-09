from playwright.sync_api import Page
from .config import Config
import time

def handle_login(page: Page):
    # Start by navigating to the website
    page.goto(Config.WEBSITE_URL)
    print(f"Navigated to: {page.url}")

    time.sleep(5) # Add a sleep to allow the page to load

    # Wait for redirect to Microsoft SSO
    #page.wait_for_url("*://login.microsoftonline.com/*")
    print(f"Redirected to Microsoft SSO: {page.url}")

    # Enter email in Microsoft SSO
    page.fill('input[type="email"]', Config.SSO_USERNAME)
    page.click('input[type="submit"]')
    print("Entered email in Microsoft SSO")

    # Wait for redirect to second SSO
    time.sleep(5)
    #page.wait_for_url("*://login.windows.net/*")
    #print(f"Redirected to second SSO: {page.url}")

    # # Enter email and password in second SSO
    # page.fill('input[type="email"]', Config.SSO_USERNAME)
    # page.fill('input[type="password"]', Config.SSO_PASSWORD)
    # page.click('input[type="submit"]')
    # print("Entered email and password in second SSO")

    # Wait for redirect back to the website
    page.wait_for_url(f"{Config.WEBSITE_URL}*")
    print(f"Redirected back to website: {page.url}")

    # Wait for 5 seconds to ensure the page is fully loaded
    time.sleep(5)
    print("Waited 5 seconds for page to load")