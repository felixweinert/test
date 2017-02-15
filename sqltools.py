from settings import connection_properties
from datenbanken import *
import pymysql
import sys

"""class DB:
    conn = None

    def connect(self):
        self.conn = pymysql.connect(**connection_properties)
        return self.conn

    def query(self, sql):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            self.conn.commit()
        except (AttributeError, pymysql.err.OperationalError):
            print("FAILED TO SEND QUERY - RECONNECT")
            self.connect()
            cursor = self.conn.cursor()
            cursor.execute(sql)
            self.conn.commit()
        return cursor

    def close(self):
        self.conn.close()"""

class DatenbankTools:
    def __init__(self):
        self.konfi = "**connection_properties"
        self.dbname = "test1"
        self.zeich = "utf8"
        self.sort = "utf8_general_ci"
        self.DB = DB()
    def anlegen(self):

        self.DB.query("SHOW DATABASE;")
        self.DB.query("DROP DATABASE IF EXISTS ", self.dbname, ";")
        self.DB.query("CREATE DATABASE ", self.dbname, ";")

    def löschen(self):
        self.DB.query("DROP DATABASE IF EXISTS ", self.dbname, ";")

    def überschreiben(self):
        self.DB.query("SHOW DATABASE;")
        self.DB.query("DROP DATABASE IF EXISTS ", self.dbname, ";")
        self.DB.query("CREATE DATABASE ", self.dbname, ";")

if __name__ == "__main__":
    DB = DB()
    DB.connect()
    DBTools = DatenbankTools()
    DBTools.anlegen()
    DB.close()

