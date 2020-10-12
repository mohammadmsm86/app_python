import unittest
# اضافه کردن ماژول مورد نظر
import My_moduls
# چند نکته مهم 

#اسم کلاس مهم نیست هر می خواد باشه 
#اما اسم تابع خیلی مهمه که از دو قسمت تشکیل شده 
#  _ که باید باشد به همراه  test  قمست اول 
# قسمت دوم که باید با نام متدی که می خواهیم تست کنیم برار باشد 
class Test_app7(unittest.TestCase):

    #گاهی وقت ها یک ماژول ما کلی متد دارد و ما برای هر متد باید قبل آن اسم کلاس را بیاریم و این کار وقت گیز است و برای همین از 
    def setUp(self):
       self.emp=My_moduls

    #این متد زمانی اجرا میشود که یک متد شما تست شده باشد 
    def tearDown(self):
        print('hello')   
    @classmethod
    def setUpClass(cls):
        print('in start ')#این متد  فقط در اول تست اجرا می شود 
    @classmethod
    def tearDownClass(cls):
        print('in end ')#این متد فقط در پایان تست انجام میشود 
#هست  unittest  البته توجه داشته باشید که چهار  متد بالا فقط مربوط به کلاس 

    def test_add_number(self):
        number_sum=self.emp.add_number(5,5)
        self.assertEqual(number_sum,10)

    def test_hello(self):
        self.assertEqual(self.emp.hello(),'i love you M')


print(__name__)

if __name__ == '__main__':
    unittest.main()        