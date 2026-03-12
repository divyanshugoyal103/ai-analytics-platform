class VisualizationAgent:
    def create_visualization(self, results, question: str):
        """
        Generates chart configuration JSON based on the query results.
        """
        # Example logic for chart type
        if len(results[0]) == 2:
            chart_type = "bar"
        else:
            chart_type = "line"

        # Generate a simple ECharts configuration
        chart_config = {
            "type": chart_type,
            "data": results,
            "xAxis": {"type": "category"},
            "yAxis": {"type": "value"},
        }

        return chart_config