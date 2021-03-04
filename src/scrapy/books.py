### Instalar o pacote webdriver manager
## pip install webdriver-manager
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import re
# driver = webdriver.Chrome(ChromeDriverManager().install())
from util import wait_element

def get_conteudo(drv, urls):
    results = []
    for u in urls:
        drv.get(u)
        titulo = drv.find_element_by_xpath('//article//h1').text ## AAA
        plist = drv.find_elements_by_xpath("//div[contains(@class,'product_main')]/p")
        preco = float(plist[0].text[1:])
        estoque = int(re.findall('\d+', plist[1].text)[0])
        descricao = drv.find_element_by_xpath('//article/p').text
        results.append({'titulo': titulo, 'preco': preco, 'estoque': estoque, 'descricao': descricao})
    return results


options = webdriver.FirefoxOptions()
options.headless = True
driver_conteudo = webdriver.Firefox(options=options)
driver = webdriver.Firefox(options=options)
url = 'http://books.toscrape.com'
driver.get(url)
wait_element(driver, "//li[@class='next']/a", by=By.XPATH)
botao = driver.find_element_by_xpath("//li[@class='next']/a")
count = 0
resultados = []
encontrou = True
to_exit = False
while encontrou:
    ## coletar os dados dessa página ###

    tags_links = driver.find_elements_by_xpath('//article/h3/a')
    urls = [t.get_attribute('href') for t in tags_links]
    current_page = get_conteudo(driver_conteudo, urls)
    # resultados = resultados + current_page
    resultados.extend(current_page)

    ## Fim da coleta
    botao.click()
    encontrou = wait_element(driver, "//li[@class='next']/a", by=By.XPATH)
    try:
        botao = driver.find_element_by_xpath("//li[@class='next']/a")
        count = 0
    except NoSuchElementException:
        pass
        print("Nao tem mais o botao next")
        break
    if not encontrou:
        count = count + 1
        if count > 3:
            break
        else:
            continue

current_page = get_conteudo(driver_conteudo, urls)
resultados.extend(current_page)
print(resultados)








print(resultados)

# urls = [f'http://books.toscrape.com/catalogue/page-{x}.html' for x in range(1, 51)]
