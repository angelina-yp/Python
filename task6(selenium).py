import time
from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# def dd_open():
# browser.get('http://suninjuly.github.io/cats.html')
# time.sleep(5)
# 7.1. Найдите кпопку c текстом "Gold". Попробуйте подобрать как минимум 2 разных XPATH и/или CSS-селекторов
# http://suninjuly.github.io/xpath_examples
browser.get('http://suninjuly.github.io/xpath_examples')

a = browser.find_element(By.XPATH,"/html/body/div[2]/button[3]")
print(a.text)
a1 = browser.find_element(By.XPATH,"//*[contains(text(), 'Gold')]")
print(a1.text)
a3 = browser.find_element(By.CSS,"body > div:nth-child(2) > button:nth-child(3)")
print(a3.text)
# 7.2. Найдите элемент с текстом "Fully charged cat". Чем больше разных XPATH и/или CSS-селекторов сможете подобрать, тем лучше
# http://suninjuly.github.io/cats.html