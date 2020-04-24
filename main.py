"""
Tutorial: https://repl.it/talk/learn/How-to-create-an-SQLite3-database-in-Python-3/15755
"""
from modules.pysqllite import PySQLLite
from pprint import pprint


while True:
    # Connect to a database
    my_db = PySQLLite("database/WSU_AL.db")

    statement = input("Please enter a statement: ")
    my_db.execute(statement)

    # Fetch the data
    my_db.execute(statement)

    # Pretty print the fetched data
    pprint(my_db.fetchall())

    # Remember to save + close
    my_db.exit()
