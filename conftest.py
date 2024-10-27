# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import yaml


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode for CI environments
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # Initialize ChromeDriver without directly passing the executable path
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()  # Close browser after each test


@pytest.fixture(scope="session")
def config():
    with open("config/config.yaml", "r") as file:
        return yaml.safe_load(file)
