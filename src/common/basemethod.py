from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

def presence_of_element_located(ele_located):
    element = WebDriverWait.until(EC.visibility_of_element_located(ele_located))
    return element