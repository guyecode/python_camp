import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# 创建浏览器对象
driver = webdriver.Chrome()
# driver = webdriver.PhantomJS()
# 设置窗口大小
driver.set_window_size(1280,2400)
# 发起请求，相当于我们在地址栏里输入一个URL并回车
driver.get('http://item.jd.com/782353.html')
print driver.title
print driver.page_source
# 购买数量填写10个
e = driver.find_element_by_id('buy-num')
e.send_keys('10')
# 刷新页面
driver.refresh()
# 滚动到页面底部
driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
# 滚动到页面顶部
driver.execute_script('window.scrollTo(0, 0)')
driver.execute_script('alert(123)')
driver.close()


# 搜索百度并提取搜索结果
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
e = driver.find_element_by_id('kw')
e.send_keys('python')

e.send_keys(Keys.RETURN)
left = driver.find_element_by_id('content_left')
links = left.find_elements_by_xpath('//div[@class="result c-container "]/h3/a')
for link in links:
    print link.text
    print link.get_property('href')
# kw = driver.find_element_by_id('kw')
e.clear()
e.send_keys('today')
e.submit()
driver.close()


#登录知乎
driver = webdriver.Chrome()
driver.get('https://www.zhihu.com')
driver.find_element_by_link_text(u'登录').click()
driver.find_element_by_xpath('//span[@class="signin-switch-password"]').click()
driver.find_element_by_xpath('//input[@name="account"]').send_keys('xxxx@gmail.com')
driver.find_element_by_xpath('//input[@name="password"]').send_keys('xxxxxxxxx')
