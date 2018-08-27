import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

response = requests.get('https://www.baidu.com', headers=headers)

print(response.headers)
with open(r'baidu.html', 'wb') as f:
    f.write(response.content)

# GB2312 < GBK < GB18030
