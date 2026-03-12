import duckdb
import os

DB_PATH = "datasets/analytics.db"

class DuckDBManager:

    def __init__(self):
        self.conn = duckdb.connect(DB_PATH)

    def execute(self, sql):
        return self.conn.execute(sql).fetchall()

    def execute_df(self, sql):
        return self.conn.execute(sql).df()

    def register_parquet(self, table_name, path):

        self.conn.execute(f"""
        CREATE OR REPLACE TABLE {table_name} AS
        SELECT * FROM read_parquet('{path}')
        """)