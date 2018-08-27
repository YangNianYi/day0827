import urllib3

http = urllib3.PoolManager()

response = http.request('GET', 'http://www.zhihu.com')

print(response.status)
print(response.data.decode())
