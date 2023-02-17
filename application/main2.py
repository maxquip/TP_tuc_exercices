from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

driver.get("https://www.reddit.com/")

driver.implicitly_wait(5)

print(driver.title)
  

driver.close()