"""
Tutorial: https://repl.it/talk/learn/How-to-create-an-SQLite3-database-in-Python-3/15755
"""
from modules.pysqllite import PySQLLite
from pprint import pprint

# Connect to a database, otherwise create it
# This command is idempotent
my_db = PySQLLite("database/WSU_AL.db")

# Remember to save + close
my_db.exit()
