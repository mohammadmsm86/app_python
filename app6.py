
#///////////////////////////نوشتن ارور اختصاصی خودمان 
class Error(Exception):
    pass

class Number_big (Error):
    pass    
class Number_small(Error):
    pass

gese =45
while True:
    user=int(input('enter number :'))

    try:
        if user > gese:
            raise Number_big
        elif user < gese:
            raise Number_small

        elif user == gese:
            break

   
    except Number_big  :
        print('number gese >')
    except Number_small:
        print('number gese <')

