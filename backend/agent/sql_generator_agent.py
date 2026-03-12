from backend.ai.sql_generator import generate_sql

class SQLGeneratorAgent:
    def generate(self, question: str, dataset: str) -> str:
        """
        Converts a natural language question into a SQL query.
        """
        sql_query = generate_sql(question, dataset)
        return sql_query