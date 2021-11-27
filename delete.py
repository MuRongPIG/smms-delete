import requests
import json
import time

headers = {'Authorization': '填入你的smms apikey'}
url = 'https://sm.ms/api/v2/upload_history'
res = requests.get(url, headers=headers).text
data = json.loads(res)
data_ = data['data']
print(len(data_))
times = 1

for i in range(len(data_)):
    urll = (data_[i]['delete'])
    requests.get(urll)
    print(str(times) + '/' + str(len(data_)) + urll)
    time.sleep(2.5) # 改成你需要的秒数 建议不变
    times += 1

