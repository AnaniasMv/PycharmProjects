from selenium import webdriver
from time import sleep as slp
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://web.whatsapp.com/")

slp(15)

while True:
    search = driver.find_element(By.XPATH, f"//span[@title='Gordo']")
    search.click()
    slp(0.3)
    edit = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
    slp(0.5)
    edit.click()
    edit.send_keys("oi")
    enviar = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span')
    enviar.click()