import requests

response = requests.get('https://www.baidu.com')

with open(r'baidu.html', 'wb') as f:
    f.write(response.content)

# GB2312 < GBK < GB18030
