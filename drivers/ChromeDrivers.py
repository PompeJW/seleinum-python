from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class ChromeDriver:
    @staticmethod
    def get_driver():
        options = Options()
        #options.add_argument('--headless')
        service = Service(ChromeDriverManager().install())
        return webdriver.Chrome(service=service, options=options)
