from selenium import webdriver
from selenium.webdriver.common.keys import Keys

navegador = webdriver.Chrome()
navegador.get("https://www.google.com/")

# Passo 1: pegar a cotação do dolar
navegador.find_element(
    'xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("dolar hoje")
navegador.find_element(
    'xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
dolar = navegador.find_element(
    'xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value")
print(f"o valor do dolar é R$ {dolar}")
# Passo 2: pegar cotação do euro
navegador.get("https://www.google.com/")
navegador.find_element(
    'xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("euro hoje")
navegador.find_element(
    'xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
euro = navegador.find_element(
    'xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value")
print(f"o valor do euro é R$ {euro}")

# Passo 3: pegar cotação do ouro
navegador.get('https://www.melhorcambio.com/ouro-hoje')
ouro = (navegador.find_element(
    'xpath', '//*[@id="comercial"]').get_attribute("value")).replace(",", ".")
print(f"o valor do ouro é R$ {ouro} por grama")


navegador.quit()
