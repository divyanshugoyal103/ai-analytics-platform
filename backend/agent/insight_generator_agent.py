class InsightGeneratorAgent:
    def generate(self, results, question: str):
        """
        Produces human-readable insights from the query results.
        """
        # Simplistic example: Summarizing row data
        if results:
            total_rows = len(results)
            first_row = results[0]
            insight = (
                f"The query returned {total_rows} rows. "
                f"The first record includes: {first_row}."
            )
        else:
            insight = "No data available for the given query."

        return insight