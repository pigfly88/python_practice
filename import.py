import funcs
from collections import OrderedDict

print(funcs.test(1,2,3,4,5))
user1 = OrderedDict()
user1['name'] = 'pigfly'
user1['sex'] = 'femail'
user1['age'] = 31

for k,v in user1.items():
    print(k + ':' + str(v) + ' ')