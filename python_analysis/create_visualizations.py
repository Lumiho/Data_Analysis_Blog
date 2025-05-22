import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Create some example data
np.random.seed(42)
dates = pd.date_range(start='2024-01-01', periods=100, freq='D')
data = {
    'date': dates,
    'value': np.random.normal(100, 15, 100).cumsum(),
    'category': np.random.choice(['A', 'B', 'C'], 100)
}
df = pd.DataFrame(data)

# 1. Create a static matplotlib plot
plt.figure(figsize=(12, 6))
plt.plot(df['date'], df['value'], linewidth=2)
plt.title('Time Series Analysis')
plt.xlabel('Date')
plt.ylabel('Value')
plt.grid(True)
# Save the static plot
plt.savefig('../public/graphs/time_series.png', dpi=300, bbox_inches='tight')
plt.close()

# 2. Create a static seaborn plot
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='category', y='value')
plt.title('Value Distribution by Category')
# Save the seaborn plot
plt.savefig('../public/graphs/boxplot.png', dpi=300, bbox_inches='tight')
plt.close()

# 3. Create an interactive plotly plot
fig = px.scatter(df, x='date', y='value', color='category',
                 title='Interactive Time Series by Category')
fig.update_layout(
    template='plotly_white',
    xaxis_title='Date',
    yaxis_title='Value'
)
# Save the interactive plot
fig.write_html('../public/graphs/interactive_scatter.html') 