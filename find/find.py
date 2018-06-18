from selenium import webdriver
from twilio.rest import Client
from time import sleep
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.PhantomJS()
driver.get("http://pur.store.sony.jp/digital-paper/products/DPT-RP1/DPT-RP1_purchase/") 
b = driver.find_element_by_link_text("入荷待ち").value_of_css_property("background-color").find('245, 229, 136, 1')

    
while b == 5:
    
    driver.refresh()
    b = driver.find_element_by_link_text("入荷待ち").value_of_css_property("background-color").find('245, 229, 136, 1')
    print('没货了')
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    
    
    with open('findlog.txt', 'r+') as f:
        content = f.read()        
        f.seek(0, 0)
        f.write(str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))+"\n"+content)
    
    
    time.sleep(50)
    
body = '有货了++++++++++++++++++'
def sendsms(body):
    account_sid = "ACedd76007a88f61e155325a3cb71fb3da"
    auth_token  = "63ac12761ebb2a562acf883a60e19787"
    client = Client(account_sid, auth_token)
    message = client.messages.create(to="+8613013123381",from_="+12403803744",body=body)
    with open('findlog.txt', 'r+') as f:
        content = f.read()        
        f.seek(0, 0)
        f.write(str(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))+'有货了'+"\n"+content)
       # f.write(str('有货了')+"\n"+content)
        
    return('有货了')    
    

sendsms(body)