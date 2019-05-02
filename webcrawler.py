import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.ptt.cc/bbs/MobileComm/index.html") #將網頁資料GET下來
print(r.text) #印出HTML

soup = BeautifulSoup(r.text,"html.parser") #將網頁資料以html.parser
sel  = soup.select("div.title a") #取HTML標中的 <div class="title"></div> 中的<a>標籤存入sel
for s in sel:
    print(s["href"], s.text) 

u = soup.select("div.btn-group.btn-group-paging a")#上一頁按鈕的a標籤
url = "https://www.ptt.cc"+ u[1]["href"] #組合出上一頁的網址
