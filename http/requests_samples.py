# coding:utf-8

import requests
from faker import Faker


faker = Faker()
website = 'http://httpbin.org'

print('GET请求')
r = requests.get(website)
print(r.status_code)

print('\nPOST请求')
r = requests.post('%s/post' % website, data={'key':'value'})
print(r.json())

print("\nGET参数")
payload = {'a': '1', 'b': '2', 'c': None, 'd': [4, 5, 6]}
r = requests.get('%s/get' % website, params=payload)
print(r.url)

print("\n定制Headers")
headers = {'user-agent': faker.user_agent()}
r = requests.get('%s/headers' % website, headers=headers)
print(r.json())

print("\n使用Cookies")
url = '%s/cookies' % website
cookies = dict(userid='123', token='xxxxxxxxxxxxxxx')
r = requests.get(url, cookies=cookies)
print(r.json())


print('\nBasic认证')
r = requests.get('%s//basic-auth/user/passwd' % website, auth=('user', 'passwd'))
print(r.json())

print('\nSession会话保持')
s = requests.Session()
s.get('%s/cookies/set/userid/123456789' % website)
r = s.get("%s/cookies" % website)
print(r.json())

print('\n抛出状态码异常')
bad_r = requests.get('%s/status/404' % website)
print(bad_r.status_code)
bad_r.raise_for_status()