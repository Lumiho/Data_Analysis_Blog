import React from 'react';
import { StaticGraph, InteractiveGraph } from '@/components/DataVisualization';

export default function PythonAnalysis() {
  return (
    <div className="max-w-4xl mx-auto p-6">
      <h1 className="text-3xl font-bold mb-6">Python Data Analysis Results</h1>
      
      <section className="mb-12">
        <h2 className="text-2xl font-semibold mb-4">Time Series Analysis</h2>
        <p className="mb-4">
          This visualization shows the trend of our time series data over time.
        </p>
        <StaticGraph
          src="/graphs/time_series.png"
          alt="Time series analysis visualization"
          width={800}
          height={400}
        />
      </section>

      <section className="mb-12">
        <h2 className="text-2xl font-semibold mb-4">Category Distribution</h2>
        <p className="mb-4">
          A box plot showing the distribution of values across different categories.
        </p>
        <StaticGraph
          src="/graphs/boxplot.png"
          alt="Box plot of value distributions"
          width={800}
          height={400}
        />
      </section>

      <section className="mb-12">
        <h2 className="text-2xl font-semibold mb-4">Interactive Time Series</h2>
        <p className="mb-4">
          An interactive scatter plot that allows you to explore the relationship between time and values,
          colored by category. You can hover over points, zoom, and pan the visualization.
        </p>
        <InteractiveGraph
          src="/graphs/interactive_scatter.html"
          height="600px"
        />
      </section>
    </div>
  );
} 