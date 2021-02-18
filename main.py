import pandas as pd
import datatime
import requests 
from bs4 import BeautifulSoup 

def real_time_price(stock_code): 
    #get url from the site
    url = ('https://ca.finance.yahoo.com/quote/') + stock_code + ('?p=') + stock_code + ('&.tsrc=fin-srch')
    r = requests.get(url)

    web_content = BeautifulSoup(r.text, 'lxml')
    web_content = web_content.find('div', class_="D(ib) Va(m) Maw(65%) Ov(h)") #locating the class name from yahoo finance's site directly 
    web_content = web_content.find('span').text #find the span tag

    if web_content == []:
        web_content = "000" #if data is not received 

    return web_content

print(real_time_price("AAPL"))

for step in range (1, 101):
    price = []
    col = []
    time_stamp = datetime.datatime.now()
    time_stamp = time_stamp.strftime("%Y-%m-%d %H:%M:%S")
    price.append(real_time_price("AAPL"))
    col = [time_stamp]
    col.extend(price)
    df = pd.DataFrame(col)
    df = df.T
    df.to_csv('storing-data.csv', mode='a', header=False)
    print(col)