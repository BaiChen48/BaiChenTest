import time
i
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

def invisibility_of_element_located(driver,timeout=30,frequency=0.5,xpath_location=''):
    try:
        element = WebDriverWait(driver,timeout,poll_frequency=frequency).until(ec.visibility_of_element_located(By.XPATH,xpath_location))
    except:
        print('元素没找到')
driver = webdriver.Chrome()
driver.get('http://172.22.2.72:30004/')

print(driver.title)
print(driver.current_url)
print(driver.name)

driver.find_element()
driver.close()
