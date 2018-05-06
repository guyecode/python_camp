from urllib.parse import urlparse
url = 'https://guye:123@list.jd.com:443/list.html;abc=1?cat=9987,653,655&page=1#J_main'
o = urlparse(url)
attrs = ['fragment', 'hostname', 'netloc', 'params', 'password', 'path', 'port', 'query', 'scheme', 'username']
for attr in attrs:
    print('%s: %s' % (attr, getattr(o, attr)))