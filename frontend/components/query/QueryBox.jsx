import { useState } from "react";
import { runQuery } from "../../services/queryService";
import EchartsRenderer from "../charts/EchartsRenderer";

export default function QueryBox() {

  const [question, setQuestion] = useState("");
  const [chart, setChart] = useState(null);
  const [insight, setInsight] = useState("");

  async function handleQuery() {

    const result = await runQuery(question, "sales");

    setChart(result.chart);
    setInsight(result.insight);
  }

  return (

    <div>

      <input
        value={question}
        onChange={(e)=>setQuestion(e.target.value)}
        placeholder="Ask a question about your data..."
      />

      <button onClick={handleQuery}>
        Run Query
      </button>

      {chart && <EchartsRenderer option={chart}/>}

      {insight && (
        <div className="insight-box">
          {insight}
        </div>
      )}

    </div>

  );
}