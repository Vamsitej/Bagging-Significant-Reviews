from selenium import webdriver
from bs4 import BeautifulSoup
import requests as rq
import pandas as pd
from time import sleep
import re



rating = []
review = []
comment = []
link = []



url = input('Enter URL: ')
driver = webdriver.Chrome("/Users/gadivemulavamsitej/Downloads/CapStone Project/chromedriver")
driver.maximize_window()
driver.get(url)
r1 = rq.get(url)
soup1 = BeautifulSoup(r1.text,'html.parser')
#soup = BeautifulSoup(html, features="xml")
driver.execute_script('window.scroll(0,2500)')
sleep(2)
for t in soup1.findAll('a', attrs={'href': re.compile("/product-reviews/")}):
    q=t.get('href')
    link.append(q)
#print(link)
    for i in link:
        if 'LSTMOBFH3XMSZHGY6ZPEK27RG' in i:
             aa= i
    f_url = ('https://www.flipkart.com'+ str(i))

i=1
while i<=5:
    ss=driver.get(str(f_url)+"&page="+str(i))
    qq=driver.current_url
    r2=rq.get(qq)
    soup=BeautifulSoup(r2.text,'html.parser')
    try:
        for ra in soup.find_all('div',{'class':'hGSR34 E_uFuv'}):
            aa=ra.get_text()
            rating.append(aa)
    except:
        for ra in soup.find_all('div',{'class':'hGSR34 _1nLEq1 E_uFuv'}):
            aa=ra.get_text()
            rating.append(aa)
        for re in soup.find_all('p',{'class':'_2xg6U1'}):
            bb=re.get_text()
            review.append(bb)
        for co in soup.find_all('div',{'class':'qwjRop'}):
            cc=co.get_text()
            comment.append(cc)
        sleep(1)
        i+=1
         

    
    
df= pd.DataFrame([rating,review,comment]).transpose()
df.to_excel('/Users/gadivemulavamsitej/Downloads/CapStone Project/Fk_reviews.xlsx')
https://www.flipkart.com/flipkart-perfect-homes-opus-engineered-wood-queen-box-bed/p/itm211146a630bb3?pid=BDDFHB352KARHSCP&lid=LSTBDDFHB352KARHSCPFOEIXW&marketplace=FLIPKART&srno=s_1_2&otracker=AS_QueryStore_OrganicAutoSuggest_2_13_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_13_na_na_na&fm=SEARCH&iid=f488f217-6566-4b83-bd33-4bec71cd75f0.BDDFHB352KARHSCP.SEARCH&ppt=sp&ppn=sp&ssid=xi52w604sw0000001614937755873&qH=079090167549a24f