
# 访问该URL，服务器会返回setcookie的头信息
http HEAD http://httpbin.org/cookies/set/userid/123456
# 再次访问，Cookie并没有被上传
http  http://httpbin.org/cookies
# 手动在request header里面设置Cookie
http  http://httpbin.org/cookies "Cookie:userid=123456"


# 以下是Python代码
# 创建一个requests.Session对象
s = requests.Session()
# 使用session对象访问url，会接收服务器返回的cookie并保存
r = s.get('http://httpbin.org/cookies/set/userid/123456')
# 再次使用session对象访问该网站其他URL，自动上传了刚才保存的cookie
s.get('http://httpbin.org/cookies').json()