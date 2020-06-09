import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

driver = webdriver.Safari()
ten_second_wait = WebDriverWait(driver, 10)
log_in_url = 'https://developer.vuforia.com/vui/auth/login'
licenses_url = 'https://developer.vuforia.com/vui/develop/licenses'
new_free_licenses_url = 'https://developer.vuforia.com/vui/develop/licenses/free/new'
email_address = os.environ['EMAIL_ADDRESS']
password = os.environ['PASSWORD']
driver.get(log_in_url)
email_address_input_element = driver.find_element_by_id('login_email')
email_address_input_element.send_keys(email_address)

password_input_element = driver.find_element_by_id('login_password')
password_input_element.send_keys(password)
password_input_element.send_keys(Keys.RETURN)

get_development_key_button_element = ten_second_wait.until(
    expected_conditions.presence_of_element_located(
        (By.ID, 'get-development-key'),
    ),
)

get_development_key_button_element.click()

license_name_input_element = ten_second_wait.until(
    expected_conditions.presence_of_element_located(
        (By.ID, 'license-name'),
    ),
)

license_name = 'foo'
license_name_input_element.send_keys(license_name)
import pdb; pdb.set_trace()
driver.close()
