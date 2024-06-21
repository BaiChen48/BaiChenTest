import datetime
from selenium import webdriver
import requests, json


class Buy():

    def __init__(self, login_url: str = "https://www.taobao.com"):
        self.driver = webdriver.Chrome()
        self.driver.get(login_url)
        self.driver.maximize_window()

    def taobao_time(self):
        url = 'http://api.m.taobao.com/rest/api3.do?api=mtop.common.getTimestamp'
        ret = requests.get(url).text
        js = json.loads(ret)
        return int(js['data']['t'])  # 以时间戳形式范围
        # timestamp = int(js['data']['t']) / 1000
        # return datetime.datetime.fromtimestamp(timestamp)


if __name__ == '__main__':
    # 淘宝时间
    time = Buy().taobao_time()
    print("淘宝时间13位时间戳：", time)
    # 指定时间
    year, month, day, hour, minute, second, = 2024, 6, 20, 15, 30, 0,
    buy_dt = datetime.datetime(year, month, day, hour, minute, second)
    buy_time = int(buy_dt.timestamp())*1000
    print("特定时间13位时间戳：", buy_time)
    # 系统时间
    now = datetime.datetime.now()
    timestamp_milliseconds = int(now.timestamp() * 1000)
    print("当前时间13位时间戳：", timestamp_milliseconds)


    # dt_object = datetime.datetime.fromtimestamp(time / 1000)
    # formatted_time = dt_object.strftime('%Y-%m-%d %H:%M:%S')
    # # 格式化 datetime 对象为字符串，并包含毫秒
    # formatted_time_with_milliseconds = dt_object.strftime('%Y-%m-%d %H:%M:%S.%f')#[:-3]
    #
    # print("格式化的日期和时间（包含毫秒）：", formatted_time_with_milliseconds)
    # print("淘宝格式化的日期和时间：", formatted_time)
