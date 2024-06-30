from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Methods

def add_string_text(element):
    element.send_keys("テスト")
    pass


def add_telephone_text(element):
    element.send_keys('010-0101-0101')
    pass


def add_email_text(element):
    element.send_keys('test@test.com')


def make_radio_selection(element):
    element.click()


def click_checkbox(element):
    element.click()


def handle_inputs(all_input_elements):
    for input_element in all_input_elements:
        validation_type = input_element.get_attribute('validation-type')
        if validation_type in validation_type_input_data:
            validation_type_input_data[validation_type](input_element)


def handle_selects(all_select_elements):
    for select in all_select_elements:
        option_to_check = select.find_elements(By.TAG_NAME, 'option')
        option_to_check[1].click()


def handle_text_areas(all_textarea_elements):
    for textarea in all_textarea_elements:
        textarea.send_keys("テスト テスト テスト テスト")


# Validation Check Map
validation_type_input_data = {
    'string': add_string_text,
    'telephone': add_telephone_text,
    'email': add_email_text,
    'radio': make_radio_selection,
    'checkbox': click_checkbox,
    'confirm': click_checkbox,
}

# Web Driver Setup
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
selected_url = input("Please enter the URL for testing: \r\n")
driver.get(selected_url)

# Gather all Inputs
all_inputs = driver.find_elements(By.TAG_NAME, 'input')
all_select_inputs = driver.find_elements(By.TAG_NAME, 'select')
all_text_areas = driver.find_elements(By.TAG_NAME, 'textarea')

handle_inputs(all_inputs)

handle_selects(all_select_inputs)

handle_text_areas(all_text_areas)
