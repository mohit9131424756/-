# -*- coding: utf-8 -*-
"""
@author: mohit sawal
"""
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
my_url='https://www.moneycontrol.com/india/stockpricequote/banks-private-sector/yesbank/YB'
uClient=uReq(my_url)
page_html=uClient.read()
uClient.close()
#print(page_html)
page_soup=soup(page_html,'html.parser')
containers=page_soup.findAll("div",{"class":"pcnsb div_live_price_wrap"})
container=containers[1]
#<div class="pcnsb div_live_price_wrap">
 #<span class="span_price_wrap stprh grn_hilight grnclr"># IF SHARE PRICE IS UP 
  #25.10
 #</span>
 #<span class="span_price_arrow green_arwup">
 #</span>
# <span class="span_price_change_prcnt grnpc1">
 # 0.55
  #<em>
   #(2.24%)
  #</em>
 #</span>
#</div>
 ###THIS IS A CODE AFTER INSPECTING YES BANK VALUE AT MONEYCONTROL WHEN POSITIVE
price=container.findAll("span",{"class":"span_price_wrap stprh grn_hilight grnclr"})
if price!=[]:
    print(price[0].text)
    price=container.findAll("span",{"class":"span_price_change_prcnt grnpc1"})
    print(price[0].text)
else:
    
    price=container.findAll("span",{"class":"span_price_wrap stprh red_hilight rdclr"})
    print(price[0].text)#print price
    price=container.findAll("span",{"class":"span_price_change_prcnt rdpc1"})
    print(price[0].text) #print change and % change
      
