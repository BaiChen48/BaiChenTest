import time

from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
def presence_of_element_located(driver,ele_located):
    element = WebDriverWait(driver,timeout=30,poll_frequency=1).until(EC.visibility_of_element_located(ele_located))
    return element

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com')

    baidu_input_ele = presence_of_element_located(driver,(By.CSS_SELECTOR,'[name="wd"]'))
    baidu_input_ele.send_keys('显示等待')
    badiu_ele = presence_of_element_located(driver,(By.CSS_SELECTOR,'[value="百度一下"]'))
    badiu_ele.click()
    time.sleep(5)
