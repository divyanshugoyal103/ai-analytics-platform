from fastapi import APIRouter, HTTPException
from backend.ai.orchestrator import handle_nl_query
from backend.services.sql_service import execute_sql

router = APIRouter()

@router.post("/ask")
async def ask_question(question: str, dataset: str):
    """
    Accepts a user question and the target dataset.
    Returns query results or an error if any step fails.
    """
    try:
        # Generate SQL query from NL input
        sql_query = handle_nl_query(question, dataset)

        # If SQL generation fails
        if not sql_query:
            raise HTTPException(status_code=400, detail="Could not generate a SQL query.")

        # Execute the SQL query in DuckDB
        result = execute_sql(sql_query, dataset)

        return {
            "message": "Query executed successfully.",
            "query": sql_query,
            "results": result
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))