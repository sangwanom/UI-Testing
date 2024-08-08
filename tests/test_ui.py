import pytest
from playwright.sync_api import Page, expect
from src.login import sso_login
from src.config import Config

##@pytest.mark.usefixtures("playwright")
@pytest.fixture(scope="module")
def authenticated_page(page: Page):
    sso_login(page)
    return page

def test_page_title(authenticated_page: Page):
    expect(authenticated_page.title()).to_equal(Config.EXPECTED_TITLE)