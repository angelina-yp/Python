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
browser.find_elements()





# 7.2. Найдите элемент с текстом "Fully charged cat". Чем больше разных XPATH и/или CSS-селекторов сможете подобрать, тем лучше
# http://suninjuly.github.io/cats.html