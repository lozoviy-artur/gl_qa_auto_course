from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class BasePage:
    PATH = r"/Users/arturlozovyi/Desktop/gl_qa_auto_course/"
    DRIVER_NANE = "chromedriver"

    def __init__(self) -> None:
        self.driver = webdriver.Chrome(
            service=Service(BasePage.PATH + BasePage.DRIVER_NANE)
        )

    def close(self):
        self.driver.close()

