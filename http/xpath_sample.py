import requests
from lxml import etree


headers = {
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'Accept-Encoding': "gzip, deflate, br",
    'Accept-Language': "zh-CN,zh;q=0.9,en;q=0.8",
    'Cache-Control': "no-cache",
    'Connection': "keep-alive",
    'DNT': "1",
    'Host': "movie.douban.com",
    'Upgrade-Insecure-Requests': "1",
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    # 'Postman-Token': "0d84d830-19c5-117f-cdbf-936da9ffe395"
    }

r = requests.get('https://movie.douban.com/', headers=headers)

s = selector = etree.HTML(r.text)

# 取出页面中所有的链接
links = s.xpath('//@href')
print(type(links), len(links))

# 抓取电影评论页
r = requests.get('https://movie.douban.com/subject/26611804/comments',
        headers=headers)
s = etree.HTML(r.text)


# 获取每个评论节点
comments = s.xpath('//div[@class="comment"]')
for comment in comments:
    # 获取当前评论的用户名称
    username = comment.xpath('./h3/span[2]/a/text()')[0]
    # 获取当前评论的内容
    content = comment.xpath('./p/text()')[0]
    # 获取打分星级
    stars = comment.xpath('./h3/span[2]/span[2]/@class')[0]
    # 评论发表时间
    comment_time = comment.xpath('./h3/span[2]/span[3]/@title')
    comment_time = comment_time[0] if comment_time else ''
    print('%s %s %s: \n%s' % (username, stars, comment_time, content))