from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys



driver = webdriver.Chrome(r'C:\Users\MHMSM\Desktop\python\chromedriver.exe')

driver.get('https://www.instagram.com/')
time.sleep(1)
driver.find_element_by_name('username').send_keys('mohammad.h.m.stm32@gmail.com')
time.sleep(1)
driver.find_element_by_name('password').send_keys('135479.mo')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
time.sleep(1)
search=input('enter :')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(search)
for i in range(2):
    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(Keys.ENTER)
    time.sleep(10)

input('enter:')
pic=[]
pic=driver.find_element_by_tag_name('a')

pic_real=[]

for i in pic :
    if i in 'https://www.instagram.com/p/':
        pic_real=i
    else:
        continue    

print(pic_real)    




