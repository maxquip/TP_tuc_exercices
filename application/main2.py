from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

driver = webdriver.Chrome()
driver.get("https://wikiroulette.co/")
wiki="https://wikiroulette.co/"

def titre(url):
  driver.get(url)
  driver.set_window_size(1900,1200)
  titre = driver.title
  print("le titre du site est :"+titre)

def titrearticle(url):
  driver.get(url)
  article= driver.find_elements(by=By.CSS_SELECTOR, value="mw-page-title-main")
  print("le titre de l'article est :"+article)

time.sleep(5)
driver.close()

titre(wiki)
titrearticle(wiki)
