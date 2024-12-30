import sqlite3
class Database:
    def __init__(self, db_path ):
        self.db_path = db_path
    
    def connect(self):
        return sqlite3.connect(self.db_path)
    
    def add_plant(self, plant):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO plants(specie,date_aquired,description) VALUES(?,?,?)",(plant.specie,plant.date_aquired,plant.description))
        conn.commit()
        conn.close()

    def delete_plant(self, plant):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM plants WHERE name = ?",(plant.name,))
        conn.commit()
        conn.close()

    def get_plants(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM plants")


    