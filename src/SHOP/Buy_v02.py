import datetime
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.basemethod import presence_of_element_located
from SHOP.BuyTime import BuyTime


class Buy():
    def __init__(self, login_url: str = "https://www.taobao.com"):

        if login_url:
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
        else:
            print("Please input the login url.")
            raise Exception("Please input the login url.")
        while True:
            self.driver.get(login_url)
            try:
                if presence_of_element_located(self.driver,(By.LINK_TEXT,'亲，请登录')):
                    print("没登录，开始点击登录按钮...")
                    presence_of_element_located(self.driver,(By.LINK_TEXT,'亲，请登录')).click()
                    print("请在30s内扫码登陆!!")
                    time.sleep(30)
                    if presence_of_element_located(self.driver, (By.XPATH,'//*[@id="J_SiteNavMytaobao"]/div[1]/a/span')):
                        print("登陆成功")
                        break
                    else:
                        print("登陆失败, 刷新重试, 请尽快登陆!!!")
                        continue
            except Exception as e:
                print(str(e))
                continue

    def local_time_diff(self):
        while True:
            # 假设有一个日期时间字符串
            seckill_time_str = "2024-06-23 00:15:00.000000"
            seckill_time = datetime.datetime.strptime(seckill_time_str, "%Y-%m-%d %H:%M:%S.%f")
            print(seckill_time)
            print('设置抢购时间:', seckill_time)
            taobao_time = BuyTime().taobao_time_format()
            count_down = (seckill_time - taobao_time).seconds
            print('倒计时:', count_down/60)
            if count_down > 180000:
                self.driver.get("https://cart.taobao.com/cart.htm")
                print("每分钟刷新一次界面，防止登录超时...")
                time.sleep(60)
            else:
                print("抢购时间点将近，停止自动刷新，准备进入抢购阶段...")
                self.start_buy()
                break

    def start_buy(self):
        self.driver.get("https://cart.taobao.com/cart.htm")
        time.sleep(0.1)
        select_all_locat = (By.ID, 'J_SelectAll1')
        if presence_of_element_located(self.driver, select_all_locat):
            presence_of_element_located(self.driver, select_all_locat).click()
            print('已经选中购物车全部商品！')
        click_submit_times = 0
        max_retry_count = 30
        submit_succ = False
        while True:
            if True:
                try:
                    settlement_element_locat = (By.ID, 'J_Go')
                    time.sleep(0.01)
                    if presence_of_element_located(self.driver, settlement_element_locat):
                        presence_of_element_located(self.driver, settlement_element_locat).click()
                        print('已经点击结算按钮了')
                        while True:
                            try:
                                if click_submit_times < 20:
                                    submit_order_button = (By.CSS_SELECTOR, '[title="提交订单"]')
                                    if presence_of_element_located(self.driver, submit_order_button):
                                        presence_of_element_located(self.driver, submit_order_button).click()
                                        print("已经点击提交订单按钮")
                                    submit_succ = True
                                    break
                                else:
                                    print("提交订单失败...")
                            except Exception as e:
                                print("没发现提交按钮, 页面未加载, 重试...")
                                click_submit_times += 1
                                time.sleep(0.01)
                except Exception as e:
                    print(e)
                if submit_succ:
                    print("订单已经提交成功，无需继续抢购...")
                    break
                if click_submit_times > max_retry_count:
                    print("重试抢购次数达到上限，放弃重试...")
                    break
            time.sleep(0.1)


if __name__ == '__main__':
    buy = Buy()
    buy.local_time_diff()
    buy.driver.quit()
