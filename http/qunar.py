import json
import requests
from pprint import pprint

url = "https://flight.qunar.com/touch/api/domestic/wbdflightlist"

querystring = {
    "departureCity": "北京",
    "arrivalCity": "南京",
    "departureDate": "2018-11-01",
    "ex_track": "",
    "__m__": "3e4e469cc5f474b31be6c46da6a0ac9a",
    "sort": ""
}

headers = {
    '6b3dd5': "134c11b30a3020d74c45e67833c3050d",
    'accept': "text/javascript, text/html, application/xml, text/xml, */*",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "zh-CN,zh;q=0.9,en;q=0.8",
    'content-type': "application/x-www-form-urlencoded",
    'cookie': "QN170=111.194.47.49_8d7ef3_0_6eQlh7vKpbLmfnEGBooTHRsU7fyjDkZqje%2BTFDULmjE%3D; "
              "F235=1540902914621; "
              "QN1=05dvHlvYVXlxDqlmC7NNAg==; "
              "QN601=4055de4ec9c51b2669af0adfb3dca6d5; "
              "QN300=organic; "
              "QN99=2589; "
              "QN205=organic; "
              "QN277=organic; "
              "csrfToken=TdbtjRu3bMAZSYlc5cTxGddgpNZduX7i; "
              "QN269=0FF9E0A1CF3511E7816AFA163E9BF76E; "
              "_i=VInJOZjV_T7qU-ZxZEikKoIO5dpq; "
              "QN48=79a27849-b1ac-4774-bcda-1e794d8fdf97; "
              "F234=1540904321226; "
              "fid=6db0ff51-2876-4e53-a943-ce5a2301d73b; "
              "_RF1=111.194.44.254; "
              "_RSG=3jqJtS7WBvADbQepljDdt8; "
              "_RDG=28c10b35a2c38a21661d9bd66cea46676a; "
              "_RGUID=ae4b8077-374f-4b43-8de7-36dbf3a1a94d; "
              "SC18=; "
              "QunarGlobal=10.88.125.22_-1f2cda41_166c45f79f6_3393%7C1540904321284; "
              "QN621=fr%3Dqunarindex%261490067914133%3DDEFAULT; "
              "_vi=EDt5p7JDXBmcCi3kihs2rQETdPKOmv_dbpauyz-o7hOoaZlvBVPwGcpLKdGFKxOhHjYfLrt4bHOk3AYDTq5J15ce6cQ6oqFSa7TfnwKTZv5IOfO1J8xZOb1TCfGPhuiM8cjro9ZGmqCE5Yz5e1MBpx3NRbvgd6gW_6W_jA9qIu4A; "
              "QN271=29d96fca-e5f3-447e-9a80-bfbe54487cea; "
              "QN667=B; "
              "QN668=51%2C55%2C54%2C50%2C59%2C50%2C56%2C50%2C58%2C53%2C55%2C51%2C50; "
              "QN267=140222306028f0fc73",
    'dnt': "1",
    'referer': "https://flight.qunar.com/site/oneway_list.htm?searchDepartureAirport=%E5%8C%97%E4%BA%AC&searchArrivalAirport=%E6%88%90%E9%83%BD&searchDepartureTime=2018-11-01&searchArrivalTime=2018-11-04&nextNDays=0&startSearch=true&fromCode=BJS&toCode=CTU&from=qunarindex&lowestPrice=null",
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
    'x-requested-with': "XMLHttpRequest",
    'Cache-Control': "no-cache",
    'Postman-Token': "af761922-676b-6226-f77e-f9fe3bea2116"
}

response = requests.request("GET", url, headers=headers, params=querystring, verify=False)

result = json.loads(response.text)
pprint(result)
