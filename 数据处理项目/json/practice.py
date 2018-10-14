# @Time    : 2018/10/9 20:51
# @Author  : Yanlin Wang
# @Email   : wangyl_a@163.com
# @File    : practice.py

import json

path_dir = 'a.json'
temp_str = []
json_str = {'seg_detail': temp_str}
print('seg', json_str)
with open(path_dir, 'w') as dump_f:
    json.dump(json.loads(json.dumps(json_str)), dump_f)
print('export ' + path_dir + ' success!')
