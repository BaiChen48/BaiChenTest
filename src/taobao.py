from time import sleep
def _login(self, login_url: str="https://www.taobao.com"):
    if login_url:
        self.driver = self.start_driver()
    else:
        print("Please input the login url.")
        raise Exception("Please input the login url.")
    while True:
        self.driver.get(login_url)
        try:
            if self.driver.find_element_by_link_text("亲，请登录"):
                print("没登录，开始点击登录按钮...")
                self.driver.find_element_by_link_text("亲，请登录").click()
                print("请在30s内扫码登陆!!")
                sleep(30)
                if self.driver.find_element_by_xpath('//*[@id="J_SiteNavMytaobao"]/div[1]/a/span'):
                    print("登陆成功")
                    break
                else:
                    print("登陆失败, 刷新重试, 请尽快登陆!!!")
                    continue
        except Exception as e:
            print(str(e))
            continue
while True:
    current_time = datetime.now()
    if (self.seckill_time_obj - current_time).seconds > 180:
        self.driver.get("https://cart.taobao.com/cart.htm")
        print("每分钟刷新一次界面，防止登录超时...")
        sleep(60)
    else:
        print("抢购时间点将近，停止自动刷新，准备进入抢购阶段...")
        break
self.driver.get("https://cart.taobao.com/cart.htm")
        sleep(1)
        if self.driver.find_element_by_id("J_SelectAll1"):
            self.driver.find_element_by_id("J_SelectAll1").click()
            print("已经选中全部商品！！！")
# 获取淘宝时间
def taobao_time(self):
    url = 'http://api.m.taobao.com/rest/api3.do?api=mtop.common.getTimestamp'
    ret = requests.get(url).text
    js = json.loads(ret)
    return int(js['data']['t'])


def local_jd_time_diff(self):
    return self.local_time() - self.taobao_time()
while True:
    if self.local_time() - diff_time >= self.buy_time_ms:
        try:
            if self.driver.find_element_by_id("J_Go"):
                self.driver.find_element_by_id("J_Go").click()
                click_submit_times = 0
                while True:
                    try:
                        if click_submit_times < 20:
                            self.driver.find_element_by_link_text('提交订单').click()
                            print("已经点击提交订单按钮")
                            submit_succ = True
                            break
                        else:
                            print("提交订单失败...")
                    except Exception as e:
                        print("没发现提交按钮, 页面未加载, 重试...")
                        click_submit_times = click_submit_times + 1
                        sleep(0.01)
        except Exception as e:
            print(e)
        if submit_succ:
            print("订单已经提交成功，无需继续抢购...")
            break
        if retry_count > max_retry_count:
            print("重试抢购次数达到上限，放弃重试...")
            break
        retry_count += 1
    sleep(0.1)
def pay(self):
    try:
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'sixDigitPassword')))
        element.send_keys(self.password)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'J_authSubmit'))).click()
        print("付款成功")
    except:
        print('付款失败')
    finally:
        sleep(60)
        self.driver.quit()
