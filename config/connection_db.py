import sqlite3
from config.variables import Variables
from pymongo import MongoClient


class ConnectionDb:

    @staticmethod
    def connect():
        try:
            if 'LOCAL' == Variables.get_env_deploy():
                conn = sqlite3.connect('test.sqlite')
            else:
                client = MongoClient(Variables.get_mongo_connection(), 27017)
                db = client['test']
                conn = db['country']
            return conn
        except ValueError as e:
            print(e)

    @staticmethod
    def create_if_not_exist_table(con):
        if 'LOCAL' == Variables.get_env_deploy():
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
