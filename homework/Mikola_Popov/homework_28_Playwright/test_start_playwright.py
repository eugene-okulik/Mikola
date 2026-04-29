import time
from playwright.sync_api import Page


def test_by_role(page: Page):
    page.goto("https://the-internet.herokuapp.com/")
    time.sleep(1)
    # page.get_by_text('Form Authentication').click()
    # альтернативный поиск элемента
    page.get_by_role("link", name="Form Authentication").click()
    time.sleep(1)
    username = page.get_by_role("textbox", name="username")
    username.fill("Nikolay")
    time.sleep(1)
    password = page.get_by_role("textbox", name="password")
    password.fill("80292788064np")
    time.sleep(1)
    # page.locator('button[type="submit"]').click()
    # альтернативный поиск элемента
    page.get_by_role("button").click()
    time.sleep(1)


def test_search_element_by_text(page: Page):
    page.goto(" https://the-internet.herokuapp.com/")
    page.get_by_text("Form Authentication").click()
    username = page.get_by_label("username")
    username.fill("Nikolay")
    password = page.get_by_label("password")
    password.fill("80292788064np")
    page.get_by_role("button", name="Login").click()
