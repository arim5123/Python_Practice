import pymysql
import requests

headers = {"Accept": "application/json"}

name_url = "https://api.upbit.com/v1/market/all?isDetails=false"
price_url = "https://api.upbit.com/v1/candles/minutes/1"

name_response = requests.get(name_url, headers=headers)
price__response = requests.get(price_url, headers=headers)

con = pymysql.connect(host='localhost', user='root', password='1234', db='python_test', charset='utf8')
cur = con.cursor()

ndata = name_response.json()
pdata = price__response.json()

for i in range(0,len(ndata)) :
    num = str(i+1)
    name_val_01 = str(ndata[i]['korean_name'])
    name_val_02 = str(ndata[i]['english_name'])
    sql = "INSERT INTO subject_name VALUES (%s, %s, %s)"
    val = (num, name_val_01, name_val_02)
    cur.execute(sql, val)

    result = rows = cur.fetchall()
    print(result)

con.close()
