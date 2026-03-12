import React from "react";
import ReactECharts from "@echarts-for-react/core";

const EChartsRenderer = ({ chartConfig }) => {
    if (!chartConfig || !chartConfig.data) {
        return <p>No chart data available.</p>;
    }

    const chartOptions = {
        xAxis: { type: chartConfig.xAxis.type, data: chartConfig.data.map(row => row[0]) },
        yAxis: { type: chartConfig.yAxis.type },
        series: [{ type: chartConfig.type, data: chartConfig.data.map(row => row[1]) }]
    };

    return <ReactECharts option={chartOptions} style={{ height: "400px", width: "100%" }} />;
};

export default EChartsRenderer;