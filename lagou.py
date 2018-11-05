import time
import requests

url = "https://www.lagou.com/jobs/positionAjax.json"

querystring = {"px":"default","city":"北京","needAddtionalResult":"false"}

# payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"first\"\r\n\r\nfalse\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"pn\"\r\n\r\n16\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"kd\"\r\n\r\nPython\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
payload = {
"first": "false",
# "pn":"16",
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

cookies = {' Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1540917355',
 ' Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1539047366,1539675076,1540902737',
 ' JSESSIONID': 'ABAAABAAAFCAAEGF2076306A23D961ED009431AA35F1984',
 ' LGRID': '20181031003554-df3b0de0-dc61-11e8-846a-5254005c3644',
 ' SEARCH_ID': 'f94905a7fea24d66b96f76cb09b358ac',
 ' TG-TRACK-CODE': 'index_navigation',
 ' X_HTTP_TOKEN': 'ae0cef88015f67e55b5ac231e3172186',
 ' _ga': 'GA1.2.958992131.1495979526',
 ' _gid': 'GA1.2.915017862.1540902737',
 ' index_location_city': '%E6%9D%AD%E5%B7%9E',
 ' sajssdk_2015_cross_new_user': '1',
 ' sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%22166c5c6dd70cfb-05e0d717cf3e8b-1e396652-3686400-166c5c6dd71e95%22%2C%22%24device_id%22%3A%22166c5c6dd70cfb-05e0d717cf3e8b-1e396652-3686400-166c5c6dd71e95%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D',
 ' user_trace_token': '20180530211201-1de96db0-9e72-4b34-8eec-13552ab4cec6',
 'LGUID': '20170528215155-cf9f14b5-43ac-11e7-9399-5254005c3644'}

for i in range(30):
    payload['pn'] = str(i + 1)
    response = requests.post(url, data=payload, headers=headers, cookies=cookies, params=querystring)
    print(response.text)
    # time.sleep(1)