# coding:utf-8

"""
爬取大学排名列表并保存为JSON文件，另建立一个尽可能齐全的大学资料库，用JSON文件保存
"""
import threading
from queue import Queue
import lxml.etree
import requests


start_url = 'http://140.143.192.76:8002/2018USNEWS世界大学排名'
q = Queue()
threads = []
downloader_num = 20


def fetch(url):
    r = requests.get(url)
    r.raise_for_status()
    return r.text


def clean(s):
    return s.strip() if s else ''


def downloader():
    while True:
        link = q.get()
        if link is None:
            break
        parse_university(fetch(link))
        q.task_done()


def parse_university(html):
    dom = lxml.etree.HTML(html)
    wiki_content = dom.xpath('//div[@id="wikiContent"]')[0]
    title = wiki_content.xpath('./h1[@class="wikiTitle"]/text()')[0]
    keys = wiki_content.xpath('./div[@class="infobox"]/table//tr/td[1]/p/text()')
    values = wiki_content.xpath('./div[@class="infobox"]/table//tr/td[2]/p/text()')
    info = {title: dict(zip(keys, values))}
    print(info)


if __name__ == '__main__':
    for i in range(downloader_num):
        t = threading.Thread(target=downloader)
        t.start()
        threads.append(t)
    print('%s threads are ready' % len(threads))
    dom = lxml.etree.HTML(fetch(start_url))
    rows = dom.xpath("//div[@id='content']//tr")
    for row in rows:
        columns = map(clean, row.xpath('./td//text()'))
        for column in columns:
            print(column, end=',')
        print()
        link = row.xpath('./td[2]//@href')
        if link:
            q.put(link[0])
    q.join()

    for i in range(downloader_num):
        q.put(None)
    for t in threads:
        t.join()