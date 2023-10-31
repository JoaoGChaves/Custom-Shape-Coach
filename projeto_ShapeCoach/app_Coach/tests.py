from django.test import TestCase
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

def test_treino():
    navegador.find_element('xpath', '//*[@id="criar_conta"]/a'.click())
    

test_treino()