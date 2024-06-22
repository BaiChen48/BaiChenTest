import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging
from SHOP.BuyTime import BuyTime

# 设置日志记录
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# 配置日志记录，同时输出到文件和控制台
logging.basicConfig(
    level=logging.INFO,
    filename='buy_script.log',  # 日志文件名
    filemode='a',  # 追加模式
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'

)

logger = logging.getLogger('BuyScriptLogger')
class Buy:
    def __init__(self, login_url):
        self.driver = webdriver.Chrome()
        self.driver.get(login_url)
        self.driver.maximize_window()
        self.login_url = login_url

    def login(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.element_to_be_clickable((By.LINK_TEXT, '亲，请登录'))).click()
            logging.info("点击登录按钮")
            time.sleep(30)  # 等待用户登录，实际使用中应使用显式等待
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="J_SiteNavMytaobao"]/div[1]/a/span')))
            logging.info("登录成功")
        except TimeoutException:
            logging.error("登录超时或失败")

    def start_buy(self):
        # 抢购逻辑...
        pass

    def local_time_diff(self, seckill_time_str):
        seckill_time = datetime.datetime.strptime(seckill_time_str, "%Y-%m-%d %H:%M:%S")
        seckill_time_stamp = int(seckill_time.timestamp()) * 1000
        logging.info(f"抢购时间戳:{seckill_time_stamp}")
        taobao_time_stamp = BuyTime().taobao_time_stamp()
        logging.info(f"淘宝时间戳:{taobao_time_stamp}")
        count_down = seckill_time_stamp - taobao_time_stamp
        logging.info(f"倒计时: {count_down} ")
        if count_down > 100:
            self.refresh_page()
        else:
            self.start_buy()

    def refresh_page(self):
        self.driver.get(self.login_url)
        logging.info("页面刷新完成")



if __name__ == '__main__':
    buy = Buy("https://www.taobao.com")
    buy.login()
    buy.local_time_diff("2024-06-23 00:30:00")
    buy.driver.quit()