import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import pytest
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


@pytest.fixture()
def driver():
    option = Options()
    option.add_argument('--window-size=3072,1536')
    option.add_argument('--force-device-scale-factor=0.99')
    option.add_experimental_option('detach', value=True)
    chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
    yield chrome_driver


def test_go_to_page(driver):
    some_word = 'Sunny_day'
    driver.get("https://www.qa-practice.com/elements/input/simple")
    wait = WebDriverWait(driver, 5)
    input_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Submit me"]')))
    input_field.send_keys(some_word)
    input_field.send_keys(Keys.ENTER)
    result_text = wait.until(EC.presence_of_element_located((By.XPATH, '//p[@class="result-text"]')))
    assert some_word == result_text.text


def test_fill_out_form(driver):
    driver.get("https://demoqa.com/automation-practice-form")
    wait = WebDriverWait(driver, 5)
    first_name = driver.find_element(By.XPATH, '//input[@placeholder="First Name"]')
    first_name.send_keys('Nikolay')

    last_name = driver.find_element(By.XPATH, '//input[@placeholder="Last Name"]')
    last_name.send_keys('Popov')

    email = driver.find_element(By.XPATH, '//input[@id="userEmail"]')
    email.send_keys("Nikolay@gmail.com")

    gender_radio = wait.until(EC.element_to_be_clickable((By.XPATH, '//label[@class="custom-control-label"] ')))
    gender_radio.click()

    radio_male = driver.find_element(By.ID, "gender-radio-1")
    if radio_male.is_selected():
        print("Radio male selected")
    else:
        print("Radio male not selected")

    mobile_num = driver.find_element(By.XPATH, '//input[@placeholder="Mobile Number"]')
    mobile_num.send_keys("5294555555")

    date_of_birth = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="dateOfBirthInput"]')))
    date_of_birth.click()

    month_selection = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//select[@class="react-datepicker__month-select"]')
        )
    )
    month_selection.click()

    driver.find_element(By.XPATH, '//option[@value="7"]').click()

    year_selection = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//select[@class="react-datepicker__year-select"]')
    ))
    year_selection.click()
    driver.find_element(By.XPATH, '//option[@value="1986"]').click()

    day = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//div[@class="react-datepicker__day react-datepicker__day--006"]')
    ))
    day.click()

    subject = driver.find_element(By.XPATH, '//input[@id="subjectsInput"]')
    sub = ["E", "Co"]
    for i in range(len(sub)):
        subject.send_keys(sub[i])
        time.sleep(1)
        subject.send_keys(Keys.RETURN)

    hobbies = {
        "Sports": "//label[@for='hobbies-checkbox-1']",
        "Reading": "//label[@for='hobbies-checkbox-2']",
        "Music": "//label[@for='hobbies-checkbox-3']"
    }

    for hobby, selected in hobbies.items():
        check_box = wait.until(EC.element_to_be_clickable((By.XPATH, f'{selected}')))
        if not check_box.is_selected():
            driver.execute_script("arguments[0].click();", check_box)
        print(f"Checkbox - {hobby} - is selected")

    address = ['ул. Космонавтов', ' дом 145', ' кв. 999']

    current_address = driver.find_element(By.XPATH, '//textarea[@id="currentAddress"]')
    current_address.send_keys(*address)

    state = wait.until(EC.element_to_be_clickable((By.ID, 'state')))
    state.click()

    nrc_state = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="react-select-3-input"]')))
    nrc_state.send_keys("N")
    time.sleep(1)
    nrc_state.send_keys(Keys.RETURN)

    city = wait.until(EC.element_to_be_clickable((By.ID, 'city')))
    city.click()

    delhi_city = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="react-select-4-input"]')))
    delhi_city.send_keys("Delhi")
    time.sleep(1)
    delhi_city.send_keys(Keys.RETURN)

    button = driver.find_element(By.XPATH, '//button[@id="submit"]')
    button.click()

    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'modal-content')))

    title_modal = driver.find_element(By.XPATH, '//div[@id="example-modal-sizes-title-lg"]')
    print(title_modal.text)

    body_modal = driver.find_elements(By.XPATH, '//div[@class="modal-body"]//tr')
    data_form = {}

    for row in body_modal:
        column = row.find_elements(By.TAG_NAME, 'td')
        if len(column) == 2:
            key = column[0].text
            value = column[1].text
            data_form[key] = value
            print(f"{key} - {value}")


def test_choose_language(driver):
    driver.get("https://www.qa-practice.com/elements/select/single_select")
    wait = WebDriverWait(driver, 5)

    select = wait.until(EC.presence_of_element_located((By.XPATH, '//select[@id="id_choose_language"]')))
    select.click()

    language = wait.until(EC.element_to_be_clickable((By.XPATH, '//option[contains(text(), "Python")]')))
    language.click()

    drop_select = driver.find_element(By.XPATH, '//select[@id="id_choose_language"]')
    drop_select.click()

    button = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="submit-id-submit"]')))
    button.click()

    check_language = wait.until(EC.visibility_of_element_located((By.XPATH, '//p[@class="result-text"]')))

    assert check_language.text == "Python"


def test_dynamic_page(driver):
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    wait = WebDriverWait(driver, 10)

    button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button')))
    button.click()

    finish = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@id="finish"]/h4')))

    assert finish.text == "Hello World!"