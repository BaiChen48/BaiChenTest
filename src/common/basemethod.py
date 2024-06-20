import logging
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver


def presence_of_element_located(driver, ele_located):
    element = WebDriverWait(driver, timeout=30, poll_frequency=1).until(EC.visibility_of_element_located(ele_located))
    return element


if __name__ == '__main__':
    print('start')
    driver = webdriver.Chrome()
    driver.get('https://www.taobao.com/')
    driver.maximize_window()
    # 请 请登录 按钮
    login_ele = (By.LINK_TEXT, '亲，请登录')
    presence_of_element_located(driver, login_ele).click()

    time.sleep(5)
    driver.quit()
