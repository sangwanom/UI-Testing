from playwright.sync_api import sync_playwright
from src.login import sso_login
from src.config import Config

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        sso_login(page)
        print(f"Title: {page.title()}")
        assert page.title() == Config.EXPECTED_TITLE, f"Expected title: {Config.EXPECTED_TITLE}, but got: {page.title()}"
        
        print(f"Test passed! Page title is: {page.title()}" )
        browser.close()


if __name__ == "__main__":
    main()