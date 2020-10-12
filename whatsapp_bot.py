from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

deriver=webdriver.Chrome(r'C:\Users\MHMSM\Desktop\python\chromedriver.exe')

deriver.get('https://web.whatsapp.com/')
input('are you ready?????...')
#ساخت xpath 
#xpath == // tag [@خصیصه = ""]
deriver.find_element_by_xpath('//span[@title = "{}"]'.format('محمد رضا')).click()
time.sleep(1)
msg= deriver.find_element_by_class_name('_3uMse')

for i in range(1000):
    try:
        msg.send_keys('سلام من محمد حسین هستم و این رباتی هست که ساختم امید وارم خوشت بیاد پسر عمو جان ')
        time.sleep(2)
        button= deriver.find_element_by_class_name('_1U1xa')
        button.click()
        time.sleep(2)
        print(i)
    except:
        pass  
    
