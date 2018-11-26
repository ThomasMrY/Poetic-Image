import pyodbc

server = 'poetic-image.database.windows.net'
database = 'poetic_image'
username = 'administor'
password = 'PoeticImage.abc'
driver= '{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.execute("SELECT * from dbo.test")
# cursor.execute("SELECT TOP 20 pc.Name as CategoryName, p.name as ProductName FROM [SalesLT].[ProductCategory] pc JOIN [SalesLT].[Product] p ON pc.productcategoryid = p.productcategoryid")

row = cursor.fetchone()
while row:
    print (str(row[0]) + " " + str(row[1]))
    row = cursor.fetchone()

# cursor.execute("INSERT INTO dbo.test VALUES (456, 123, 678, 1213, 000)")
# with open('D:\\data\\local\\coco\\images\\val2014\\COCO_val2014_000000000042.jpg', 'rb') as img:
#     print("INSERT INTO dbo.test VALUES (0,1,2,3,4,NULL,\"{}\")".format(img.read().encode('base64')))
#     cursor.execute("INSERT INTO dbo.test VALUES (0,1,2,3,4,NULL,\"{}\")".format(img.read().encode('base64')))
cursor.execute("insert into dbo.test(image_new)  SELECT BulkColumn FROM Openrowset( Bulk N'D:\\data\\local\\coco\\images\\val2014\\COCO_val2014_000000000042.jpg', Single_Blob) as img")
cursor.execute("SELECT * from dbo.test")
# cursor.execute("SELECT TOP 20 pc.Name as CategoryName, p.name as ProductName FROM [SalesLT].[ProductCategory] pc JOIN [SalesLT].[Product] p ON pc.productcategoryid = p.productcategoryid")

row = cursor.fetchone()
while row:
    print (str(row[0]) + " " + str(row[-1]))
    row = cursor.fetchone()

cnxn.commit()


