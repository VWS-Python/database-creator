import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Safari()
log_in_url = 'https://developer.vuforia.com/vui/auth/login'
licenses_url = 'https://developer.vuforia.com/vui/develop/licenses'
email_address = os.environ['EMAIL_ADDRESS']
password = os.environ['PASSWORD']
driver.get(log_in_url)
email_address_input_element = driver.find_element_by_id('login_email')
email_address_input_element.send_keys(email_address)

password_input_element = driver.find_element_by_id('login_password')
password_input_element.send_keys(password)
password_input_element.send_keys(Keys.RETURN)

get_development_key_button_element = driver.find_element_by_id('get-development-key')

import pdb; pdb.set_trace()
driver.close()
