class New:
    pass 

class1=New()#instance



class1.name='ali'#instance variable
class1.age=5


# or 

class Karmand:
    a=50#class vriable 
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname#instance varible
        self.email=fname+lname+'@MHMSM'
        # این اسم می توند هر چیزی  باشد ^  اینو  
    def full_nane(self):#اگر  نداشته باشد ارور دارد #slfe 
        print('i love god ')    
        #a+=10 ارور دارد چون نمی شناسد 
        Karmand.a+=10


#self چیست 
#به معنای نامی است که ما برای شی سازی انتخاب میکنیم ما در بالا نوشتیم 
#self.fname
#اما در اصل 
#class3.fname
#class3.lname

class3=Karmand('MHM','SM')
print(class3.email)
class3.full_nane()

print(Karmand.a)
#print(Karmand.__dict__)#همه اطالاعات کلاس 


#تفاوت class varible v instans varible
#
class variabl(Karmand):#ارث بری اما در ارث بری اول مقادیر داخل خود کلاس اجرا بعدش مقادیر داخل کلاسی  که برای ارث صداش کردیم 
    count=0
    def __init__(self):
        self.count+=1
        variabl.count+=1

#وقتی از self استفاده می شود این متغییر فقط برای خود شی ساخته شده می باشد 
# اما وقتی اسم کلاس در پشت متغییر متغغیر استفاده میشود با هر بار به گار بردن خود اسم کلاس متغییر اضافه می شود 

variabl2=variabl()
variabl3=variabl()
variabl4=variabl()
print(variabl.count)
print(variabl2.count)


#passبرای مواقعی که می خواهیم کلاسی را خالی رها کنیم یا متذی 

class devloper(Karmand):
    def __init__(self,fname,lname,age):
        super().__init__(fname,lname)
        #super== نام کلاس ارث برده شده ==karmand
        # در این جا چون ما قبلا اسم و فامیلی رو گرفته بودیم و خواستیم درباره اونو ذخیره کنیم این کار رو کردیم و فقط برای سن متغییر تعریف کردیم 
        self.age=age

class A:
    def __init__(self):
        print('class A')        



class B:
    def __init__(self):
        print('class B')  

class C(A,B):
    def __init__(self):
        super().__init__()#super همیشه به اولین کلاس ارث یری شده کار دارد 
        #Aکه میشود 
        #اما اگر خواستیم از کلاس دوم استفاده کنیم 
        B.__init__(self)
        print('class C')                  


v= C()

class hello:


    def __init__(self):
        self.a=10
        self._b=20 # variable private
        self.__c=30# مغییر مخصوص کلاس و غیر قابل دسترسی یا همان خصوصی فرقی با بالایی ندارد یکی  هست هر دوتاش 

         #Encapsulation کپسوله سازی 
    def seter (self,value):
        self._b=value
        self.__c=value   
    def geter(self):
        print(self._b)
        print(self.__c)
        self.__helloo()# صدا زدن متد خصوصی
        #Encapsulation کپسوله سازی 


    # method private 
    def __helloo(self):
        
        print('hello')

    # این متد فقط در کلاس استفاده میشود 



h=hello()

print(h.a)

#print(h.b)
#print(h.c)#ارور متغییر ها خوصوصی است 
h.geter()




#Decorator or properties

class add_name:
    def __init__(self,name):
        self.__name=name
    @property #این برای متد دریافت استفاده میشود 
    # اسم متد ها یکی است 
    def name(self):
        return self.__name


    @name.setter    #این برای ست کردن است 
    #اسم باید با خود متد برابر باشد 
    def name(self,value):
        self.__name=value

    
a=add_name('MHMSM86')

print(a.name)#در گر نیازی به گداشتن پرانتز نیست برای متد 
#خود برنامه می فهمید که با کدام متد کار داریم
a.name='god'#در گر نیازی به گداشتن پرانتز نیست برای متد
print(a.name)


#///////////////////static method

class car:
    @staticmethod#نیست self نیازی به 
    def my_math(x,y):
        return x*y


print(car.my_math(10,2))#نیاز یبه شی سازی هم نیست 



#////////////////////////////class method 

class MSM86:
   
    def __init__(self,name,famly):
        print('hello  '+name,famly)
            
    @classmethod
    def show (cls,name,famly):
        return cls(name,famly)
        #در رودی خود کلاس را به عنوان ورودی می گرد#cls==class 
        # وقتی از این روش استفاده می کنیم این متد در آخر خورجی اش را به خود کلاس بر می گرداند 
        #و از همه مهم تر اینکه برای استفاده از متد نیازی به شی سازی نیست 

MSM86.show('ali','mohammad')#نیاز یبه شی سازی هم نیست 


#/////////////////////////////////////////Polymorphism


class cat :
    def sound(self):
        print('cat')

class dog :
    def sound(self):
        print('dog')


def make_sounf(anilml):
    anilml.sound()


cat1=cat()
dog1=dog()
make_sounf(cat1)        
#/////////////////////////////////////////Polymorphism    

#////////////////////////////////////////////////////////// SpecialMethods
#__str__
#&
#___
#__repr__

class test:
    def __repr__(self):#با اندکی تفاوت است زیاد کاربردی نیست 
        return 'god.'

test1=test()
print(test1)


class test2:
    def __str__(self):
         return 'god {}{}{}{}{}'.format('h','e','l','l','e')
    

test3=test2()
print(test3)      
#////////////////////////////////////////////////////////// SpecialMethods