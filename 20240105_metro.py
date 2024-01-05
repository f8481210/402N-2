#高鐵時刻表

#匯入模組
import requests
from bs4 import BeautifulSoup
import json #網頁的文件副檔名

#要傳遞的資料
data = {
        'SearchType': 'S',
        'Lang': 'TW',
        'StartStation': 'TaiPei', #起點站
        'EndStation': 'TaoYuan', #終點站
        'OutWardSearchDate': '2024/01/05', #日期
        'OutWardSearchTime': '20:00' #時間
        }

#網址
url = 'https://www.thsrc.com.tw/TimeTable/Search'

#發送請求 post
res = requests.post(url,data = data)

#解析
soup = BeautifulSoup(res.text,"html.parser")

#json to python
metro = json.loads(soup.text)

#print(metro)
for i in metro['data']['DepartureTable']['TrainItem']:
    trainNumber = i['TrainNumber'] #班次
    DepartureTime = i['DepartureTime'] #出發時間
    DestinationTime = i['DestinationTime'] #抵達時間
    print('車次:'+trainNumber, '出發時間:'+DepartureTime, '抵達時間:'+DestinationTime)


