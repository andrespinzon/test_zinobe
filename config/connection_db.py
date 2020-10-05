import sqlite3


class ConnectionDb:

    @staticmethod
    def connect():
        try:
            con = sqlite3.connect('test.sqlite')
            return con
        except ValueError as e:
            print(e)

    @staticmethod
    def create_if_not_exist_table(con):
        cursor = con.cursor()
        cursor.execute(
            '''
                CREATE TABLE IF NOT EXISTS country (
                    id integer PRIMARY KEY, 
                    region text, 
                    country text, 
                    language text, 
                    time real
                )
            '''
        )
        con.commit()
