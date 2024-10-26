# conftest.py
import pytest
from selenium import webdriver
import yaml


@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # Initialize ChromeDriver
    yield driver
    driver.quit()  # Close browser after each test


@pytest.fixture(scope="session")
def config():
    with open("config/config.yaml", "r") as file:
        return yaml.safe_load(file)
