# Import the necessary packages
from consolemenu import *
from consolemenu.items import *
import sqlite3
from datetime import datetime



db=sqlite3.connect('range.db')
c=db.cursor()

def inti():
    c.execute('CREATE TABLE IF NOT EXISTS poolsum (pool integar, name text,time text,sum integer)')
    db.commit()
    db.close()


def add(pool,name ):
    date=str(datetime.now().strftime('%Y-%m-%d |%H:%M'))
    c.execute('INSERT INTO poolsum VALUES(:pool,:name,:time,:sum)',{'pool':pool,'name':name,'time':date,'sum':None})
    db.commit()
    db.close()

def show(name_by=None):
    if name_by:
        c.execute('SELECT * FROM poolsum WHERE name =(:name)',{'name':name_by})
        resulte=c.fetchall()
    else:
        c.execute('SELECT * FROM poolsum')
        resulte=c.fetchall()
    return resulte    
    db.close()    


#inti()
#add(200,'m')

print(show('m'))


#pip install docopt