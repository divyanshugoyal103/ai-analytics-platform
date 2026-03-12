import duckdb
import os

DB_FILE_PATH = "./datasets/analytics.db"

def execute_sql(query: str, dataset: str):
    """
    Executes a validated SQL query on the corresponding dataset.
    """
    # Verify the dataset exists
    dataset_path = f"./datasets/{dataset}.parquet"
    if not os.path.exists(dataset_path):
        raise ValueError(f"Dataset '{dataset}' not found.")

    # Connect to DuckDB
    conn = duckdb.connect(database=DB_FILE_PATH)

    # Link the dataset to DuckDB
    conn.execute(f"CREATE OR REPLACE TABLE {dataset} AS SELECT * FROM '{dataset_path}'")

    # Execute query
    result = conn.sql(query).fetchall()

    return result