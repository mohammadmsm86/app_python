for a in 'MHMSM':
    print('hello')
 
# بعد از فور ها می توان از   esle استفاده کرد 

b=[1,2,8,56,100]
for c in b:
    print(c)


else:
    print('adad tamom shod ') 


#break شکستن حلقه 
#continue ادامه می دهد 
#pass

for c in 'string':
    if(c=='i'):
        continue#با درسیدن به این جا این قمست فور را انجام نمی دهد 
    print(c)
#i در مقادیر چاپ شده نیست 

list1=[]

for v in 'MHMSM':
    list1.append(v)
#/////////////////////////for in list 

list2=[ v for v in 'MSM']#مثل شرط گداشتن برای اضافه کردن چیزی به لیست هست 
print(list2)    

list3= [ s for s in range(20) if s%2 == 0]
print(list3)


#/////////////////////while
g=0
while g!=2:
    print('i love you god ')
    g+=1
else:
     print('tamam shod ')

#/////////////////////////////////fucntion 

#def ==defind

def hello():
    print('hello MHMSM')
    'doc string '#یعنی توضیحاتی درباره تابع 
    return '86'

hello()#وقتی صداش میزنم کار های داخل تابع را انجام میدهد

print(hello())#اما وقتی این طوری صداش میزنم مقدار return شد را نمایش میدهد 3

#count=? # یعنی خالی 


def print_hello(count):
    for i in range(count):
        print("hello")
        '''it is for count'''


 
print(print_hello.__doc__)

print_hello(int(input('enter count :')))

#//////////////////////////// globall && local

f=2 #globall

def add():
    
   # f=3#local
    # در حالت عادی مقدار متغییر محلی تغییر میکند و نمی نتوان از متغییری که در بالا تعریف شده استفاده کرد 
    #مگر اینکه مشخص کنیم که از کدام متغییر استفاده می کنیم 
    global f 
    f+=3
    return f

print(add())
#print(locals())#برای متغییر ها محلی 
#print(globals())#برای متغییر هاجهانی

#می توان در همان ابتدا به متغیر ها مقدار داد تا در صورت ندادن مقدار به صورت پیش ورز مقدار داشته باشد 
#نکته خیلی مهم نمی توان یکی را مقدرا پیش ورز داد و دیگری را نداد چون ارور می دهد 
# برای پیش نیامدن ارور متغیری که بهش مقدار پیش ورز نمی دهید را در ابتدا بگدارید 
def MHMSM(countr,name_love='MHM' ):
    return f'{name_love} {countr} man in ghadr doset darm'


#print(MHMSM('god',10000))به روشی دیگر هم میشود به متغییر ها مقدار داد 

#print(MHMSM(name_love='god',countr=100))#به روش می گویند کیبورد ارگمان 

print(MHMSM(10))

#در متد نویسی دو تا پارامتر مهم هست 
#*args =(1,'ali)= tuple 
#**kwargs = {name :"ali"} = dictionary 

# از این پارامتر ها موقعی استفاده می شود که ما نمی دانیم کاربر قرار است چند مقدار وارد کند 

def name(*arge,**kwargs):
    print(arge)
    print(kwargs)
#البته برای نام گدازی  پارامترها می توان از هر اسمی استفاده کرد ولی بهتر است از 
# *args & **kwargs     

#name('i am mohammad iam ','developer',age=19,my_love='god')

# اما اگر مغییر بود

list4=['MHMSM','developer']
list5={'age':19,'my_love':'god'}

#name(list4,list5)اما اگر این طوری مقدار دهیم همه را در *arge می گدارد
name(*list4,**list5)


#////////////////////////////////recursive function تابع بازگشتی 
#list6=[]

#def zarb(x):
 #   javab=0
  #  if  i<10:
   #     javab=x*i
    #    list6.append(javab)
     #   i+=1
      #  zarb(5)
   # else:
    #    return list6
  
     


#print(zarb(5))

#///////////////////////////////////lambda

#def number(num):
#    return num**2

#print(number(3))    


#///////////////////تبدیل به
#lambda
number =lambda num: num**2

print(number(5))

even=lambda enter: enter%2==0

print(even(5))


add= lambda x,y: x+y

print(add(10,10))



    


    




