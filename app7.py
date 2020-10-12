#//////////////////////////moduls 

# برای اضافه کردن ماژول های به غیر از خود برنامه باید اون ماژولی را که می خواهیم اضافه کنیم در کنار خود برنامه خودمان باشد 

import My_moduls
#به چند روش می توان کار کرد 

My_moduls.add_number(10,20)
print(My_moduls.MHMSM)
My_moduls.hello()



#1 تغییر اسم ماژول
import My_moduls as M
M.add_number(10,20)
print(M.MHMSM)
M.hello()



#اضافه کردن بخشی از یک ماژول

from My_moduls import MHMSM,hello

#My_moduls.add_number(10,20)در دست رس نیست 
print(My_moduls.MHMSM)
My_moduls.hello()


#اما گاهی وقت ها هست که ما نمی دونیم ماژول که چیزهای درون خود دارد برای همین از این دستور استفاده می شود 
print(dir(My_moduls))


import my_moduls_folder.sound.My_moduls

my_moduls_folder.sound.My_moduls.add_number(5,20)


#/////////////////////////cmdنصب ماژول از طریق 
# 


#////////////////////pip install .....
#/////////////////////pip uninstall

#//////////////////////////pip list -o  ماژول هایی که بروز نیستند 
#//////////////////////////////pip install -U اسم ماژول 


#/////////////////////////////////functon map 
b=[1,2,5,6,9,7,10]
def temp (a):
    return a +5

m=map(temp,b)
print(list(m))

#////////////////////////////////////function filter 
def zoge(num):
    if(num%2==0):
        return True
    else:
        return False
    


v=[0,1,2,3,4,5,6,7,8,9,10]        
print(list(filter(zoge,v)))


#//////////////////////////////////////// named tuple 

from collections import namedtuple

a=namedtuple('MHMSM86','age name location ')
#///  ////name tuple /// field name
a(19,'mohammad','qom')

print(a.name)

#/////////////////////////////////////namede tuple 

#///////////////////////////////////decorator 

#یعنی متدی که به عنوان ورودی یک متد دیگر می گیرد
#و برای کوچکی کردن کد هم استفاده می شود 
def my_decorator(fun):

    def wrapper():
        print('befor')
        fun()
        print('after')
    return wrapper# با این کار می توان متد را هم صدا زد بدون اینکه کاربر آن را صدا برند 

def say_hello():
    print('hello')

say_hello = my_decorator(say_hello)
say_hello()

# البته به یک روش دیگر هم می توان استفاده کرد 

# این روش جدید و بهتر است :)
def my_decorator1(fun):

    def into(f):
        print('befor method 1')
        fun(f)
        print('after method 1')
    return into 


@my_decorator1 #  با این کار وقتی ما متد زیر زا صدا می زنیم متد بالا هم صدا زده می شود
def say_hello1(n):
    print('hello  '+n)

say_hello1('ali')


#/////////////////////////////////////////////مثال 



user={'ali':'123456','mahya':'8668'}

def login(fun):
    def chek(username,password):
        if(username in user.keys() and password == user[username]):
            return fun(username,password)

        elif (username not in user.keys() or password != user[username]):
            print('not defind')        
    return chek
@login
def comment(username,password ):
    print('hello ths is comment ')

comment('mahya','8668')


#////////////////////////////////////iteratol یا تکرار کننده 

#iter() کار این متد قابل شمارش کردن چیزی است و تکرار مدام آن است 

list1=[1,2,3,4]

iterator=iter(list1)

#next()از این متد برای رفتن به چیز بعدی در چیز های قابل شمارش 

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


#////////////////////////////////Generator  

#Generator
#استفاده میشود  yeild از  return همان متد فقط به جای 

#تفاوت 
#return 
#با 
#yeild

#در گزینه 1 مقدار بازگشتی در هیچ کجا ذخیره نمیشود و فقط در هنگام صدا زدن متد می توان از مقدار بازگشتی استفاده کرد 

#اما در گزینه 2 مقدار بازگشتی ذخیره مشود 

def my_generator():
    n=1
    print('one ')
    yield n

    n+=1
    print('two ')
    yield n

    n+=1
    print('three ')
    yield n

my_generator1=my_generator()
print(next(my_generator1))    

print(next(my_generator1))    

print(next(my_generator1))    # می کند iter  همه را yeild  استفاده شده ایت است چون  next علت اینکه از 

#////////////////////////////////////for test unittest

def add_test(x,y):
    return x + y
    





