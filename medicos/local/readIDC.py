import urllib3

http = urllib3.PoolManager()

r = http.request('GET', 'http://google.com/')

print(r.status, r.data)