import pymysql
import requests
from datetime import datetime

headers = {"Accept": "application/json"}

con = pymysql.connect(host='localhost', user='root', password='1234', db='python_test', charset='utf8')
cur = con.cursor()

name_url = "https://api.upbit.com/v1/market/all?isDetails=false"
price_url_01 = "https://api.upbit.com/v1/candles/minutes/1?"

name_response = requests.get(name_url, headers=headers)
name_data = name_response.json()

# for i in range(0,len(name_data)) :
#     num = str(i+1)
#     market = str(name_data[i]['market'])
#     k_name_val = str(name_data[i]['korean_name'])
#     e_name_val = str(name_data[i]['english_name'])
#
#     sql = "INSERT INTO subject_name VALUES (%s, %s, %s)"
#     val = (market, k_name_val, e_name_val)
#     cur.execute(sql, val)
#     con.commit()

now = datetime.now()
current_time = now.strftime("%D,%H:%M")

sql = "SELECT * FROM subject_name"
cur.execute(sql)
rs = cur.fetchall()

for row in rs:
    market = str(row[0])
    price_url_02 = market+"&count=1"
    price_url = price_url_01 + price_url_02
    price_response = requests.get(price_url, headers=headers)
    price_data = price_response.json()
    #price = str(price_data[0]['trade_price'])
    print(price_url)
    # sql = "INSERT INTO subject_price VALUES (%s, %i, %s)"
    # val = (market, price, current_time)

con.close()



