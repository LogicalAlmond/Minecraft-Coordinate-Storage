import mysql.connector as sql
from secrets import creds
from datetime import datetime

class DbSetup:
    
    def __init__(self):
        self.db = sql.connect(
            host=creds.get('host'),
            user=creds.get('user'),
            password=creds.get('pass'),
            database=creds.get('database'),
        )
        self.cursor = self.db.cursor(prepared=True)
        print('Connection to SQL database established...')
        
    def submitQuery(self, queryParameters):
        db = self.db
        cursor = self.cursor
        baseQuery = "INSERT INTO Coordinates (name, x, y, z, explored) VALUES (%s, %s, %s, %s, %s);"
        cursor.execute(baseQuery, queryParameters)
        db.commit()
        print('Query submitted...')
        
    # Helper function to reload data after submitQuery is triggered
    def _reloadData(self):
        print('Reloading data...')
        cursor = self.cursor
        query = 'SELECT * FROM Coordinates;'
        cursor.execute(query)
        data = cursor.fetchall()
        print('Reloaded successful')
        return data
        
    def queryAll(self):
        print('Querying data...')
        db = self.db
        cursor = self.cursor
        query = 'SELECT * FROM Coordinates;'
        start = datetime.now()
        cursor.execute(query)
        finish = datetime.now()
        exeTime = finish - start
        exeTimeSeconds = exeTime.total_seconds()
        data = cursor.fetchall()
        print(f'Data queried in {exeTimeSeconds} seconds')
        return data
