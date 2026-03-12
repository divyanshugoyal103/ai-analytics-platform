import React, { useState } from 'react';
import EChartsRenderer from '../components/EChartsRenderer';
import axios from 'axios';

export default function Dashboard() {
    const [query, setQuery] = useState('');
    const [dataset, setDataset] = useState('');
    const [results, setResults] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const handleQuery = async () => {
        setLoading(true);
        setError(null);
        try {
            const response = await axios.post('http://127.0.0.1:8000/api/query/ask', {
                question: query,
                dataset: dataset,
            });

            setResults(response.data);
        } catch (err) {
            setError('An error occurred: ' + err.message);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="container mx-auto p-4">
            <h1 className="text-2xl font-bold mb-4">AI Analytics Dashboard</h1>

            <div className="mb-4">
                <input
                    type="text"
                    placeholder="Enter your question"
                    value={query}
                    onChange={(e) => setQuery(e.target.value)}
                    className="border rounded px-4 py-2 mr-2"
                />
                <input
                    type="text"
                    placeholder="Dataset name"
                    value={dataset}
                    onChange={(e) => setDataset(e.target.value)}
                    className="border rounded px-4 py-2 mr-2"
                />
                <button
                    onClick={handleQuery}
                    className="bg-blue-500 text-white px-4 py-2 rounded"
                >
                    Run Query
                </button>
            </div>

            {loading && <p>Loading...</p>}
            {error && <p className="text-red-500">{error}</p>}

            {results && (
                <div>
                    <h2 className="text-xl font-semibold mb-2">Query Results</h2>
                    <p className="mb-4">SQL Query: {results.query}</p>

                    {/* Render ECharts Visualization */}
                    <EChartsRenderer chartConfig={results.visualization} />

                    <h3 className="text-lg font-medium mt-4">Insights</h3>
                    <p>{results.insights}</p>
                </div>
            )}
        </div>
    );
}