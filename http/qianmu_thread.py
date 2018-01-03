# coding:utf-8
import time
import threading
from queue import Queue
import requests
import lxml.etree
from w3lib.html import remove_tags

START_URL = 'http://qianmu.iguye.com/2018USNEWS世界大学排名'
link_queue = Queue()    # 队列，保存等抓取的url
DOWNLOADER_NUM = 100   # 启动的线程数量
threads = []    # 线程列表，保存Thread对象
download_pages = 0


def fetch(url, raise_err=True):
    global download_pages
    try:
        # 使用requests抓取url
        r = requests.get(url)
        r.encoding = 'utf-8'
        download_pages += 1
        return r.text
    except Exception as e:
        # 如果报错则print出来
        print(e)
    else:
        # 如果没报错，则检查http的返回码是否正常
        if raise_err:
            r.raise_for_status()


def filter(html):
    """过滤网页源码中的特殊符号和sup标签"""
    return remove_tags(html, which_ones=('sup',)).replace('\n', '')\
    .replace('\r', '').replace('\t', '')


def clean(s):
    """去除字符串两边的空格"""
    return s.strip() if s else ''


def parse(html):
    """解析入口页面信息"""
    # 使用全局变量
    global link_queue
    dom = lxml.etree.HTML(html)
    # 获取除第一行以外的所有行
    rows = dom.xpath("//div[@id='content']//tr[position()>1]")
    for row in rows:
        # 提取每行的文本，并用clean函数进行处理
        columns = map(clean, row.xpath('./td//text()'))
        for column in columns:
            print(column, end=',')
        print()
        #提取每行第二个单元格中的超链接
        link = row.xpath('./td[2]//@href')        
        if link:
            link = link[0]
            if not link.startswith('http://'):
                link = 'http://qianmu.iguye.com/%s' % link
            # 将url放入队列
            link_queue.put(link)


def parse_univercity(html):
    """解析大学详情页面的信息"""
    dom = lxml.etree.HTML(filter(html))

    # 先获取一个父节点，以减少重复代码
    wiki_content = dom.xpath('//div[@id="wikiContent"]')[0]
    # 获取大学名称
    title = wiki_content.xpath('./h1[@class="wikiTitle"]/text()')[0]
    # 获取左边的列
    keys = wiki_content.xpath('./div[@class="infobox"]/table//tr/td[1]/p/text()')
    # 获取右边的每一个单元格
    cols = dom.xpath('//*[@id="wikiContent"]/div[@class="infobox"]/table//tr/td[2]')
    # 因为有的单元格中存在多行，所以用逗号连接起来
    values = [','.join(col.xpath('.//text()')) for col in cols]
    # 用title作为key，存储成字典
    info = {title: dict(zip(keys, values))}
    print(info)



def downloader():
    while True:
        # 阻塞直到从队列获得了一条消息
        link = link_queue.get()
        # 如果收到的消息是None，则退出循环
        if link is None:
            break
        # 执行下载、解析操作
        parse_univercity(fetch(link, raise_err=False))
        # 向队列发送完成任务的消息
        link_queue.task_done()
        print('remaining queue: %s' % link_queue.qsize())

if __name__ == '__main__':
    start_time = time.time()
    # 抓取解析入口页面
    parse(fetch(START_URL))
    # 启动线程
    for i in range(DOWNLOADER_NUM):
        t = threading.Thread(target=downloader)
        t.start()
        threads.append(t)
    # 阻塞到队列清空为止
    link_queue.join()

    # 向队列发送DOWNLOADER_NUM个None，以通知线程退出
    for i in range(DOWNLOADER_NUM):
        link_queue.put(None)
    # 退出线程
    for t in threads:
        t.join()
    # 计算抓取的耗时
    cost_seconds = time.time() - start_time
    print('download %s pages in %.2f seconds' % (download_pages, cost_seconds))
