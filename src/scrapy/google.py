from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

from src.scrapy.util import wait_element

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://www.google.com/')
input = driver.find_element_by_xpath('//input[@title="Pesquisar"]')
input.send_keys("minha string de busca")
input.send_keys(Keys.ENTER)

# WAIT para esperar carregar os resultados na sua página
wait_element(driver, by=By.XPATH, by_content='//div[@class="g"]')
lista = driver.find_elements_by_xpath('//div[@class="g"]')
for l in lista:
    print(l)
    l.find_element_by_xpath("./")

print(driver)