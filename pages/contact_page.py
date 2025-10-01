from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ContactPage(BasePage):
    NAME = (By.ID, "name")
    EMAIL = (By.ID, "email")
    MESSAGE = (By.ID, "message")
    SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")

    ERROR_NAME = (By.ID, "error-name")
    ERROR_EMAIL = (By.ID, "error-email")
    SUCCESS = (By.ID, "success")

    def fill_form(self, name="", email="", message=""):
        if name is not None:
            self.type(self.NAME, name)
        if email is not None:
            self.type(self.EMAIL, email)
        if message is not None:
            self.type(self.MESSAGE, message)

    def submit(self):
        self.click(self.SUBMIT)

    def get_success_text(self):
        return self.find(self.SUCCESS).text

    def get_name_error(self):
        return self.find(self.ERROR_NAME).text

    def get_email_error(self):
        return self.find(self.ERROR_EMAIL).text
