# coding:utf-8

"""
爬取大学排名列表并print出来，另建立一个尽可能齐全的大学资料库，也print出来
"""
import string
import lxml.etree
import requests
from w3lib.html import remove_tags


domain = 'qianmu.iguye.com'
start_url = 'http://qianmu.iguye.com/2018USNEWS世界大学排名'
link_queue = [] # 保存等待抓取的url


def fetch(url):
    """使用request抓取页面"""
    r = requests.get(url)
    r.encoding = 'utf-8'
    r.raise_for_status()
    return r.text


def clean(s):
    """去除字符串两边的空格"""
    return s.strip() if s else ''


def filter(html):
    """过滤网页源码中的特殊符号和sup标签"""
    return remove_tags(html, which_ones=('sup',)).replace('\n', '')\
    .replace('\r', '').replace('\t', '')


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
            # 放入待抓取列表
            link_queue += link


def parse_university(html):
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


if __name__ == '__main__':
    # 处理入口页面，并提取数据
    parse(fetch(start_url))
    # 反转List以便先进先出
    link_queue.reverse()
    while link_queue:
        link =link_queue.pop()
        if not link.startswith('http://'):
            link = 'http://%s/%s' % (domain, link)
        parse_university(fetch(link))

