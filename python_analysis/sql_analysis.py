import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from datetime import datetime, timedelta

# Create a connection to a new SQLite database (or connect to existing one)
conn = sqlite3.connect('sales_data.db')
cursor = conn.cursor()

# Create a sales table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS sales (
        date DATE,
        product_name TEXT,
        category TEXT,
        quantity INTEGER,
        revenue FLOAT
    )
''')

# Generate some sample data
np.random.seed(42)
start_date = datetime(2024, 1, 1)
products = {
    'Laptop': 'Electronics',
    'Smartphone': 'Electronics',
    'Headphones': 'Electronics',
    'T-shirt': 'Clothing',
    'Jeans': 'Clothing',
    'Sneakers': 'Footwear'
}

# Generate and insert sample data
data_to_insert = []
for i in range(100):
    date = start_date + timedelta(days=i)
    for product, category in products.items():
        quantity = np.random.randint(1, 20)
        # Random base price between 50 and 500
        base_price = {'Electronics': (300, 1000),
                     'Clothing': (20, 100),
                     'Footwear': (50, 150)}[category]
        price = np.random.uniform(base_price[0], base_price[1])
        revenue = quantity * price
        data_to_insert.append((date, product, category, quantity, revenue))

# Insert the data
cursor.executemany('''
    INSERT INTO sales (date, product_name, category, quantity, revenue)
    VALUES (?, ?, ?, ?, ?)
''', data_to_insert)
conn.commit()

# Now let's analyze the data using SQL queries

# 1. Monthly revenue by category
monthly_revenue_query = '''
    SELECT 
        strftime('%Y-%m', date) as month,
        category,
        SUM(revenue) as total_revenue
    FROM sales
    GROUP BY month, category
    ORDER BY month, category
'''
monthly_df = pd.read_sql_query(monthly_revenue_query, conn)

# Create a static plot for monthly revenue
plt.figure(figsize=(12, 6))
for category in monthly_df['category'].unique():
    category_data = monthly_df[monthly_df['category'] == category]
    plt.plot(category_data['month'], category_data['total_revenue'], 
             marker='o', label=category)
plt.title('Monthly Revenue by Category')
plt.xlabel('Month')
plt.ylabel('Revenue ($)')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig('../public/graphs/monthly_revenue.png', dpi=300, bbox_inches='tight')
plt.close()

# 2. Product performance analysis
product_query = '''
    SELECT 
        product_name,
        category,
        SUM(quantity) as total_units,
        SUM(revenue) as total_revenue,
        AVG(revenue/quantity) as avg_price
    FROM sales
    GROUP BY product_name, category
    ORDER BY total_revenue DESC
'''
product_df = pd.read_sql_query(product_query, conn)

# Create an interactive bubble chart
fig = px.scatter(product_df, 
                 x='total_units', 
                 y='total_revenue',
                 size='avg_price',
                 color='category',
                 text='product_name',
                 title='Product Performance Analysis')
fig.update_traces(textposition='top center')
fig.update_layout(
    xaxis_title='Total Units Sold',
    yaxis_title='Total Revenue ($)',
    template='plotly_white'
)
fig.write_html('../public/graphs/product_performance.html')

# 3. Daily sales patterns
daily_query = '''
    SELECT 
        date,
        SUM(revenue) as daily_revenue,
        SUM(quantity) as daily_units
    FROM sales
    GROUP BY date
    ORDER BY date
'''
daily_df = pd.read_sql_query(daily_query, conn)

# Create a seaborn plot for daily patterns
plt.figure(figsize=(12, 6))
sns.regplot(data=daily_df, x='daily_units', y='daily_revenue', 
            scatter_kws={'alpha':0.5}, line_kws={'color': 'red'})
plt.title('Daily Sales: Revenue vs Units Sold')
plt.xlabel('Total Units Sold')
plt.ylabel('Total Revenue ($)')
plt.savefig('../public/graphs/daily_patterns.png', dpi=300, bbox_inches='tight')
plt.close()

# Close the database connection
conn.close() 