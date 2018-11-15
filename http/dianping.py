import os
import re
import requests
from pprint import pprint
from urllib.request import urlretrieve
from lxml import etree
import lxml.html
import tinycss
from tinycss.token_data import ContainerToken, TokenList


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}
url = 'http://www.dianping.com/shop/507576'
r = requests.get(url, headers=headers)
print(r.text)
index = r.text.find('flora_3659')
print(r.text[index: index + 1500])

dom_selector = etree.HTML(r.text)
# 获取CSS文件的url
css_url = dom_selector.xpath('//link[contains(@href, "svgtextcss")]/@href')[0]
print(css_url)
# 请求CSS文件
css_resp = requests.get('http:' + css_url)
# 解析CSS文件(先去了解一下tinycss的基本用法)
parser = tinycss.make_parser('page3')
ss = parser.parse_stylesheet(css_resp.text)
css_dict = {}
for rule in ss.rules:
    # 先取出所有的选择器，也就是 .em-0Pk0 或者 span[class^="ov-"] 这样的
    # 我们去掉前面的.以及span，class,以及各种符号，以类名作为键值

    css_selector = rule.selector[-1]
    if isinstance(css_selector, ContainerToken):
        css_class = css_selector.content[-1].value[:-1]
    else:
        css_class = css_selector.value
    css_dict[css_class] = {}
    for d in rule.declarations:
        lst = []
        for v in d.value:
            if v.value == ' ':
                continue
            lst.append(v.value)
        css_dict[css_class][d.name] = lst
# 最终生成的css字典类似于这样：
# {'em': {'background-image': [
#     '//s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/853af8f7da7dd415cc0e47eb771e5a94.svg'],
#         'background-repeat': ['no-repeat'],
#         'display': ['inline-block'],
#         'height': [30],
#         'margin-top': [-12],
#         'vertical-align': ['middle'],
#         'width': [12]},
#  'em-03Of': {'background': [-324.0, -126.0]},
#  'em-03Qy': {'background': [-72.0, -696.0]},
#  'em-03cn': {'background': [-60.0, -6.0]},
# }
# pprint(css_dict)

# 遍历所有的css属性
for k, data in css_dict.items():
    if 'background-image' not in data:
        continue

    # 根据svg的url，决定保存互本地后的文件路径
    svg_url = data['background-image'][0]
    svg_filename = os.path.basename(svg_url)
    svg_path = os.path.join('./svg/', svg_filename)
    # 下载svg文件
    urlretrieve('http:' + svg_url, svg_path)
    data['svg_path'] = svg_path
    # 解析svg文件
    svg = etree.parse(svg_path)
    # 读取其中所有文字内容，注意svg的格式不只一种，目前发现的有3种
    text_list = svg.findall(".//{http://www.w3.org/2000/svg}textPath") or svg.findall(".//{http://www.w3.org/2000/svg}text")
    # 组成一个二维数组
    data['char_list'] = [t.text for t in text_list]

# 再定义一个字典，保存css样式名称对应具体的字符
char_map = {}
# 再次遍历css属性字典
for k, data in css_dict.items():
    # 只处理名称中带符号“-”的，也就是具体的span样式
    if '-' not in k:
        continue
    # 按“-”分割，前面的是大类的名字，后面的是具体的类名
    category, name = k.split('-')
    # 看当前的类具体是哪一个大类的CSS属性
    css_property = css_dict[category]
    # 先取出字符的调度和宽度
    width = int(css_property['width'][0])
    height = int(css_property['height'][0])
    left, top = data['background']
    # 根据高度、宽度以及偏移量，计算出坐标
    x, y = -int(left / width), -int(top / height)
    char_list = css_dict[category]['char_list']
    # 取出
    char_map[k] = char_list[y][x]

# pprint(char_map)
# 所有的评论原始信息
plist = dom_selector.xpath('//ul[@id="reviewlist-wrapper"]/li//p[@class="desc J-desc"]')
for p in plist:
    # 把节点对象转换成html源码
    source = lxml.html.tostring(p, encoding='unicode')
    # pprint(source)
    # 去掉源码里最外面的p标签
    source = source[23:-5]
    # 替换掉内部的span标签
    text = re.sub(r'<span class=\"([a-zA-Z0-9\-]+)\"></span>', r'{\1}', source)
    # pprint(text)
    pprint(text.format(**char_map).replace('\xa0', ' ').replace('<br/>', '\n').replace('<br>', '\n'))



