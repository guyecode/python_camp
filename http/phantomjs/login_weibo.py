# coding:utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


"""登录微博"""

if __name__ == '__main__':
    # driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true'])
    driver = webdriver.Chrome()
    driver.delete_all_cookies()
    driver.set_window_size(1280,2400)
    # driver.implicitly_wait(30)   # 隐性等待，最长等30秒
    driver.get('https://weibo.com')
    time.sleep(5)
    loginname = driver.find_element_by_id('loginname')
    with open('/tmp/weibopwd') as f:
        email, pwd = f.read().split(' ')
    # loginname.send_keys(email)
    for i in email:
        loginname.send_keys(i)
        time.sleep(0.1)
    loginname.send_keys(Keys.TAB)
    time.sleep(1)
    password = driver.find_element_by_xpath('//input[@name="password"]')
    # password.send_keys(pwd)
    for i in pwd:
        password.send_keys(i)
        time.sleep(0.1)
    time.sleep(1)
    # password.send_keys(Keys.RETURN)
    driver.find_element_by_xpath('//a[@action-type="btn_submit"]').click()
    cookies = driver.get_cookies()
    username = driver.find_element_by_xpath('//a[@bpfilter="page_frame"]').text
    print username
    # 拿到登录cookies，可以从任意地方登录了
    request_cookies = {c['name']:c['value'] for c in cookies}
    requests.get('https://weibo.com').text.find(username)
    requests.get('https://weibo.com', cookies=request_cookies).text.find(username)

    # 下翻到页面底部
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    # 获取页面里的feeds
    feeds = driver.find_elements_by_xpath('//div[@node-type="feed_list_content"]')
    for feed in feeds:
        print feed.text

    driver.close()
    driver.quit()