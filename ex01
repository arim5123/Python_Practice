import pymysql
import requests

headers = {"Accept": "application/json"}

name_url = "https://api.upbit.com/v1/market/all?isDetails=false"
price_url = "https://api.upbit.com/v1/candles/minutes/1"

name_response = requests.get(name_url, headers=headers)
price__response = requests.get(price_url, headers=headers)

ndata = name_response.json()
pdata = price__response.json()

for i in range(0,len(ndata)) :
    print(ndata[i]['korean_name'])


con = pymysql.connect(host='localhost', user='root', password='Arim1004!', db='ei4db', charset='utf8')
cur = con.cursor()

sql = "SELECT * FROM account"

cur.execute(sql)
rows = cur.fetchall()

for i in rows :
    print(i)

con.close()
