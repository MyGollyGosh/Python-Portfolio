import os
import sqlite3
import unittest
import pandas as pd
from Financial_data import pull_data, save_to_csv, convert_to_sql, execute_query

class TestFinancialData(unittest.TestCase):

    def setUp(self):
        self.output_directory = 'test_data'
        if not os.path.exists(self.output_directory):
            os.makedirs(self.output_directory)
        self.csv_file_path = os.path.join(self.output_directory, 'historical_data.csv')
        self.db_file_path = 'historical_data.db'

    def tearDown(self):
        if os.path.exists(self.csv_file_path):
            os.remove(self.csv_file_path)
        if os.path.exists(self.db_file_path):
            os.remove(self.db_file_path)
        if os.path.exists(self.output_directory):
            os.rmdir(self.output_directory)
    
    def test_pull_data(self):
        data = pull_data()
        self.assertIsInstance(data, pd.DataFrame)
        self.assertTrue(len(data) > 0)
    
    def test_save_to_csv(self):
        save_to_csv(self.output_directory)
        self.assertTrue(os.path.exists(self.csv_file_path))
    
    def test_convert_to_sql(self):
        save_to_csv(self.output_directory)
        convert_to_sql(self.csv_file_path)
        self.assertTrue(os.path.exists(self.db_file_path))
        
        # Check if data is inserted correctly
        connection = sqlite3.connect(self.db_file_path)
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM historical_data")
        count = cursor.fetchone()[0]
        connection.close()
        self.assertTrue(count > 0)
    
    def test_execute_query(self):
        save_to_csv(self.output_directory)
        convert_to_sql(self.csv_file_path)
        
        # Test query execution
        query = "SELECT COUNT(*) FROM historical_data"
        connection = sqlite3.connect(self.db_file_path)
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        connection.close()
        self.assertTrue(len(result) > 0)
        self.assertTrue(isinstance(result[0][0], int))

if __name__ == '__main__':
    unittest.main()
