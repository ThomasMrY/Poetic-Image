import pyodbc
import time


class DBIO(object):
    def __init__(self,
                 server='poetic-image.database.windows.net',
                 database='poetic_image',
                 username='administor',
                 password='PoeticImage.abc',
                 driver='{ODBC Driver 13 for SQL Server}'):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.driver = driver
        self.connect()

    def connect(self):
        self.cnxn = pyodbc.connect(
            'DRIVER=' + self.driver + ';SERVER=' + self.server + ';PORT=1433;DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
        self.cursor = self.cnxn.cursor()

    def close(self):
        self.cnxn.close()

    def submit(self, id, poetry, score, tags, comments):
        datetime = time.strftime('%Y-%m-%d %H:%M:%S')
        self.insert('Main', [id, poetry, score, datetime])
        for tag in tags:
            self.insert('Image_Tag', [id, tag])
        for comment in comments:
            self.insert('Image_Comment', [id, comment])

    def insert(self, table, row):
        self.cursor.execute("select COUNT(*) FROM INFORMATION_SCHEMA.COLUMNS WHERE table_catalog = ? AND table_name = ?", [self.database, table])
        num_columns = self.cursor.fetchone()[0]
        assert num_columns == len(row), 'length of inserted item must equal column of table'
        value_insert_format = "insert into dbo.{} VALUES ".format(table) + '(' + ','.join(['?' for _ in range(num_columns)]) + ')'
        self.cursor.execute(value_insert_format, list(row))
        self.cnxn.commit()

