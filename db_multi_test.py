# coding=utf-8

import pyodbc
import time

server = 'poetic-image.database.windows.net'
database = 'poetic_image'
username = 'administor'
password = 'PoeticImage.abc'
driver= '{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

datetime = time.strftime('%Y-%m-%d %H:%M:%S')
id = 6
poetry = u'宋祖英， 周公子'
query = "insert into dbo.Main VALUES (?, ?, ?, ?)"
cursor.execute(query, [id, poetry, 0.01, datetime])
tag_list = ['man', 'woman']
for tag in tag_list:
    cursor.execute("insert into dbo.Image_Tag VALUES (?, ?)", [id, tag])

cursor.execute(u"insert into dbo.Image_Comment VALUES (?, ?)", [id, u'非常差'])
cnxn.commit()


cursor.execute("SELECT * from dbo.Main")

row = cursor.fetchone()
while row:
    print (row)
    print (row[1])
    row = cursor.fetchone()