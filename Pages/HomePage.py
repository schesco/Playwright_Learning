
from playwright.sync_api import Page, expect

class HomePage:

    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        self.page.goto("https://rahulshettyacademy.com/angularpractice/")
        print("Launch Hallo")

    def fill_basic_info(self, name, email, password):
        self.page.fill('input[name="name"]', name)
        self.page.fill('input[name="email"]', email)
        self.page.fill('#exampleInputPassword1', password)

    def select_checkbox(self):
        self.page.check('#exampleCheck1')

    def select_dropdown(self, index):
        self.page.select_option('#exampleFormControlSelect1', index=int(index))

    def fill_birthday(self, date):
        self.page.fill('input[name="bday"]', date)

    def submit(self):
        self.page.click('input[value="Submit"]')

    def get_alert_text(self):
        alert = self.page.locator('.alert-success')
        expect(alert).to_be_visible()
        return alert.text_content()
