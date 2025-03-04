import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options

@pytest.fixture(scope="function", autouse=True)
def driver(request):
    options = Options()
    options.page_load_strategy = "normal"
    options.add_argument("--disable-cache")
    options.add_argument("--incognito")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    service = Service(executable_path='geckodriver.exe')
    driver = webdriver.Firefox(service=service)
    request.cls.driver = driver
    yield driver
    driver.quit()
