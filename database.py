import sqlite3 as sql

class DatabaseHandler:
    def __init__(self,databaseName):
        self.name = databaseName


    def createTables(self):
        connection = sql.connect(self.name)

        connection.execute('''CREATE TABLE IF NOT EXISTS user
                           (
                            username text primary key,
                            password text not null
                           );''')
        
        connection.close()

    def createUser(self,username,password):
        connection = sql.connect(self.name)

        connection.execute('''INSERT INTO user
                            VALUES (?,?)''', (username, password))
        
        connection.commit()
        
        connection.close()