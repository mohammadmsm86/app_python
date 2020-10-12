import calendar

y=int(input('enter year'))
m=int(input('enter mount'))

print(calendar.month(y,m))

import datetime

f=datetime.date(2000,7,13)
l=datetime.date(2007,1,20)

print(l-f)

# با این کتابخونه می تونید دسنور سیتمی را اجرا کنید مثلا 
#cmd  or linux
import subprocess

subprocess.call('ping 8.8.8.8')


import getpass

print(getpass.getuser())


import socket    
hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)    
print("Your Computer Name is:" + hostname)    
print("Your Computer IP Address is:" + IPAddr) 




import webbrowser

webbrowser.open('http://google.com')

