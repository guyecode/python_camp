import re
import os
from io import BytesIO
import pycurl
from urllib.parse import urlparse

# 发起一个GET请求并打印响应结果
buffer = BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, 'http://www.xiachufang.com/')
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()
body = buffer.getvalue()
text = body.decode('utf-8')
images = re.findall(r'src=\"(http://i2\.chuimg\.com/\w+\.jpg)', text)
image_dir = os.path.join(os.curdir, o.hostname)

for image in images:
    o = urlparse(image)
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)
    filepath = os.path.join(image_dir, o.path[1:])
    print(filepath)
    with open(filepath, 'wb') as f:
        c = pycurl.Curl()
        c.setopt(c.URL, image)
        c.setopt(c.WRITEDATA, f)
        print('downloading image: %s' % image)
        c.perform()
        c.close()


# 也可以用一句Linux命令来实现，Linux命令好强大
# curl -s http://www.xiachufang.com/|grep -oP '(?<=src=\")http://i2\.chuimg\.com/\w+\.jpg'|xargs -i curl {} -O