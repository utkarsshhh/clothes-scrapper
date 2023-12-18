from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

driver = webdriver.Chrome('/Users/utkarshpadia/Downloads/chromedriver-mac-arm64/chromedriver')

driver.get('https://store.unionlosangeles.com/collections/clothing?page=3')

last_height = 0

while (True):
    page_height = driver.execute_script("document.body.scrollHeight")
    if (page_height==last_height):
        break
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(6)
    last_height = page_height

