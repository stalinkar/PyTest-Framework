# tests/web/test_google_search.py
import time

import pytest
from pages.google_homepage import GoogleHomePage


@pytest.mark.parametrize("search_term", ["OpenAI", "Python", "Selenium"])
def test_google_search(driver, search_term):
    google_page = GoogleHomePage(driver)
    google_page.load()
    google_page.search(search_term)
    time.sleep(2)
    assert search_term in driver.title
