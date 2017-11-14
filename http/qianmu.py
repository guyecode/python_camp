# coding:utf-8

"""
爬取大学排名列表并保存为JSON文件，另建立一个尽可能齐全的大学资料库，用JSON文件保存
"""
import string
import lxml.etree
import requests


domain = '140.143.192.76:8002'
start_url = 'http://140.143.192.76:8002/2018USNEWS世界大学排名'
link_queue = []


def fetch(url):
    r = requests.get(url)
    r.raise_for_status()
    return r.text


def clean(s):
    return s.strip() if s else ''

def x(ele):
    if not ele:
        return ''
    return ele[0].strip()

def parse(html):
    global link_queue
    dom = lxml.etree.HTML(html)
    rows = dom.xpath("//div[@id='content']//tr")
    for row in rows:
        columns = map(clean, row.xpath('./td//text()'))
        for column in columns:
            print(column, end=',')
        print()
        link = row.xpath('./td[2]//@href')
        if link:
            link_queue += link


def parse_university(html):
    dom = lxml.etree.HTML(html)
    wiki_content = dom.xpath('//div[@id="wikiContent"]')[0]
    title = wiki_content.xpath('./h1[@class="wikiTitle"]/text()')[0]
    keys = wiki_content.xpath('./div[@class="infobox"]/table//tr/td[1]/p/text()')
    values = wiki_content.xpath('./div[@class="infobox"]/table//tr/td[2]/p/text()')
    info = {title: dict(zip(keys, values))}
    print(info)


if __name__ == '__main__':
    content = fetch(start_url)
    parse(content)
    link_queue.reverse()
    while link_queue:
        link =link_queue.pop()
        if not link.startswith('http://'):
            link = 'http://%s/%s' % (domain, link)
        parse_university(fetch(link))

