"""
Tutorial: https://repl.it/talk/learn/How-to-create-an-SQLite3-database-in-Python-3/15755
"""
from modules.pysqllite import PySQLLite
from pprint import pprint

# Connect to a database, otherwise create it
# This command is idempotent
my_db = PySQLLite("database/WSU_AL.db")

try:
    # Create the table, this command is NOT idempotent
    # https://www.w3schools.com/sql/sql_datatypes.asp
    my_db.execute(
    """CREATE TABLE DemoTable (
        id INTEGER PRIMARY KEY,
        description VARCHAR(5)
        );
    """
    )
except Exception as e:
    if e.args[0] != 'table DemoTable already exists':
        raise e

# # Insert data into our demo table
# # This commands is idempotent
my_db.execute(
  """
    INSERT INTO DemoTable VALUES (
      1, "Our first DemoTable record entry"
    );
  """
)

# Fetch the data 
my_db.execute("SELECT * FROM DemoTable")

# Pretty print the fetched data
pprint(my_db.fetchall())

# Remember to save + close
my_db.exit()
