import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import pytest
from selenium.webdriver.common.keys import Keys


@pytest.fixture()
def driver():
    option = Options()
    option.add_argument("--window-size=3072,1536")
    option.add_argument("--force-device-scale-factor=0.99")
    option.add_experimental_option("detach", value=True)
    driver_chrome = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=option
    )
    yield driver_chrome


def test_customizable_desk(driver):
    driver.get("http://testshop.qa-practice.com/")
    desk_link = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Customizable Desk"))
    )
    current_window = driver.current_window_handle
    ActionChains(driver).key_down(Keys.CONTROL).click(desk_link).key_up(
        Keys.CONTROL
    ).perform()
    all_tabs = driver.window_handles

    for tab in all_tabs:
        if tab != current_window:
            break
    driver.switch_to.window(tab)

    add_to_cart = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "add_to_cart"))
    )
    add_to_cart.click()

    cont_shopping = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(
            (By.XPATH, '//button[@class="btn btn-secondary"]')
        )
    )

    cont_shopping.click()
    time.sleep(3)
    driver.close()
    driver.switch_to.window(current_window)

    open_basket = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((
            By.CSS_SELECTOR, ".p-1.text-center.text-reset"))
    )
    open_basket.click()

    total_price = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, '//td[@class="text-end border-0 px-0 pt-3"]')
        )
    )
    print(total_price.text)

    assert total_price.text != "0"


def test_bags_compare(driver):
    driver.get("https://magento.softwaretestingboard.com/gear/bags.html ")

    first_bag = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "product-item"))
    )

    action = ActionChains(driver)
    action.move_to_element(first_bag).perform()
    time.sleep(1)

    add_compare = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.action.tocompare"))
    )

    add_compare.click()

    compare_products = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//span[@class="counter qty"]'))
    )

    assert "1 item" in compare_products.text
