print ('MHMSM')#for CM = comment
#نکته های مهم 
#immutable =بدون تغییر 
#variable=متغییر
MHMSM=86
MSM='MHMSM'
M=int(MHMSM)#convert
V=0xA0 #hax
d=MHMSM+2
print(d)
a=b=c=1
A,B,C=1,2,'MHMSM'

m=20
del m #کلا با متغییر پاک می شود 
#del m,b دوتا شو پاک می کند 
print (MHMSM)
print(MSM)
print(a)
print(C)
print(type(B))
#//////////////////////////////////////////
a1=10
b1=20
print(a1+b1)
print(a1-b1)
print(a1*b1)
print(a1/b1)#خارج قسمت
print(a1%b1)#باقی مانده
print(a1**b1)#توان
print(a1//b1)#باقی مانده ولی گرد شده 

print(a1==b1)


#/////////////////////////////list
x=[1,2,3,5]
print(1 in x)
print(10 not in x )

#هر متغییر در حافظه ذخیره شود یک ادرس ای دی دارد برای فهمیدن آن 
x_id=id(x)
a1_id=id(a1)
print(a1_id)
print(a1_id is a1_id)

#/////////////////////////////////////////
#''با ""  فرقی ندارد

#'''  '''==""" """در این روش شما می تونید از اینتر هم استفاده کنید 
#''' MHMSM 
# 86'''
m='hello'
print(m[3])#از اول نشون بده 
print(m[-1])#از آخر نشون بده 

print(m[0:3])
#      start :end 
print (m+ "   hello")
print(m[0:5:2])
#    start:end:step
print(m*2)
print('mskmkn k\n ksdlmsd k')
print('mskmkn k\\n ksdlmsd k')
print(r'mskmkn k\n ksdlmsd k')#r string 

#/////////////////////////////////////نمایش متن به سه صورت 
#////////////////////////به صورت در صدی
print('hello %s c i f d '%m)
print('avg %f '%12.75)
print('avg %.1f'%12.75)
#%s strin %c char %i int %f float 
#///////////////////////////به صورت    format string 
print('hello  {}SM'.format('MHM'))
r='mkasfmkaf {}  fsf'
print(r.format('allah'))

f='i{0} you {1}{2}'
print(f.format('love','MSM',86))
#//////////////////////////////////////// 
print('salam {0} man shod{1:20}'.format('moadel',18.95))

print('salam {0:<20} man shod{1:>20}'.format('moadel',18.95))#برای فاصله گداری از سمت چپ یا راست 


print('salam {0:^20} man shod{1:^20}'.format('moadel',18.95))#برای فاصله گداری از دو طرف  

print('{0:*^50}'.format('i love you god'))
#///////////////////////////////////////////f string 
gomle='i love you'
gomle1='MSM'
gomle2=86

print(f'i {gomle}  {gomle1}{gomle2}')
print(f'i {2+2}  {5*5 :*>20}  {10-1}')

#////////////////////////////////////////
a2='i love you \t god '
a3='kndkandkadnkawdnkawd'
a4='   '
print(a2.capitalize())
print(a2.count('o'))
print(a2.count(''))

print(a2.expandtabs(50) )

print(a3.isalnum())#آیا عدد یا حروف در جمله هست یا نه 
print(a3.isalpha())#آیا  حروف در جمله هست یا نه 
print(a3.isalpha())#آیا  حروف در جمله هست یا نه 
print(a4.isspace())
print(a3.islower())#آیا  حروف کوجیک  در جمله هست یا نه 
print(a3.isupper())#آیا  حروف بزدگ در جمله هست یا نه 

#//////////////////////////////tuple 
char1 = '-'
char2 = ('a','b','c')
print(char1.join(char2))
print(char2[0].join(char2))

print(len(a3))
print(a3.lower())
print(a3.upper())

a5='i love you god '
print(a5.split(' '))
print(a5.find('g'))

new = a5.replace('i','me')
print(new )

#برای کمک کردن و فهمیدن متد ها 
print(help(int.imag))


#////////////////////////////

b2=['mohammad','MHMSM','86']#list 
b3=[1379,1386,1366]

b2.append('i love you god ')

print(b2[2])
del b2[1]

print(b2+b3)#کان کتینت یا جمع کردن 
print(b2*2)#repit کردن 

print(86 in b2)
print(len(b2))

print(min(b2, key=len))#کم ترین میزان کاراکتر 


g=('mas,mef','knak')#tuple
list1=list(g)
print(g)
print(list1 )

 

b4=list(range(5))
print(b4)

#تفاوت 
#append 
#با
#extand 

#append کلا همه رو اضافه می کنه که شامل این هم میشه []
#extand فقط مقدار داخل لیست رو اضافه میکنه 

b3.insert(0,86)
print(b3)
#b3.pop()#اخرین مقدار حذف می شود 

b3.remove(1366)
print(b3)


b3.reverse()
print(b3)

b3.sort()
print(b3)

b3.sort(reverse=True)
print(b3)


print(b3.index(86))

b3=str(b3)
b3='-'.join(b3)
print(b3)
#//////////////////////////////tuple 
tuple1=('i love god ','MHMSM',86)# it is a tuple 
tuple2=(2)#it is not tulpe 
tuple3=(2,)#it is a tuple 

#tuple1[2]='86'#error  this is a immutable :(
print(tuple1)

print(tuple1 + tuple3)

tuple1+=(1379,)
print(tuple1)
#//////////////////////////////////////dictionary


dictionary={1:'i love you god ','86':'MHMSM',3:[1,'kasfn']}#از دو قسمت تشکیل شده است اولی کلید و دومی مقدار 
print(dictionary['86'])

dictionary[1]='I lOVE GOD '
dictionary['MSM']='i love you mahya '

# پون این کلید وجود ندارد کلید را ساخته و مقدار را درونش قرار میدهد 
# del dictionary
# del dictionary[3]
dictionary.clear()#فقط ایتم ها پاک می شود 
#b={'a':1,'a':2,'a':5}کلید های تکراری به حساب نمیاید و فقط آخری حساب می شود 

dictionary1={'MHMSM',86,'god'}#ساخت دیکشنری بدون مقدار  

dictionary1=dict.fromkeys(dictionary1,'10')

print(dictionary1)

dictionary.update(dictionary1)#برای اضافه کردن 

print(dictionary)

print(dictionary.values())
print(dictionary.keys())


#///////////////////////////////////nested _ Dictionary
nested_dict={1:{'MHMSM':86}, 2:{86:'MHMSM'}}

print(nested_dict[1]['MHMSM'])

#/////////////////////////////set
set1={1,'MHMSM',86,(2,1,'mhmsm')}
set2={1,2,3,4}
set3={4,5,6,7}
print(set1)#درون ست ها از  لیست و دیکشنری نمیشه اسنتفاده کرد ولی از تاپل ها میشود 
print(type(set1))#نکته مهم در ست ها مقدار های تکراری نه نمایش داده می شود و نه حسابمی شود 
#dictionary VS set 
#{1:86} | {}    VS  {,}

set1.add('i love god ')
set1.update([1,2,86,79])
#تفاوت 
# add فقط برای اضافه کردن یک مقدار 
# با 
# update برای اضافه کردن همه چند تا چیز 
#             

set1.remove(1) #اگر عضویی که بخواهیم حدف کنیم وجود نداشته باشد ارور دارد
set1.discard(1) #اگر عضویی که بخواهیم حدف کنیم وجود نداشته باشد ارور ندارد


print(set2 |  set3)#اجتماع گرفتن   
#print(set2.union(set3))

print(set2 & set3)#اشتراک گرفتن 
#print(set2.intersection(set3))

print(set2 - set3)#اختلاف گرفتن 
#print(set2.difference(set3))

print(set2 ^ set3)#چیز هایی که هم در اولی و هم در دومی نست 
#print(set2.symmetric_difference(set3))


#//////////////////////////////////////if & else 
#else if = elif    
num = int(input('enter :'))
if num>100:
    print('hello')

elif num==86:
     print('i live god ')

else:
    print('MHMSM')

 #num1=input('enter nummer ')در حالت پیشوز به صورت رشته می گرد 
 

   

 
    


