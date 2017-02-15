from datenbanken import *
if __name__ == "__main__":
    DB.connect()
    dbquery = DB.query("select * from test;")
    DB.close()