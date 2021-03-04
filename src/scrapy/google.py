from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get('https://www.google.com.br')

input = driver.find_element_by_xpath("//input[@name='q']")
input.send_keys("teste")
input.send_keys(Keys.ENTER)
print(driver)

