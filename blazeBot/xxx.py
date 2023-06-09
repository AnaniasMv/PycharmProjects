from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chrome_options = Options()
chrome_options.add_argument("-headless")
nav = webdriver.Chrome(options = chrome_options)
BASE_URL = 'https://blaze.com/pt/games/double'
nav.get(BASE_URL)


while True:
    pegarDados = nav.find_element(By.XPATH, '//*[@id="roulette-recent"]').text

    tfg = pegarDados.split()

    def qualnum(x):
        if x == '1':
            return 1

        if x == '2':
            return 2

        if x == '3':
            return 3

        if x == '4':
            return 4

        if x == '5':
            return 5

        if x == '6':
            return 6

        if x == '7':
            return 7

        if x == '8':
            return 8

        if x == '9':
            return 9

        if x == '10':
            return 10

        if x == '11':
            return 11

        if x == '12':
            return 12

        if x == '13':
            return 13

        if x == '14':
            return 14


    def qualcor(x):
        if x == '1':
            return 'V'

        if x == '2':
            return 'V'

        if x == '3':
            return 'V'

        if x == '4':
            return 'V'

        if x == '5':
            return 'V'

        if x == '6':
            return 'V'

        if x == '7':
            return 'V'

        if x == '8':
            return 'P'

        if x == '9':
            return 'P'

        if x == '10':
            return 'P'

        if x == '11':
            return 'P'

        if x == '12':
            return 'P'

        if x == '13':
            return 'P'

        if x == '14':
            return 'P'


    pd = tfg[0:16]

    mapeando = map(qualnum, pd)
    mapeando2 = map(qualcor, pd)

    finalnum = list(mapeando)
    finalcor = list(mapeando2)

    print(finalnum)
    print(finalcor)


    def verificarSaida(num):
        if num == ['P', 'P', 'V', 'V', 'P', 'P', 'P', 'P', 'V', 'V', 'P', 'P', 'V', 'V', 'P', 'V']:
            return '''
               ✅ Estrategia x entrar no 🔴
               Apoiar no Branco 🔴
               '''
        if num == ['V', 'V', 'P', 'V', 'V', 'P', 'P', 'V', 'V', 'P', 'V', 'V', 'P', 'P', 'V', 'V']:
            return '''
               ✅ Estrategia x entrar no 🔴
               Apoiar no Branco 🔴
               '''

        if num == ['P', 'V', 'V', 'P', 'P', 'V', 'V', 'P', 'V', 'V', 'P', 'P', 'P', 'V', 'P', 'P']:
            return '''
                      ✅ Estrategia x entrar no 🔴
                      Apoiar no Branco 🔴
                      '''

        def convert_cor(q):
            if q == 'V':
                return '🔴'

            if q == 'P':
                return '🔴'


    time.sleep(30)




