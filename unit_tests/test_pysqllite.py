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
