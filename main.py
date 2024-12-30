from models.database import Database
from models.plant import Plant
import sys
def create_tables_if_needed(db):
    db.execute_query(
        '''
        CREATE TABLE IF NOT EXISTS plants (
            plant_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            specie TEXT NOT NULL,
            date_acquired DATE NOT NULL,
            description TEXT
        );
        '''
    )

def pretty_print_plant(plant):
    print(f"Name: {plant[1]}")
    print(f"Specie: {plant[2]}")
    print(f"Date acquired: {plant[3]}")
    print(f"Description: {plant[4]}")

def main():
    db = Database("data/plants.db")
    create_tables_if_needed(db)
    print("Welcome to the plant app! (MVP)")
    print("""Commands available: 
                ADD <name> <specie> <date> <description>
                DELETE <name>
                LIST
                EXIT""")

    for line in sys.stdin:
        command = line.strip().split()

        if not command:
            continue

        if command[0] == 'EXIT':
            break
        elif command[0] == 'ADD':
            plant = Plant(command[1],command[2],command[3],command[4])
            db.add_plant(plant)
        elif command[0] == 'DELETE':
            db.delete_plant(command[1])
        elif command[0] == 'LIST':
            plants = db.get_plants()
            for plant in plants:
                pretty_print_plant(plant)

if __name__ == "__main__":
    main()