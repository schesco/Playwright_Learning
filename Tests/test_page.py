#variante test_practice_form1
from Pages.HomePage import HomePage

def test_form(page):
    home = HomePage(page)

    home.navigate()
    home.fill_basic_info("Francis Pascal uggggogoguog", "hello@gmail.com", "123456")
    home.select_checkbox()
    home.select_dropdown(1)
    home.fill_birthday("1983-04-03")
    home.submit()
    print("test")
    page.screenshot(path="screenshots/homepage.png")
    assert "Success" in home.get_alert_text()