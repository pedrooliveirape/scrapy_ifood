import requests
import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from bs4 import BeautifulSoup
import pandas as pd

class AcessaIfood:

    def __init__(self, cep, number_anddress, category='restaurantes'):
        options = Options()
        options.add_argument('window-size=1240,980')
        #options.add_argument('--headless')
        service = Service(ChromeDriverManager(driver_version="114.0.5735.16").install())
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(f'https://www.ifood.com.br/{category}')

        self.cep = cep
        self.number_address = number_anddress
        self.address = self.get_address()
        self.input_address()

        input('Aperte ENTER para continuar...')
        self.driver.close()

    def input_address(self):
        #address = 'rua São Francisco de Assis, 110 - Cruz de Rebouças, Igarassu-PE'
        print('chamei a função input_address')
        cont = 0
        while True:
            sleep(1)
            try:
                if self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div/div/div[1]/div/div/div[2]/div[1]/button[2]'): 
                    print('encontrado')
                    self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div/div/div[1]/div/div/div[2]/div[1]/button[2]').send_keys(self.address)
                    break 
            except:
                cont += 1
                print(f'passando no except. cont={cont}')
                if cont > 60:
                    print('falha ao buscar input endereço.')
                    break
        # Botão do endereço
        #/html/body/div[5]/div/div/div/div/div/div[2]/div/div[1]/div[3]/ul/li[1]/div/button 
        cont = 0
        while True:
            sleep(1)
            try:
                if self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div/div/div[2]/div/div[1]/div[3]/ul/li[1]/div/button '): 
                    print('encontrado')
                    self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div/div/div[2]/div/div[1]/div[3]/ul/li[1]/div/button ').click()
                    break 
            except:
                cont += 1
                print(f'passando no except de clicar. cont={cont}')
                if cont > 60:
                    print('falha ao clicar no endereço.')
                    break
        # Botão confirmar localização
        #/html/body/div[5]/div/div/div/div/div/div[3]/div[2]/button
        cont = 0
        while True:
            sleep(1)
            try:
                if self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div/div/div[3]/div[2]/button'): 
                    print('botão "Confirmar localização" encontrado!')
                    self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div/div/div[3]/div[2]/button').click()
                    break 
            except:
                cont += 1
                print(f'passando no except de clicar confirmar localização. cont={cont}')
                if cont > 60:
                    print('falha ao clicar no botão confirmar localização.')
                    break
        # Digitar '.' no Ponto de referência
        #/html/body/div[5]/div/div/div/div/div/div[3]/div[1]/div[2]/form/div[2]/div/label/input
        cont = 0
        while True:
            sleep(1)
            try:
                if self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div/div/div[3]/div[1]/div[2]/form/div[2]/div/label/input'): 
                    print('encontrado')
                    self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div/div/div[3]/div[1]/div[2]/form/div[2]/div/label/input').send_keys('.')
                    break 
            except:
                cont += 1
                print(f'passando no except Ponto de referência. cont={cont}')
                if cont > 60:
                    print('falha ao buscar input Ponto de referência.')
                    break
        # Botão salvar endereço
        #/html/body/div[5]/div/div/div/div/div/div[3]/div[1]/div[2]/form/div[4]/button
        cont = 0
        while True:
            sleep(1)
            try:
                if self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div/div/div[3]/div[1]/div[2]/form/div[4]/button'): 
                    print('botão "Salvar endereço" encontrado!')
                    self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div/div/div[3]/div[1]/div[2]/form/div[4]/button').click()
                    break 
            except:
                cont += 1
                print(f'passando no except de clicar Salvar endereço. cont={cont}')
                if cont > 60:
                    print('falha ao clicar no botão Salvar endereço.')
                    break

    def get_address(self):
        info_endereco = requests.get(f'https://brasilapi.com.br/api/cep/v1/{self.cep}').json()
        endereco = (f'rua {info_endereco["street"]}, {self.number_address} - {info_endereco["neighborhood"]}, {info_endereco["city"]} - {info_endereco["state"]}, Brasil')
        return endereco
