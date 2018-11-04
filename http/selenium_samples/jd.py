import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pyexcel


if __name__ == '__main__':
    keyword = 'iphone'
    if len(sys.argv) > 1:
        keyword = sys.argv[1]
    driver = webdriver.Chrome()
    driver.get('https://jd.com')
    k = driver.find_element_by_id('key')
    k.send_keys(keyword)
    k.send_keys(Keys.RETURN)

    # 隐式等待查找任何一个元素时，如果未能立即找到，则让WebDriver等待一定时间
    # driver.implicitly_wait(10)
    sort_btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((
            By.XPATH, '//div[@class="f-sort"]/a[2]')))
    # 按销量排序
    sort_btn.click()
    has_next = 1
    rows = []
    page_count = 3
    page = 1
    while has_next and page <= page_count:
        # 最差的写法
        # time.sleep(10)
        # 隐式等待查找任何一个元素时，如果未能立即找到，则让WebDriver等待一定时间
        # driver.implicitly_wait(10)
        # products = driver.find_elements_by_xpath('.//li[@class="gl-item"]')

        # 显示等待
        # 先定义等待条件，只有该条件触发，才执行后续代码
        # 最长等待10秒钟，直到xpath表达式中的元素至少有一个被找到
        # 如果查找的是一个元素，可以用presence_of_element_located
        products = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((
                By.XPATH, '//li[@class="gl-item"]')))

        # 整个商品区域的DIV
        goods_list = driver.find_element_by_id('J_goodsList')
        y = goods_list.rect['height'] + goods_list.rect['y']
        # y = next_page.rect['y']
        driver.execute_script('window.scrollTo(0, %s);' % y)
        # 将网页滚动至商品区域底部，以便触发加载更多商品的事件
        # for i in range(0, y + y // 10, y // 10):
        #     driver.execute_script('window.scrollTo(0, %s);' % i)
        #     time.sleep(0.2)
        time.sleep(5)
        products = driver.find_elements_by_xpath('.//li[@class="gl-item"]')
        for product in products:
            try:
                row = {}
                sku = product.get_attribute('data-sku')
                # print(product.get_attribute('innerHTML'))
                row['name'] = product.find_element_by_css_selector('div.p-name>a>em').text
                row['price'] = product.find_element_by_class_name('J_%s' % sku).text
                row['shop'] = product.find_element_by_xpath('.//div[@class="p-shop"]//a').text
                row['comments'] = product.find_element_by_id('J_comment_%s' % sku).text

                print(row)
                rows.append(row)
            except Exception as e:
                print(e)
                continue
            # writer.writerow(info)
        # 查找下一页按钮
        next_page = driver.find_element_by_xpath('//a[@class="pn-next"]')
        if not next_page.is_enabled():
            has_next = False
            print('end of all the pages')

        next_page.click()
        page += 1

    file_name = '%s.xls' % keyword
    pyexcel.save_as(records=rows, dest_file_name=file_name)
    sys.exit(driver.quit())