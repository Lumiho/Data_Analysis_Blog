import React from 'react';
import { StaticGraph, InteractiveGraph } from '@/components/DataVisualization';

export default function ExampleDataAnalysis() {
  return (
    <div className="max-w-4xl mx-auto p-6">
      <h1 className="text-3xl font-bold mb-6">Data Analysis Results</h1>
      
      <section className="mb-8">
        <h2 className="text-2xl font-semibold mb-4">Static Visualization</h2>
        <StaticGraph
          src="/graphs/my_plot.png"
          alt="Data analysis visualization"
          width={800}
          height={600}
        />
      </section>

      <section className="mb-8">
        <h2 className="text-2xl font-semibold mb-4">Interactive Visualization</h2>
        <InteractiveGraph
          src="/graphs/interactive_plot.html"
          height="600px"
        />
      </section>
    </div>
  );
} 