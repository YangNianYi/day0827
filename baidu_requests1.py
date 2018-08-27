import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

params = {'wd': '尚硅谷'}

response = requests.get('https://www.baidu.com/s', params=params, headers=headers)
# response = requests.get('http://192.168.11.63:8080', headers=headers)

print(response.headers)
print(response.url)
with open(r'尚硅谷.html', 'wb') as f:
    f.write(response.content)

# GB2312 < GBK < GB18030
