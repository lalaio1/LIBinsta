from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome() 
driver.get("https://www.instagram.com/")  

username = driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "password")
username.send_keys("vzz.max")
password.send_keys("1recuperando")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

time.sleep(5) 

perfil_alvo = 'veradp047'
driver.get(f"https://www.instagram.com/{perfil_alvo}")

driver.find_element(By.CSS_SELECTOR, "svg[aria-label='Opções']").click()
time.sleep(1)

driver.find_element(By.XPATH, "//button[text()='Denunciar']").click()
time.sleep(1)

driver.find_element(By.XPATH, "//div[text()='Denunciar conta']").click()
time.sleep(1)

driver.find_element(By.XPATH, "//div[text()='Está fingindo ser outra pessoa']").click()
time.sleep(1)

driver.find_element(By.XPATH, "//button[text()='Denunciar']").click()

driver.quit()
