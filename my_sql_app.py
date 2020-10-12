# ابتدا برنامه mysql را نصب 
#بعد دستور زیر را وارد کنید 
#pip install mysql-connctor-python

import mysql.connector

sql=mysql.connector.connect(host='localhost ', user='root',password='135479.ئخ')

print(sql)

edit=sql.cursor()

edit.execute('CREATE DATABASE IF NOT EXISTS MHMSM86')

edit.execute('SHOW DATABASES')

for show in edit:
    print(show)