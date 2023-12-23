from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    time.sleep(10)
    ad = driver.find_element_by_xpath('//*[@id="ps-widget-custom-form__close-button"]/span')
    if (ad):
        ad.click()
    time.sleep(3)
    driver.switch_to.default_content()
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(10)
    # print (driver.page_source)
    # iframes = driver.find_elements_by_tag_name("iframe")
    # for index, iframe in enumerate(iframes):
    #     print(f"Iframe {index} outerHTML: {iframe.get_attribute('outerHTML')}")
    #     driver.switch_to.frame(index);

    # try:
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div[1]/div//div/div/div[2]/div[3]'))
        )
    print (element)
            # load_button = driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/div//div/div/div[2]/div[3]')
            # //*[@id="fs-serp-page"]/div/div[2]/div[3]
    element.click()
    driver.switch_to.default_content()

    # except Exception as e:
    #     print ("Exception ",e)
    #     break
    driver.switch_to.default_content()
        # if (index==len(iframes)-1):
        #     break

html = driver.page_source
soup = BeautifulSoup(html,'lxml')

# print (soup)
driver.quit()




