import sqlite3

db=sqlite3.connect(':memory:')#این دیتا بیس به دلیل نداشتن نام فقط در خود حافظه موقت ذخیره میشود

db1=sqlite3.connect('my_name.db')#در هارد ذخیره میشود 

c=db1.cursor()#cursor == مکان نما 


c.execute('CREATE TABLE IF NOT EXISTS MHMSM (name text , family text )')

c.execute(' INSERT INTO MHMSM VALUES ("mohammad","MHMSM86")')     

name=input('enter name :')
family=input('enter family :')

c.execute('INSERT INTO MHMSM VALUES (:name,:family)',{'name':name,'family':family})
#برای ذخیره کردن تغییرات 

c.execute('UPDATE MHMSM SET name=mm WHERE name= mohammad AND family=MHMSM86')
db1.commit()


c.execute('SELECT * FROM MHMSM')
print(c.fetchall())
db1.close()

print('hello')