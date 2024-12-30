import sqlite3
class Database:
    def __init__(self, db_path ):
        self.db_path = db_path
    
    def connect(self):
        return sqlite3.connect(self.db_path)

    def execute_query(self, query):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        conn.close()
    
    def add_plant(self, plant):
        """
        Adds a plant to the database
        """
        conn = self.connect()
        cursor = conn.cursor()
        name_without_spaces = plant.name.strip()
        if self.check_name(name_without_spaces):
            cursor.execute(
                "INSERT INTO plants(name,specie,date_acquired,description) "+\
                "VALUES(?,?,?,?)"
                ,(name_without_spaces,
                  plant.specie,
                  plant.date_aquired,
                  plant.description))
            conn.commit()
        else:
            print("The plant name is already in use")
        conn.close()

    def delete_plant(self, name):
        """
        Deletes a plant from the database
        """
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM plants WHERE name = ?",(name,))
        conn.commit()
        conn.close()

    def get_plants(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM plants")
        return cursor.fetchall()


    def get_plant(self, name):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM plants WHERE name = ?",(name,))
        return cursor.fetchone()
    
    def update_plant(self, plant):
        """
        Updates a plant in the database
        """
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE plants SET specie = ?, date_acquired = ?, description = ? "+\
                "WHERE name = ?"
            ,(plant.specie,plant.date_aquired,plant.description,plant.name))
        conn.commit()
        conn.close()

    def check_name(self, name):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM plants WHERE name = ?",(name.upper(),))
        return cursor.fetchone() is None