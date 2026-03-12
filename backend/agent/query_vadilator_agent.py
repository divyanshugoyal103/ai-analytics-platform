import duckdb

class QueryValidatorAgent:
    def validate(self, sql_query: str) -> bool:
        """
        Validates a SQL query using syntax checking.
        """
        try:
            # Attempt to parse the query in DuckDB (syntax check)
            duckdb.sql(sql_query)
            return True
        except Exception as e:
            print(f"Query validation error: {e}")
            return False