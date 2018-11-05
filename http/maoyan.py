import os
import re
import urllib
from pprint import pprint
import requests
import parsel
from fontTools.ttLib import TTFont


BASE_FONT_PATH = './base.woff'
# Base 字体的编码和数字的对应关系
BASE_FONT = {
    'x': '.',
    'uniEA64': '0',
    'uniF0A1': '1',
    'uniF662': '2',
    'uniF8B2': '3',
    'uniF69D': '4',
    'uniE450': '5',
    'uniF442': '6',
    'uniE2AE': '7',
    'uniE90F': '8',
    'uniE7B8': '9',
}
basefont = TTFont(BASE_FONT_PATH)
# 根据base字体文件生成 {字形编码: 真实数字}} 的对应关系
hex2num = {basefont['glyf'][i].coordinates.array.tobytes().hex():BASE_FONT[i] for i in basefont.getGlyphOrder()[2:]}
# pprint(hex2num)

# 初始化字体目录
font_dir = os.path.join(os.path.curdir, 'fonts')
if not os.path.isdir(font_dir):
	os.mkdir(font_dir)

# 构造请求头，并下载字体文件
headers = {
	    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
	    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
	    'Accept-Encoding': "gzip, deflate",
	    'Accept-Language': "zh-CN,zh;q=0.9,en;q=0.8",
	    'Cache-Control': "no-cache",
	    'Connection': "keep-alive",
	    'DNT': "1",
	    'Host': "maoyan.com",
	    'Upgrade-Insecure-Requests': "1",
	    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
    }
r = requests.get('http://maoyan.com/films/1229020', headers=headers)
selector = parsel.Selector(r.text)
# 解析出字体文件所在url
woff = selector.re_first("url\('(.+?\.woff)'\)")
# 下载字体文件
download_font_path = os.path.join(font_dir, os.path.basename(woff))
# 如果已存在该字体文件，则不用再下载了
if not os.path.isfile(download_font_path):
	urllib.request.urlretrieve('http:%s' % woff, download_font_path)

# 解析字体文件
font = TTFont(download_font_path)
# font.saveXML('font.xml')
# 根据新的字体文件生成{字形编码：字符编码}的对应关系
hex2u = {font['glyf'][i].coordinates.array.tobytes().hex():i for i in font.getGlyphOrder()[2:]}
# pprint(hex2u)
u2num = {}
for h, u in hex2u.items():
	# 生成新的字符编码对应真实数字的对应关系
	u2num[u] = hex2num[h]
# 小数点单独处理一下，uni2E是小数点字符的unicode值
u2num['uni2E'] = '.'
# pprint(u2num)
# 接下来可以正常解析网页中的数据了
box = selector.xpath('//div[contains(@class, "box")]')
box_num = box.xpath('./span[@class="stonefont"]/text()').get()
box_unit = box.xpath('./span[@class="unit"]/text()').get()
# 将页面中的乱码文字转化为带uni前缀的unicode编码字符串
t = lambda x: 'uni' + '%x'.upper() % ord(x)
# 逐个比对出真实数字
box_num = ''.join(u2num[t(b)] for b in box_num)

# 常规解析
movie = {}
movie['name'] = selector.xpath('//h3[@class="name"]/text()').get()
movie['票房'] = box_num + box_unit
pprint(movie)

