from backend.ai.agents.sql_generator_agent import SQLGeneratorAgent
from backend.ai.agents.visualization_agent import VisualizationAgent
from backend.ai.agents.insight_generator_agent import InsightGeneratorAgent

class PlannerAgent:
    def __init__(self):
        self.sql_agent = SQLGeneratorAgent()
        self.visualization_agent = VisualizationAgent()
        self.insight_agent = InsightGeneratorAgent()

    def process_query(self, question: str, dataset: str):
        """
        Splits the user question into subtasks and coordinates agents.
        """
        # Step 1: Generate SQL query
        sql_query = self.sql_agent.generate(question, dataset)

        # Step 2: Execute query and fetch data
        # This can be delegated to an additional service layer
        from backend.services.sql_service import execute_sql
        results = execute_sql(sql_query, dataset)

        # Step 3: Generate visualizations
        chart_config = self.visualization_agent.create_visualization(results, question)

        # Step 4: Generate analytical insights
        insights = self.insight_agent.generate(results, question)

        # Return results
        return {
            "query": sql_query,
            "results": results,
            "visualization": chart_config,
            "insights": insights,
        }