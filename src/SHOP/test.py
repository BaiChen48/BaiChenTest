import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging
from SHOP.BuyTime import BuyTime

# 配置日志记录，同时输出到文件和控制台
logging.basicConfig(
    level=logging.INFO,
    filename='buy_script.log',  # 日志文件名
    filemode='a',  # 追加模式
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('BuyScriptLogger')

class Buy:
    def __init__(self, login_url):
        self.driver = webdriver.Chrome()
        self.driver.get(login_url)
        self.driver.maximize_window()
        self.login_url = login_url
        logger.info("初始化WebDriver并访问登录页面")

    def login(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.element_to_be_clickable((By.LINK_TEXT, '亲，请登录'))).click()
            logger.info("点击登录按钮")
            # 使用显式等待代替硬编码的sleep
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="J_SiteNavMytaobao"]/div[1]/a/span')))
            logger.info("登录成功")
        except TimeoutException:
            logger.error("登录超时或失败")

    # ... 其他方法 ...

    def local_time_diff(self, seckill_time_str):
        try:
            seckill_time = datetime.datetime.strptime(seckill_time_str, "%Y-%m-%d %H:%M:%S.%f")
            logger.info(f"抢购时间: {seckill_time}")
            taobao_time = BuyTime().taobao_time_format()
            logger.info(f"淘宝当前时间: {taobao_time}")
            count_down = (seckill_time - taobao_time).total_seconds() * 1000
            logger.info(f"倒计时毫秒数: {count_down}")

            if count_down > 100 * 1000:  # 100秒转换为毫秒
                self.refresh_page()
            else:
                self.start_buy()
        except ValueError as e:
            logger.error(f"时间字符串格式错误: {e}")

    def refresh_page(self):
        self.driver.get(self.login_url)
        logger.info("页面刷新完成")

    # ... 其他方法 ...

if __name__ == '__main__':
    # 修复硬编码的URL
    login_url = "https://www.taobao.com"  # 确保URL是正确的
    buy = Buy(login_url)
    buy.login()
    buy.local_time_diff("2024-06-23 00:30:00.000000")
    buy.driver.quit()
    logger.info("脚本执行完毕")