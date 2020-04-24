"""
File: db_setup.py
Date: 4.24.2020
Author: Kyle Lanier

Porpose:
This file is used to setup the WSU Applied Learning
database from scratch in the event the database needs
to be recreated.

All methods are designed to be idempotent
"""
import datetime
import os
import sys
import pathlib  # noqa: F401
from pathlib import Path  # for relative path discovery

# change sys.path
# this allows us to import modules up one directory
file = Path(__file__).resolve()
parent, top = file.parent, file.parents[1]
sys.path.append(os.path.join(top, ''))

from modules.pysqllite import PySQLLite  # noqa: E402



def create_locations_table(wsual_db):
    try:
        wsual_db.execute("""
            CREATE TABLE Locations (
                locationId VARCHAR(50) PRIMARY KEY,
                street VARCHAR(50),
                city VARCHAR(50),
                state VARCHAR(50),
                zipcode VARCHAR(10)
            );
        """)
    except Exception as e:
        if 'table Locations already exists' not in e.args[0]:
            raise e

def create_companies_table(wsual_db):
    try:
        wsual_db.execute("""
            CREATE TABLE Companies (
                companyName VARCHAR(50) PRIMARY KEY
            );
        """)
    except Exception as e:
        if 'table Companies already exists' not in e.args[0]:
            raise e

def create_contracts_table(wsual_db):
    try:
        wsual_db.execute("""
            CREATE TABLE Contracts (
                contractId VARCHAR(50) PRIMARY KEY,
                startDate TEXT,
                endDate TEXT,
                companyManager VARCHAR(50),
                studentWage REAL,
                cost REAL
            );
        """)
    except Exception as e:
        if 'table Contracts already exists' not in e.args[0]:
            raise e

def create_projects_table(wsual_db):
    try:
        wsual_db.execute("""
            CREATE TABLE Projects (
                projectId VARCHAR(50) PRIMARY KEY,
                type VARCHAR(50),
                numStudents INTEGER,
                isRemote BOOL
            );
        """)
    except Exception as e:
        if 'table Projects already exists' not in e.args[0]:
            raise e

def create_skills_table(wsual_db):
    try:
        wsual_db.execute("""
            CREATE TABLE Skills (
                skillName VARCHAR(50) PRIMARY KEY,
                description VARCHAR(50),
                skillLevel VARCHAR(30)
            );
        """)
    except Exception as e:
        if 'table Skills already exists' not in e.args[0]:
            raise e

def create_skillsets_table(wsual_db):
    try:
        wsual_db.execute("""
            CREATE TABLE SkillSets (
                skillSetId VARCHAR(10) PRIMARY KEY
            );
        """)
    except Exception as e:
        if 'table SkillSets already exists' not in e.args[0]:
            raise e

def create_students_table(wsual_db):
    try:
        wsual_db.execute("""
            CREATE TABLE Students (
                studentId VARCHAR(10) PRIMARY KEY,
                studentName VARCHAR(50),
                major VARCHAR(50),
                tenure VARCHAR(20),
                graduationDate TEXT
            );
        """)
    except Exception as e:
        if 'table Students already exists' not in e.args[0]:
            raise e

def create_tables(wsual_db):
    """
    Create all database tables
    """
    create_students_table(wsual_db)
    create_skillsets_table(wsual_db)
    create_skills_table(wsual_db)
    create_projects_table(wsual_db)
    create_contracts_table(wsual_db)
    create_companies_table(wsual_db)

def setup_db():
    """
    Recreate the database tables, relations, and records
    return the created database for unittest validation
    """
    wsual_db = PySQLLite("database/WSU_AL.db")
    create_tables(wsual_db)

    return wsual_db

# class TestPySQLLite(TestCase):
#     """
#     TDD unittest file for the PySQLLite module
#     """
#     def test_db_connection(self):
#         """
#         Test the PySQLLite module will connect
#         to a database
#         """
#         test_db = PySQLLite("database/WSU_AL.db")
#         self.assertEqual(test_db.conn.total_changes, 0)

#     def test_db_exit_connection(self):
#         """
#         Test the PySQLLite module will exit
#         a database connection
#         """
#         test_db = PySQLLite("database/WSU_AL.db")
#         self.assertEqual(test_db.conn.total_changes, 0)

#         # save + close
#         test_db.exit()

#         with self.assertRaises(Exception) as e:
#             test_db.conn.in_transaction

#         exception_message = e.exception.args[0]

#         self.assertEqual(
#             exception_message,
#             'Cannot operate on a closed database.'
#         )

#     def test_db_make_entry(self):
#         """
#         Test to ensure the PySQLLite module
#         will add an entry to a database table
#         """
#         test_db = PySQLLite("database/WSU_AL.db")

#         try:
#             # Insert data into our demo table
#             # This commands is NOT idempotent
#             test_db.execute("""
#                 INSERT INTO DemoTable VALUES (
#                     1, "Our first DemoTable record entry"
#                 );
#             """)
#         except Exception as e:
#             if 'UNIQUE constraint failed' not in e.args[0]:
#                 raise e

#         # Fetch the data
#         test_db.execute("""
#             SELECT * FROM DemoTable
#             WHERE id = 1
#         """)

#         # Pretty print the fetched data
#         self.assertEqual(
#             test_db.fetchall(),
#             [(1, 'Our first DemoTable record entry')]
#         )

#     def test_db_read_entry(self):
#         """
#         Test to ensure the PySQLLite module
#         can read an entry from a database table
#         """
#         test_db = PySQLLite("database/WSU_AL.db")

#         # Fetch the data
#         test_db.execute("""
#             SELECT * FROM DemoTable
#             WHERE id = 1
#         """)

#         self.assertEqual(
#             test_db.fetchall(),
#             [(1, 'Our first DemoTable record entry')]
#         )

#     def test_db_with_statement(self):
#         """
#         Test to ensure the PySQLLite module
#         will __enter__ and __exit__ when
#         used in a with statement
#         """
#         test_db = PySQLLite("database/WSU_AL.db")

#         with test_db:
#             # Fetch the data
#             test_db.execute("""
#                 SELECT * FROM DemoTable
#                 WHERE id = 1
#             """)

#             self.assertEqual(
#                 test_db.fetchall(),
#                 [(1, 'Our first DemoTable record entry')]
#             )

#     def test_db_delete_entry(self):
#         """
#         Test to ensure the PySQLLite module
#         can delete an entry from a database table
#         """
#         test_db = PySQLLite("database/WSU_AL.db")

#         # Insert data into our demo table
#         # This commands is NOT idempotent
#         test_db.execute("""
#             INSERT INTO DemoTable VALUES (
#                 2, "Our second DemoTable record entry"
#             );
#         """)

#         # query to check the record
#         test_db.execute("""
#             SELECT * FROM DemoTable
#             WHERE id = 2
#         """)

#         # ensur the record exists before we delete it
#         self.assertEqual(
#             test_db.fetchall(),
#             [(2, 'Our second DemoTable record entry')]
#         )

#         # delete the record
#         test_db.execute("""
#             DELETE FROM DemoTable
#             WHERE id = 2
#         """)

#         # query to check the record
#         test_db.execute("""
#             SELECT * FROM DemoTable
#             WHERE id = 2
#         """)

#         # ensure the record does not exist
#         self.assertEqual(
#             test_db.fetchall(),
#             []
#         )
