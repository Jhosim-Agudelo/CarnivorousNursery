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
    print()
    print(f"Name: {plant[1]}")
    print(f"Specie: {plant[2]}")
    print(f"Date acquired: {plant[3]}")
    print(f"Description: {plant[4]}")
    print()
    
def main():
    db = Database("data/plants.db")
    create_tables_if_needed(db)
    print("\nWelcome to the carnivorous Nursery! (MVP)")
    print("\nCommands available: "
          ,"\nADD <name> <specie> <date> <description>"
          ,"\nDELETE <name>"
          ,"\nLIST"
          ,"\nEXIT\n")

    for line in sys.stdin:
        parts = line.strip().split(maxsplit=4)
        cmd = parts[0].upper()

        if not cmd:
            continue

        if cmd == 'EXIT':
            break
        elif cmd == 'ADD':
            plant = Plant(parts[1],parts[2],parts[3],parts[4])
            db.add_plant(plant)
        elif cmd == 'DELETE':
            db.delete_plant(parts[1])
        elif cmd == 'LIST':
            plants = db.get_plants()
            for plant in plants:
                pretty_print_plant(plant)
        else:
            print("Invalid command")

if __name__ == "__main__":
    main()