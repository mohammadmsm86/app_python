# ////////////////////////////////////////////Directory
import os

print(os.getcwd())#محل اجرا شدن کد 
os.chdir(r'C:\Users\MHMSM\Desktop\python')#عوض کردن مسیر 

os.mkdir('test')#ساخت پوشه جدید

os.rmdir('test')
#os.remove('f.txt')
print(os.listdir(r'C:\Users\MHMSM\Desktop\python'))
os.rename('f.txt','hello.txt')
os.rename('hello.txt','f.txt')
print(os.stat('f.txt'))


#///////////////////////////////////try & ecxept
try:
    f=open('m.txt')
except :#به طور کلی 
    print('Error!!!')   

#except (IndentationError,NotADirectoryError):#مشخص شده برای دو ارور
    #print('IndentationError')    

finally:#در هر صورت اجرا میشود 
    print('anyway runed ')     

#///////////////////////////////صدا زدن یک ارور 
try:
    o=open('f.txt')
    if o.name=='f.txt':
        raise  NameError#//////////////reise == بالا اوردن 


except NameError as e:
    print(e)
