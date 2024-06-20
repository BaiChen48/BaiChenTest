
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
    time = Buy().taobao_time()
    year, month, day, hour, minute, second, milliseconds = 2024, 6, 20, 15, 30, 0, 0
    dt = datetime.datetime(year, month, day, hour, minute, second, milliseconds * 1000)
    # 获取当前时间的 datetime 对象
    now = datetime.datetime.now()
    print(now)
    # 将 datetime 对象转换为时间戳（秒）
    timestamp_seconds = now.timestamp()

    # 将时间戳转换为毫秒
    timestamp_milliseconds = int(timestamp_seconds * 1000)

    print("当前时间的 13 位毫秒时间戳：", timestamp_milliseconds)

    tt = dt.timestamp()
    # print(tt)
    print("淘宝 时间 13 位毫秒时间戳：",time)
