from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

driver = webdriver.Chrome('/Users/utkarshpadia/Downloads/chromedriver-mac-arm64/chromedriver')

driver.get('https://store.unionlosangeles.com/collections/footwear')

last_height = 0



while (True):
    time.sleep(4)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(4)
    load_button = driver.find_element_by_xpath('//*[@id="fs-serp-page"]/div/div[2]/div[3]')
    if (load_button):
        load_button.click()
    else:
        break







