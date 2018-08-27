import base64

import requests

# url = 'http://www.baidu.com'
# url = 'http://192.168.11.53:8080/'
# url = 'http://icanhazip.com/'
url = 'http://httpbin.org/post'

proxy = "118.89.60.145:16818"


# proxies = {'http': 'http://%s' % proxy, }

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    "Accept-Encoding": "Gzip",  # 使用gzip压缩传输数据让访问更快
    # "Proxy-Authorization": "Basic %s" % base64.b64encode(b"trygf521:a4c4avg9"),
}

proxies = {
    'http': '116.62.194.248:3128'
    # 'http': '101.236.35.229:8866',
    # 'http': '61.135.217.7:80',
    # 'http': 'http://118.116.41.24:8118',
    # 'https': 'https://60.13.187.162:63000',
    # 'https': 'https://114.225.171.179:53128',
    # "http": "http://trygf521:a4c4avg9@118.89.60.145:16818/",
    # 'http': 'http://trygf521:a4c4avg9@118.89.60.145:16818/'
}

myusername = 'trygf521'
mypassword = 'a4c4avg9'

# proxies = {"http":  "http://%(user)s:%(pwd)s@%(ip)s/" % {'user': myusername, 'pwd': mypassword, 'ip': proxy},
#               "https": "http://%(user)s:%(pwd)s@%(ip)s/" % {'user': myusername, 'pwd': mypassword, 'ip': proxy}}

response = requests.post(url, proxies=proxies, headers=headers)

print(response.status_code)
print(response.url)
print(response.headers)
print(response.text)
