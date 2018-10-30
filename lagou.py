import requests

url = "https://www.lagou.com/jobs/positionAjax.json"

querystring = {"px":"default","city":"北京","needAddtionalResult":"false"}

# payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"first\"\r\n\r\nfalse\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"pn\"\r\n\r\n16\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"kd\"\r\n\r\nPython\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
payload = {
"first": "false",
"pn":"16",
"kd":"Python"
}
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'Accept': "application/json, text/javascript, */*; q=0.01",
    'Accept-Encoding': "gzip, deflate, br",
    'Accept-Language': "zh-CN,zh;q=0.9,en;q=0.8",
    'Connection': "keep-alive",
    'Content-Length': "26",
    'Content-Type': "application/x-www-form-urlencoded",
    'DNT': "1",
    'Host': "www.lagou.com",
    'Origin': "https://www.lagou.com",
    'Referer': "https://www.lagou.com/jobs/list_Python?px=default&city=%E5%8C%97%E4%BA%AC",
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
    'X-Anit-Forge-Code': "0",
    'X-Anit-Forge-Token': "None",
    'X-Requested-With': "XMLHttpRequest",
    'Cache-Control': "no-cache",
    # 'Postman-Token': "a6f90cb9-eef9-7563-4391-f2230970323e"
    }

response = requests.post(url, data=payload, headers=headers, params=querystring)

print(response.text)