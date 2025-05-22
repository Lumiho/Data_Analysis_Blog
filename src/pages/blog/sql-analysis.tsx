import React from 'react';
import { StaticGraph, InteractiveGraph } from '@/components/DataVisualization';

export default function SQLAnalysis() {
  return (
    <div className="max-w-4xl mx-auto p-6">
      <h1 className="text-3xl font-bold mb-6">SQL Data Analysis Example</h1>
      
      <section className="mb-8">
        <h2 className="text-2xl font-semibold mb-4">Monthly Revenue Trends</h2>
        <p className="mb-4">
          Analysis of monthly revenue trends across different product categories using SQL aggregation.
          This visualization shows how each category performs over time.
        </p>
        <div className="mb-4 bg-gray-50 p-4 rounded-lg">
          <pre className="text-sm overflow-x-auto">
            {`SELECT 
    strftime('%Y-%m', date) as month,
    category,
    SUM(revenue) as total_revenue
FROM sales
GROUP BY month, category
ORDER BY month, category`}
          </pre>
        </div>
        <StaticGraph
          src="/graphs/monthly_revenue.png"
          alt="Monthly revenue by category"
          width={800}
          height={400}
        />
      </section>

      <section className="mb-8">
        <h2 className="text-2xl font-semibold mb-4">Product Performance Analysis</h2>
        <p className="mb-4">
          Interactive visualization showing the relationship between units sold and revenue for each product.
          The bubble size represents the average price, and colors indicate product categories.
        </p>
        <div className="mb-4 bg-gray-50 p-4 rounded-lg">
          <pre className="text-sm overflow-x-auto">
            {`SELECT 
    product_name,
    category,
    SUM(quantity) as total_units,
    SUM(revenue) as total_revenue,
    AVG(revenue/quantity) as avg_price
FROM sales
GROUP BY product_name, category
ORDER BY total_revenue DESC`}
          </pre>
        </div>
        <InteractiveGraph
          src="/graphs/product_performance.html"
          height="600px"
        />
      </section>

      <section className="mb-8">
        <h2 className="text-2xl font-semibold mb-4">Daily Sales Patterns</h2>
        <p className="mb-4">
          Analysis of the relationship between daily units sold and revenue,
          with a regression line showing the general trend.
        </p>
        <div className="mb-4 bg-gray-50 p-4 rounded-lg">
          <pre className="text-sm overflow-x-auto">
            {`SELECT 
    date,
    SUM(revenue) as daily_revenue,
    SUM(quantity) as daily_units
FROM sales
GROUP BY date
ORDER BY date`}
          </pre>
        </div>
        <StaticGraph
          src="/graphs/daily_patterns.png"
          alt="Daily sales patterns"
          width={800}
          height={400}
        />
      </section>
    </div>
  );
} 