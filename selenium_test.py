#pip install selenium 
#نصب دربوار مروگر برای 
#selenium

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver =webdriver.Chrome(r'C:\Users\MHMSM\Desktop\python\chromedriver.exe')
#////////////////////   ^محل نصب درایور که اگه محل نصب درایور در کنار خود 

#نکته خیلی مهم همیشه برنامه تان را با cmd باز کنید 

driver.get('https://google.com')

driver.find_element_by_name('q').send_keys('love m')
#driver.find_element_by_name('btnK').send_keys(Keys.ENTER)

driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]').send_keys(Keys.ENTER)
#این روش خیلییییییییییی  بهتر است 

driver.execute_script('window.scrollTo(0, 100)')#کد های اسکریپت 
time.sleep(2)

driver.execute_script('window.scrollTo(0, 500)')#کد های اسکریپت 
time.sleep(2)

driver.execute_script('window.scrollTo(0, 1000)')#کد های اسکریپت 
time.sleep(2)

driver.execute_script('window.scrollTo(0, 100)')#کد های اسکریپت 
time.sleep(2)

driver.close()
