# coding:utf-8
import sys
import time
import threading
import signal
import redis
import requests
import lxml.etree
from w3lib.html import remove_tags

# START_URL = 'http://qianmu.iguye.com/2018USNEWS世界大学排名'
DOWNLOADER_NUM = 10   # 启动的线程数量
DOWNLOAD_DELAY = 0.1  # 下载间隔，单位秒，可以为小数
threads = []    # 线程列表，保存Thread对象
download_pages = 0
r = redis.Redis()
thread_on = True

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
    finally:
        print('<%s> %s' % (r.status_code, url))


def filter(html):
    """过滤网页源码中的特殊符号和sup标签"""
    return remove_tags(html, which_ones=('sup',)).replace('\n', '')\
    .replace('\r', '').replace('\t', '')


def clean(s):
    """去除字符串两边的空格"""
    return s.strip() if s else ''


def parse(html):
    """解析入口页面信息"""
    dom = lxml.etree.HTML(html)
    # 获取除第一行以外的所有行
    rows = dom.xpath("//div[@id='content']//tr[position()>1]")
    for row in rows:
        # 提取每行的文本，并用clean函数进行处理
        columns = map(clean, row.xpath('./td//text()'))
        # for column in columns:
        #     print(column, end=',')
        # print()
        #提取每行第二个单元格中的超链接
        link = row.xpath('./td[2]//@href')
        if link:
            link = link[0]
            if not link.startswith('http://'):
                link = 'http://qianmu.iguye.com/%s' % link
            # 将url放入队列
            if r.sadd('qianmu.seen', link):
                r.rpush('qianmu.queue', link)


def parse_univercity(html):
    """解析大学详情页面的信息"""
    if not html:
        return
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
    r.lpush('qianmu.items', info)


def downloader(i):
    while thread_on:
        # 阻塞直到从队列获得了一条消息
        link = r.lpop('qianmu.queue')
        # 执行下载、解析操作
        if link:
            parse_univercity(fetch(link.decode('utf-8'), raise_err=False))
            print('Thread-%s remaining queue: %s' % (i, r.llen('qianmu.queue')))
        time.sleep(DOWNLOAD_DELAY)
    print('Thread-%s exit now.' % i)


def sigint_handler(signum, frame):
    print('received CTRL+C, wait for exit gracefully')
    global thread_on
    thread_on = False
    # 向队列发送DOWNLOADER_NUM个None，以通知线程退出
    # r.lpush('qianmu.queue', *['exit'] * DOWNLOADER_NUM)
    

if __name__ == '__main__':
    if len(sys.argv) > 1:
        start_url = sys.argv[1]
        # 抓取解析入口页
        parse(fetch(start_url))
    start_time = time.time()
    # 启动线程
    for i in range(DOWNLOADER_NUM):
        t = threading.Thread(target=downloader, args=(i+1,))
        t.start()
        threads.append(t)
        print('Thread(%s) started....' % t.name)

    signal.signal(signal.SIGINT, sigint_handler)

    # 退出线程
    for t in threads:
        t.join()

    # 计算抓取的耗时
    cost_seconds = time.time() - start_time
    print('download %s pages in %.2f seconds' % (download_pages, cost_seconds))
