import sqlite3
class DrinksApp:
    def __init__(self,db_name = "I_love_drink.db" ):
        self.db_name = db_name
        self.con = sqlite3.connect(self.db_name)
        self.cursor = self.con.cursor()
        self.create_tables()
    def create_tables(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS alcohol
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            alcohol_content REAL NOT NULL,
                            volume INTEGER NOT NULL,
                            price REAL NOT NULL,
                            stock INTEGER DEFAULT 0
                            )
                        """)
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS ingredients 
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            description TEXT,
                            price REAL NOT NULL,
                            stock INTEGER DEFAULT 0
                            )
                        """)
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS cocktails 
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            description TEXT,
                            strength REAL,
                            price REAL NOT NULL
                            )
                        """)
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS cocktail_ingredients 
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            cocktail_id INTEGER NOT NULL,
                            ingredient_id INTEGER, 
                            alcohol_id INTEGER, 
                            quantity REAL NOT NULL,
                            FOREIGN KEY (cocktail_id) REFERENCES cocktails (id),
                            FOREIGN KEY (ingredient_id) REFERENCES ingredients (id),
                            FOREIGN KEY (alcohol_id) REFERENCES alcohol (id),
                            CHECK ( (ingredient_id IS NULL AND alcohol_id IS NOT NULL) OR (ingredient_id IS NOT NULL AND alcohol_id IS NULL) )
                            )
                        """)
        self.con.commit()
