import unittest
from selenium import webdriver
from bs4 import BeautifulSoup
from twilio.rest import Client
from time import sleep
import time
driver = webdriver.PhantomJS()
driver.get('https://www.amazon.com/Sony-DPT-RP1-B-Digital-Paper/dp/B072DXXXN1/ref=sr_1_3?ie=UTF8&qid=1514879751&sr=8-3&keywords=sony+dpt+rp1')

#soup = BeautifulSoup(driver.page_source, 'lxml')
#titles = soup.find_all('h3', {'class': 'ellipsis'})
#nums = soup.find_all('span', {'class': 'dy-num fr'})
         
         
#
def iselem(element):
        flag=True
        driver.refresh()
        try:
            driver.find_element_by_xpath(element)
            return flag
        except:
            flag=False
            return flag
classflag3=iselem("//*[@id='olp_feature_div']/div/span/*[contains(text(),'699')]")
while (classflag3 == True) :
    classflag3=iselem("//*[@id='olp_feature_div']/div/span/*[contains(text(),'699')]")
    driver.refresh()
    print('价格无变动')
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    
    
    with open('findlog.txt', 'r+') as f:
        content = f.read()        
        f.seek(0, 0)
        f.write(str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))+"\n"+content)
    
    
    time.sleep(40)

body = '价格改变了++++++++++++++++++'
def sendsms(body):
    account_sid = "ACedd76007a88f61e155325a3cb71fb3da"
    auth_token  = "63ac12761ebb2a562acf883a60e19787"
    client = Client(account_sid, auth_token)
    message = client.messages.create(to="+8618100180209",from_="+12403803744",body=body)
    with open('findlog.txt', 'r+') as f:
        content = f.read()        
        f.seek(0, 0)
        f.write(str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))+'价格改变了'+"\n"+content)
       # f.write(str('有货了')+"\n"+content)
        
    return('价格改变了')    
    

sendsms(body)     