import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.basemethod import presence_of_element_located


class Buy():
    def __init__(self, login_url: str = "https://www.taobao.com"):
        try:
            print('实例driver,登录淘宝')
            self.driver = webdriver.Chrome()
            self.driver.get(login_url)
            self.driver.maximize_window()
        except:
            print('打开淘宝网站失败!')

    def login(self):

        try:
            print('开始登录')
            login_element_locat = (By.LINK_TEXT, '亲，请登录')
            presence_of_element_located(self.driver, login_element_locat).click()
            time.sleep(10)

            print('点击购物车')
            shopping_car_locat = (By.CSS_SELECTOR, '[href="//cart.taobao.com"]')
            presence_of_element_located(self.driver, shopping_car_locat).click()
            print('勾选全选按钮')
            handles = self.driver.window_handles
            # print('driver.title:', self.driver.title)
            self.driver.switch_to.window(handles[1])
            # print('driver.title:', self.driver.title)
            select_all_locat = (By.ID, 'J_SelectAll1')
            presence_of_element_located(self.driver, select_all_locat).click()
            print('点击结算按钮')
            settlement_element_locat = (By.ID, 'J_Go')
            time.sleep(0.5)
            presence_of_element_located(self.driver, settlement_element_locat).click()
            print('点击提交订单按钮')
            # 提交订单按钮
            submit_order_button = (By.CSS_SELECTOR, '[title="提交订单"]')
            presence_of_element_located(self.driver, submit_order_button).click()
        except:
            print('失败')




if __name__ == '__main__':
    buy = Buy()
    buy.login()
    buy.driver.quit()
