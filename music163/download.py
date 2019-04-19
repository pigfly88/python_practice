import requests

name = input();
params = {
    's': name,
    'type': 1,
    'offset': 0,
    'sub': 'false',
    'limit': 20
}
r = requests.get('http://music.163.com/api/search/get', params=params)
res = r.text
print(res)