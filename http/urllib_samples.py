# coding=utf-8


import urllib.request
import urllib.parse

website = 'http://httpbin.org'

print('get请求')
with urllib.request.urlopen(website) as f:
    print(f.read(300))

print('post请求')
req = urllib.request.Request(url='%s/post' % website, 
  data=b'hello', method='POST')
with urllib.request.urlopen(req) as f:
    print(f.read(300))
    print(f.status)
    print(f.reason)

print('添加header信息')
req = urllib.request.Request(website)
req.add_header('Referer', 'http://www.python.org/')
r = urllib.request.urlopen(req)
print(r.status)

print('Baisc HTTP认证')
auth_handler = urllib.request.HTTPBasicAuthHandler()
auth_handler.add_password(realm='PDQ Application',
                          uri='/basic-auth/user/passwd',
                          user='user',
                          passwd='passwd')
opener = urllib.request.build_opener(auth_handler)
urllib.request.install_opener(opener)
urllib.request.urlopen(website)

print('GET 参数')
params = urllib.parse.urlencode(
  {'spam': 1, 'eggs': 2, 'bacon': 0})
url = '%s/?%s' % (website, params)
with urllib.request.urlopen(url) as f:
    print(f.readline())


print('POST 参数')
data = urllib.parse.urlencode({'name': '小明', 'age': 2})
data = data.encode()
with urllib.request.urlopen('%s/post' % website, data) as f:
    print(f.reason)
    print(f.read())

# print('使用代理')
# proxy_handler = urllib.request.ProxyHandler({'http': 'http://www.proxy.com:3128/'})
# proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
# proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
#
# opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
# opener.open(website + '/ip')


