import time
from locators import loc_state, loc_city

from playwright.sync_api import Page, expect

data = "Kosmonavtov Street, Building 44, Apartment 85"


def test_filling_form(page: Page):
    page.goto("https://demoqa.com/automation-practice-form")
    first_name = page.get_by_placeholder("First Name")
    first_name.press_sequentially("Nikolay", delay=100)
    last_name = page.get_by_placeholder("Last Name")
    last_name.press_sequentially("Popov", delay=100)
    email = page.get_by_placeholder("name@example.com")
    email.press_sequentially("test_name@gmail.com", delay=100)
    page.get_by_text("Male", exact=True).click()
    mobile_number = page.get_by_placeholder("Mobile Number")
    mobile_number.press_sequentially("8029278807", delay=100)
    date_of_birth = page.locator('//input[@id="dateOfBirthInput"]')
    date_of_birth.press("Control+a")
    date_of_birth.press_sequentially("15 May 2026", delay=100)
    subjects = page.locator('//input[@class="subjects-auto-complete__input"]')
    subjects.press_sequentially("Subjects", delay=100)
    page.get_by_label("Sports").click()
    page.set_input_files(
        '//input[@label="Select picture"]',
        "C:\\Users\\Nikolai\\Desktop\\zhivotnye_kot_13379.jpg",
    )
    current_address = page.get_by_placeholder("Current Address")
    current_address.press_sequentially(data, delay=100)
    page.locator(loc_state).click()
    page.locator("//div[@id='react-select-3-option-1']").click()
    page.locator(loc_city).click()
    page.locator("//div[@id='react-select-4-option-2']").click()
    page.get_by_role("button", name="Submit").click()
    time.sleep(2)
    text_new_page = page.locator("//div[@id='example-modal-sizes-title-lg']")
    expect(text_new_page).to_contain_text("Thanks for submitting the form")
