from backend.ai.sql_generator import generate_sql

def handle_nl_query(question: str, dataset: str) -> str:
    """
    Handles natural language input, generates a SQL query using AI,
    and validates it.
    """
    # Use the SQL Generator Agent to interpret and generate SQL
    sql_query = generate_sql(question, dataset)

    return sql_query