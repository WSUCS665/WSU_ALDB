from unittest import TestCase
from modules.pysqllite import PySQLLite


class TestPySQLLite(TestCase):
    """
    TDD unittest file for the PySQLLite module
    """
    def test_db_connection(self):
        """
        Test the PySQLLite module will connect
        to a database
        """
        test_db = PySQLLite("database/WSU_AL.db")
        self.assertEqual(test_db.conn.total_changes, 0)

    def test_db_exit_connection(self):
        """
        Test the PySQLLite module will exit
        a database connection
        """
        test_db = PySQLLite("database/WSU_AL.db")
        self.assertEqual(test_db.conn.total_changes, 0)

        # save + close
        test_db.exit()

        with self.assertRaises(Exception) as e:
            test_db.conn.in_transaction

        exception_message = e.exception.args[0]

        self.assertEqual(
            exception_message,
            'Cannot operate on a closed database.'
        )

    def test_db_make_entry(self):
        """
        Test to ensure the PySQLLite module
        will add an entry to a database table
        """
        test_db = PySQLLite("database/WSU_AL.db")

        try:
            # Insert data into our demo table
            # This commands is NOT idempotent
            test_db.execute("""
                INSERT INTO DemoTable VALUES (
                    1, "Our first DemoTable record entry"
                );
            """)
        except Exception as e:
            if 'UNIQUE constraint failed' not in e.args[0]:
                raise e

        # Fetch the data
        test_db.execute("""
            SELECT * FROM DemoTable
            WHERE id = 1
        """)

        # Pretty print the fetched data
        self.assertEqual(
            test_db.fetchall(),
            [(1, 'Our first DemoTable record entry')]
        )

    def test_db_read_entry(self):
        """
        Test to ensure the PySQLLite module
        can read an entry from a database table
        """
        test_db = PySQLLite("database/WSU_AL.db")

        # Fetch the data
        test_db.execute("""
            SELECT * FROM DemoTable
            WHERE id = 1
        """)

        self.assertEqual(
            test_db.fetchall(),
            [(1, 'Our first DemoTable record entry')]
        )

    def test_db_with_statement(self):
        """
        Test to ensure the PySQLLite module
        will __enter__ and __exit__ when
        used in a with statement
        """
        test_db = PySQLLite("database/WSU_AL.db")

        with test_db:
            # Fetch the data
            test_db.execute("""
                SELECT * FROM DemoTable
                WHERE id = 1
            """)

            self.assertEqual(
                test_db.fetchall(),
                [(1, 'Our first DemoTable record entry')]
            )

    def test_db_delete_entry(self):
        """
        Test to ensure the PySQLLite module
        can delete an entry from a database table
        """
        test_db = PySQLLite("database/WSU_AL.db")

        # Insert data into our demo table
        # This commands is NOT idempotent
        test_db.execute("""
            INSERT INTO DemoTable VALUES (
                2, "Our second DemoTable record entry"
            );
        """)

        # query to check the record
        test_db.execute("""
            SELECT * FROM DemoTable
            WHERE id = 2
        """)

        # ensur the record exists before we delete it
        self.assertEqual(
            test_db.fetchall(),
            [(2, 'Our second DemoTable record entry')]
        )

        # delete the record
        test_db.execute("""
            DELETE FROM DemoTable
            WHERE id = 2
        """)

        # query to check the record
        test_db.execute("""
            SELECT * FROM DemoTable
            WHERE id = 2
        """)

        # ensure the record does not exist
        self.assertEqual(
            test_db.fetchall(),
            []
        )
