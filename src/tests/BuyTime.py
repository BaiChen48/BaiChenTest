import datetime
from selenium import webdriver
import requests, json


class BuyTime():

    # def __init__(self, login_url: str = "https://www.taobao.com"):
    #     self.driver = webdriver.Chrome()
    #     self.driver.get(login_url)
    #     self.driver.maximize_window()

    # 淘宝时间戳
    def taobao_time_stamp(self):
        url = 'http://api.m.taobao.com/rest/api3.do?api=mtop.common.getTimestamp'
        ret = requests.get(url).text
        js = json.loads(ret)
        print('淘宝时间13位时间戳:', int(js['data']['t']))
        return int(js['data']['t'])  # 以时间戳形式范围
        # timestamp = int(js['data']['t']) / 1000
        # return datetime.datetime.fromtimestamp(timestamp)

    # 淘宝时间格式化
    def taobao_time_format(self):
        url = 'http://api.m.taobao.com/rest/api3.do?api=mtop.common.getTimestamp'
        ret = requests.get(url).text
        js = json.loads(ret)
        taobao_time_stamp = int(js['data']['t'])
        taobao_time_format = datetime.datetime.fromtimestamp(taobao_time_stamp / 1000)
        #  2024-06-22 15:17:11.947000 将时间格式化返回
        print('淘宝时间:', taobao_time_format)
        return taobao_time_format

    # 现在时间 格式化
    def now_time_format(self):
        # 2024-06-22 15:37:38.885921
        print('现在时间:', datetime.datetime.now())
        return datetime.datetime.now()

    # 现在时间13位时间戳
    def mow_time_stamp(self):
        now = datetime.datetime.now()
        now_stamp = int(now.timestamp() * 1000)
        print('现在时间13位时间戳:', now_stamp)
        return int(now_stamp)

    # 指定时间
    def designated_time_stamp(self):
        year, month, day, hour, minute, second, = 2024, 6, 20, 15, 30, 0,
        buy_dt = datetime.datetime(year, month, day, hour, minute, second)
        buy_time = int(buy_dt.timestamp()) * 1000
        print('指定时间的13位时间戳:', buy_time)
        return buy_time

    # 指定时间的 格式化
    def designated_time_format(self):
        year, month, day, hour, minute, second, millisecond = 2024, 6, 20, 15, 30, 0, 0
        # 将毫秒转换为微秒（1毫秒 = 1000微秒）
        microsecond = int(millisecond * 1000)
        buy_dt = datetime.datetime(year, month, day, hour, minute, second, microsecond)
        designated_time_format = buy_dt.strftime('%Y-%m-%d %H:%M:%S.%f')
        print('指定时间:', designated_time_format)
        return designated_time_format


if __name__ == '__main__':
    buy = BuyTime()
    buy.taobao_time_format()
    buy.taobao_time_stamp()

    buy.now_time_format()
    buy.mow_time_stamp()

    buy.designated_time_format()
    buy.designated_time_stamp()
