import re
import os
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup

r = requests.get('http://www.xiachufang.com/')
bc = BeautifulSoup(r.text)
imgs = bc.select('img')
images = []
for img in imgs:
    if img.has_attr('data-src'):
        images.append(img.attrs['data-src'])
    else:
        images.append(img.attrs['src'])


print(images)


image_dir = os.path.join(os.curdir, 'xiachufang')
if not os.path.isdir(image_dir):
    os.mkdir(image_dir)

for image in images:
    o = urlparse(image)
    filepath = os.path.join(image_dir, o.path[1:])
    print(filepath)
    img_res = requests.get(image)
    with open(filepath, 'wb') as f:
        for chunk in img_res.iter_content(1024):
            f.write(chunk)