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
        try:
            connection.execute('''INSERT INTO user
                            VALUES (?,?)''', (username, password))
        
            connection.commit()
            connection.close()
            return True

        except Exception as e:
            print(e)
            connection.close()
            return False
        

    
    def authenticate(self, username, password):
        connection = sql.connect(self.name)
        connection.cursor.execute("""SELECT username FROM user WHERE username = ? AND password = ?;""",(username, password))

        result = connection.cursor.fetchone()

        connection.close()

        if result is not None:
            return True

        else:
            return False
