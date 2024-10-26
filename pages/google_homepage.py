# pages/google_homepage.py
from selenium.webdriver.common.by import By


class GoogleHomePage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.NAME, "q")

    def load(self):
        self.driver.get("https://www.google.com")

    def search(self, query):
        self.driver.find_element(*self.search_box).send_keys(query)
        self.driver.find_element(*self.search_box).submit()
