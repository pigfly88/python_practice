# 获取双色球最近一次的开奖结果

import requests

# 接口地址
root = 'http://www.cwl.gov.cn/cwl_admin/'

# 根据彩种名称和期号获取开奖信息
# 传入参数 name=3d,ssq,qlc 和 code=2017001
jtq = 'kjxx/findKjxx/forIssue'

# 获取往期开奖信息内容
wqcx = 'kjxx/findDrawNotice'

headers = {
    'Referer': 'http://www.cwl.gov.cn/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
}
r = requests.get(root+wqcx, headers=headers, params={'name':'ssq', 'issueCount':1})
#print(r.status_code);
#print(r.text);

if(len(r.text)==0):
    print('fail')
else:
    jsonres = r.json()
    print('%s %s: %s / %s' %(jsonres['result'][0]['name'], jsonres['result'][0]['date'], jsonres['result'][0]['red'],jsonres['result'][0]['blue']))