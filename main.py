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
    time.sleep(10)
    # iframes = driver.find_elements_by_tag_name("iframe")
    # for index, iframe in enumerate(iframes):
    #     print(f"Iframe {index} outerHTML: {iframe.get_attribute('outerHTML')}")
    driver.switch_to.frame(5);
    # print (driver.page_source)

    # driver.switch_to_frame(driver.find_element_by_xpath('/html/body/div[18]/iframe'))
    time.sleep(5)
    ad = driver.find_element_by_xpath('//*[@id="ps-widget-custom-form__close-button"]/span')
    if (ad):
        ad.click()
    time.sleep(4)
    driver.switch_to.default_content()
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(3)
    try:
        load_button = driver.find_element_by_xpath('//*[@id="fs-serp-page"]/div/div[2]/div[3]')
        load_button.click()
    except Exception as e:
        print (e)
        break

html = driver.page_source
soup = BeautifulSoup(html,'lxml')

# print (soup)
# driver.quit()




