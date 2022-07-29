import requests

headers = {"Accept": "application/json"}

name_url = "https://api.upbit.com/v1/market/all?isDetails=false"
name_response = requests.get(name_url, headers=headers)
ndata = name_response.json()

now_cnt = 0
all_cnt = len(ndata)

for now_cnt in range(0,all_cnt) :
    name = ndata[now_cnt]["korean_name"]
    price_url = "https://api.upbit.com/v1/candles/minutes/1"
    query = {"market": name, "count": "1"}
    price_response = requests.request("GET", price_url, params=query)
    pdata = price_response.json()
    price = pdata[now_cnt]["opening_price"]
    print("현재 %s의 시세는 %s 원 입니다..." % (name, price))
    now_cnt = now_cnt + 10
