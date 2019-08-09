import time

import requests
import re
import numpy
import csv


headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'
}

url = 'http://www.nows.fun/'

content = []

for x in range(5000):
    try:
        res = requests.get(url, headers=headers)
    except:
        print('反爬虫延迟三秒后再爬')
        time.sleep(3)
    temp = re.findall('<span id="sentence" style="font-size: 2rem;">(.*?)</span>', res.content.decode('utf-8'), re.S)
    print('爬取：', temp)
    # content.append(temp[0])
    with open('data.csv', 'a', newline='') as f1:
        csv_write = csv.writer(f1)
        csv_write.writerow(temp)
    time.sleep(0.5)

# 去掉重复项
# content = list(set(content))
# print('去重后：', content)

# numpy.savetxt('data.csv', content, delimiter=',')

# with open('data.csv', 'w', newline='') as f1:
# with open('data.csv', 'w') as f1:
#     csv_write = csv.writer(f1)
#     csv_write.writerow(content)
    # for x in content:
    #     csv_write.writerow(x)
    #     print('写入数据：', x)
