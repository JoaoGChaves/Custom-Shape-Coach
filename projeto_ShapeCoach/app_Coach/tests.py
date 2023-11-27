from django.test import TestCase 
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import Select 
import random 
import string 
import time 
import os 
import tempfile 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 

chrome_options = webdriver.ChromeOptions() 
chrome_options.add_argument("--no-sandbox") 
chrome_options.add_argument("--disable-gpu") 
browser = webdriver.Chrome(options=chrome_options) 
wait = WebDriverWait(browser, 10) 
username = ''.join(random.choices(string.ascii_lowercase, k=8)) 
password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))

class TesteFDS (TestCase):
    def teste_a_objetivo (self):
        browser.get('http://127.0.0.1:8000/objetivo/')
        time.sleep(3)
        browser.find_element(By.ID, 'ganho_de_massa').click()
        time.sleep(3)
        browser.find_element(By.ID, 'academia').click()
        time.sleep(3)
        browser.find_element(By.ID, 'receitas').click()
        time.sleep(3)
        browser.find_element(By.ID, 'voltar').click()
        time.sleep(3)
        browser.find_element(By.ID, 'treinar').click()
        time.sleep(3)
        browser.find_element(By.ID, 'peito').click()
        time.sleep(3)
        browser.find_element(By.ID, 'voltar').click()
        time.sleep(3)
        browser.find_element(By.ID, 'costas').click()
        time.sleep(3)
        browser.find_element(By.ID, 'voltar').click()
        time.sleep(3)
        browser.find_element(By.ID, 'perna').click()
        time.sleep(3)
        browser.find_element(By.ID, 'voltar').click()
        time.sleep(3)

class TesteFDS (TestCase):
    def teste_b_objetivo (self):
        browser.get('http://127.0.0.1:8000/objetivo/')
        time.sleep(3)
        browser.find_element(By.ID, 'perda').click()
        time.sleep(3)
        browser.find_element(By.ID, 'academia').click()
        time.sleep(3)
        browser.find_element(By.ID, 'receitas').click()
        time.sleep(3)
        browser.find_element(By.ID, 'voltar').click()
        time.sleep(3)
        browser.find_element(By.ID, 'treinar').click()
        time.sleep(3)
        browser.find_element(By.ID, 'peito').click()
        time.sleep(3)
        browser.find_element(By.ID, 'voltar').click()
        time.sleep(3)
        browser.find_element(By.ID, 'costas').click()
        time.sleep(3)
        browser.find_element(By.ID, 'voltar').click()
        time.sleep(3)
        browser.find_element(By.ID, 'perna').click()
        time.sleep(3)
        browser.find_element(By.ID, 'voltar').click()
        time.sleep(3)


    def teste_c_objetivo (self):
        browser.get('http://127.0.0.1:8000/objetivo/')
        time.sleep(3)
        browser.find_element(By.ID, 'manutenção').click()
        time.sleep(3)
        browser.find_element(By.ID, 'academia').click()
        time.sleep(3)
        browser.find_element(By.ID, 'receitas').click()
        time.sleep(3)
        browser.find_element(By.ID, 'voltar').click()
        time.sleep(3)
        browser.find_element(By.ID, 'treinar').click()
        time.sleep(3)
        browser.find_element(By.ID, 'peito').click()
        time.sleep(3)
        browser.find_element(By.ID, 'voltar').click()
        time.sleep(3)
        browser.find_element(By.ID, 'costas').click()
        time.sleep(3)
        browser.find_element(By.ID, 'voltar').click()
        time.sleep(3)
        browser.find_element(By.ID, 'perna').click()
        time.sleep(3)
        browser.find_element(By.ID, 'voltar').click()
        time.sleep(3)


    def teste_d_objetivo (self):
        browser.get('http://127.0.0.1:8000/objetivo/')
        time.sleep(3)
        browser.find_element(By.ID, 'aumento').click()
        time.sleep(3)
        browser.find_element(By.ID, 'academia').click()
        time.sleep(3)
        browser.find_element(By.ID, 'receitas').click()
        time.sleep(3)
        browser.find_element(By.ID, 'voltar').click()
        time.sleep(3)
        browser.find_element(By.ID, 'treinar').click()
        time.sleep(3)
        browser.find_element(By.ID, 'peito').click()
        time.sleep(3)
        browser.find_element(By.ID, 'voltar').click()
        time.sleep(3)
        browser.find_element(By.ID, 'costas').click()
        time.sleep(3)
        browser.find_element(By.ID, 'voltar').click()
        time.sleep(3)
        browser.find_element(By.ID, 'perna').click()
        time.sleep(3)
        browser.find_element(By.ID, 'voltar').click()
        time.sleep(3)


    def teste_e_objetivo (self):
        browser.get('http://127.0.0.1:8000/home/')
        time.sleep(3)
        browser.find_element(By.ID, 'dicas').click()
        time.sleep(3)
    