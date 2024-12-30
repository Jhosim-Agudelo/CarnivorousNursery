import sqlite3
class Database:
    def __init__(self, db_path ):
        self.db_path = db_path
    
    def connect(self):
        return sqlite3.connect(self.db_path)
    
    def add_plant(self, plant):
        conn = self.connect()
        cursor = conn.cursor()

        if self.check_name(plant.name):
            cursor.execute(
                "INSERT INTO plants(specie,date_aquired,description) "+\
                "VALUES(?,?,?)"
                ,(plant.specie,plant.date_aquired,plant.description))
            conn.commit()
        else:
            print("The plant name is already in use")
        conn.close()

    def delete_plant(self, name):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM plants WHERE name = ?",(name,))
        conn.commit()
        conn.close()

    def get_plants(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM plants")


    def get_plant(self, name):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM plants WHERE name = ?",(name,))
        return cursor.fetchone()
    
    def update_plant(self, plant):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE plants SET specie = ?, date_aquired = ?, description = ? "+\
                "WHERE name = ?"
            ,(plant.specie,plant.date_aquired,plant.description,plant.name))
        conn.commit()
        conn.close()

    def check_name(self, name):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM plants WHERE name = ?",(name,))
        return cursor.fetchone() is not None