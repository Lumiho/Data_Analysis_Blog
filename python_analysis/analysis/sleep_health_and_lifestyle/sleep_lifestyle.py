import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os
# pip install dependencies, virtual env recommended

# Create the output directory if it doesn't exist
output_dir = '../../../public/graphs/sleep_health_and_lifestyle'
os.makedirs(output_dir, exist_ok=True)

# Load the dataset
df = pd.read_csv('../../data/Sleep_health_and_lifestyle_dataset.csv')

# 1. QQ Plot for Sleep Duration (existing analysis)
sleep_dur = df['Sleep Duration'].dropna()
stats.probplot(sleep_dur, dist="norm", plot=plt)
plt.title("QQ Plot - Sleep Duration Distribution")
plt.savefig(f'{output_dir}/qq_sleep_duration.png', dpi=300, bbox_inches='tight')
plt.close()

# 2. Sleep Duration Distribution
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.hist(sleep_dur, bins=15, alpha=0.7, color='skyblue', edgecolor='black')
plt.title('Sleep Duration Distribution')
plt.xlabel('Sleep Duration (hours)')
plt.ylabel('Frequency')

plt.subplot(1, 2, 2)
sns.boxplot(y=sleep_dur, color='lightgreen')
plt.title('Sleep Duration Box Plot')
plt.ylabel('Sleep Duration (hours)')
plt.tight_layout()
plt.savefig(f'{output_dir}/sleep_duration_distribution.png', dpi=300, bbox_inches='tight')
plt.close()

# the QQ plot looks approximately normal, but the histogram shows a right-skewed distribution. let's perform a shapiro-wilk test to confirm
# perform a shapiro-wilk test to confirm the distribution is normal
shapiro_test = stats.shapiro(sleep_dur)
print("Shapiro-Wilk Test Results:")
print(f"Statistic: {shapiro_test.statistic:.4f}")
print(f"p-value: {shapiro_test.pvalue:.4f}")
if shapiro_test.pvalue < 0.05:
    print("The distribution is not normal")
else:
    print("The distribution is normal")

# 3. Sleep Duration vs Quality of Sleep
plt.figure(figsize=(10, 6))
plt.scatter(df['Sleep Duration'], df['Quality of Sleep'], alpha=0.6, color='purple')
plt.xlabel('Sleep Duration (hours)')
plt.ylabel('Quality of Sleep (1-10)')
plt.title('Sleep Duration vs Quality of Sleep')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(f'{output_dir}/sleep_duration_vs_quality.png', dpi=300, bbox_inches='tight')
plt.close()

# 4. Sleep Duration by Occupation
plt.figure(figsize=(14, 8))
occupation_sleep = df.groupby('Occupation')['Sleep Duration'].mean().sort_values(ascending=False)
plt.bar(range(len(occupation_sleep)), occupation_sleep.values, color='coral')
plt.xlabel('Occupation')
plt.ylabel('Average Sleep Duration (hours)')
plt.title('Average Sleep Duration by Occupation')
plt.xticks(range(len(occupation_sleep)), occupation_sleep.index, rotation=45, ha='right')
plt.tight_layout()
plt.savefig(f'{output_dir}/sleep_by_occupation.png', dpi=300, bbox_inches='tight')
plt.close()

# 5. Correlation Heatmap (using available numeric columns)
numeric_cols = ['Sleep Duration', 'Quality of Sleep', 'Physical Activity Level', 
                'Stress Level', 'Heart Rate', 'Daily Steps']
correlation_matrix = df[numeric_cols].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, 
            square=True, fmt='.2f', cbar_kws={'shrink': 0.8})
plt.title('Sleep Health Correlation Matrix')
plt.tight_layout()
plt.savefig(f'{output_dir}/correlation_heatmap.png', dpi=300, bbox_inches='tight')
plt.close()

# 6. Interactive Sleep Quality Analysis
fig = px.scatter(df, x='Sleep Duration', y='Quality of Sleep', 
                 color='Stress Level', size='Physical Activity Level',
                 hover_data=['Occupation', 'Age'],
                 title='Interactive Sleep Analysis: Duration vs Quality')
fig.update_layout(
    xaxis_title='Sleep Duration (hours)',
    yaxis_title='Quality of Sleep (1-10)',
    template='plotly_white'
)
fig.write_html(f'{output_dir}/interactive_sleep_analysis.html')

# 7. Sleep Patterns by Age Groups
df['Age_Group'] = pd.cut(df['Age'], bins=[0, 30, 45, 60, 100], 
                        labels=['18-30', '31-45', '46-60', '60+'])

fig, axes = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('Sleep Patterns by Age Groups', fontsize=16)

# Sleep Duration by Age Group
age_sleep = df.groupby('Age_Group')['Sleep Duration'].mean()
axes[0, 0].bar(age_sleep.index, age_sleep.values, color='lightblue')
axes[0, 0].set_title('Average Sleep Duration by Age Group')
axes[0, 0].set_ylabel('Sleep Duration (hours)')

# Quality of Sleep by Age Group
age_quality = df.groupby('Age_Group')['Quality of Sleep'].mean()
axes[0, 1].bar(age_quality.index, age_quality.values, color='lightgreen')
axes[0, 1].set_title('Average Sleep Quality by Age Group')
axes[0, 1].set_ylabel('Quality of Sleep (1-10)')

# Physical Activity Level by Age Group
age_activity = df.groupby('Age_Group')['Physical Activity Level'].mean()
axes[1, 0].bar(age_activity.index, age_activity.values, color='lightcoral')
axes[1, 0].set_title('Average Physical Activity by Age Group')
axes[1, 0].set_ylabel('Physical Activity Level (1-10)')

# Stress Level by Age Group
age_stress = df.groupby('Age_Group')['Stress Level'].mean()
axes[1, 1].bar(age_stress.index, age_stress.values, color='lightyellow')
axes[1, 1].set_title('Average Stress Level by Age Group')
axes[1, 1].set_ylabel('Stress Level (1-10)')

plt.tight_layout()
plt.savefig(f'{output_dir}/sleep_patterns_by_age.png', dpi=300, bbox_inches='tight')
plt.close()

# 8. Lifestyle Factors Impact
fig, axes = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('Impact of Lifestyle Factors on Sleep', fontsize=16)

# Physical Activity Level vs Sleep Quality
activity_quality = df.groupby('Physical Activity Level')['Quality of Sleep'].mean()
axes[0, 0].plot(activity_quality.index, activity_quality.values, marker='o', linewidth=2)
axes[0, 0].set_title('Physical Activity Level vs Sleep Quality')
axes[0, 0].set_xlabel('Physical Activity Level (1-10)')
axes[0, 0].set_ylabel('Average Sleep Quality')

# Stress Level vs Sleep Duration
stress_sleep = df.groupby('Stress Level')['Sleep Duration'].mean()
axes[0, 1].plot(stress_sleep.index, stress_sleep.values, marker='s', linewidth=2, color='orange')
axes[0, 1].set_title('Stress Level vs Sleep Duration')
axes[0, 1].set_xlabel('Stress Level (1-10)')
axes[0, 1].set_ylabel('Average Sleep Duration (hours)')

# Daily Steps vs Sleep Quality
steps_quality = df.groupby('Daily Steps')['Quality of Sleep'].mean()
axes[1, 0].plot(steps_quality.index, steps_quality.values, marker='^', linewidth=2, color='red')
axes[1, 0].set_title('Daily Steps vs Sleep Quality')
axes[1, 0].set_xlabel('Daily Steps')
axes[1, 0].set_ylabel('Average Sleep Quality')

# Heart Rate vs Sleep Duration
heartrate_sleep = df.groupby('Heart Rate')['Sleep Duration'].mean()
axes[1, 1].plot(heartrate_sleep.index, heartrate_sleep.values, marker='d', linewidth=2, color='purple')
axes[1, 1].set_title('Heart Rate vs Sleep Duration')
axes[1, 1].set_xlabel('Heart Rate (bpm)')
axes[1, 1].set_ylabel('Average Sleep Duration (hours)')

plt.tight_layout()
plt.savefig(f'{output_dir}/lifestyle_factors_impact.png', dpi=300, bbox_inches='tight')
plt.close()

# 9. Gender Analysis
plt.figure(figsize=(12, 8))
fig, axes = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('Sleep Patterns by Gender', fontsize=16)

# Sleep Duration by Gender
gender_sleep = df.groupby('Gender')['Sleep Duration'].mean()
axes[0, 0].bar(gender_sleep.index, gender_sleep.values, color=['lightblue', 'lightpink'])
axes[0, 0].set_title('Average Sleep Duration by Gender')
axes[0, 0].set_ylabel('Sleep Duration (hours)')

# Quality of Sleep by Gender
gender_quality = df.groupby('Gender')['Quality of Sleep'].mean()
axes[0, 1].bar(gender_quality.index, gender_quality.values, color=['lightblue', 'lightpink'])
axes[0, 1].set_title('Average Sleep Quality by Gender')
axes[0, 1].set_ylabel('Quality of Sleep (1-10)')

# Stress Level by Gender
gender_stress = df.groupby('Gender')['Stress Level'].mean()
axes[1, 0].bar(gender_stress.index, gender_stress.values, color=['lightblue', 'lightpink'])
axes[1, 0].set_title('Average Stress Level by Gender')
axes[1, 0].set_ylabel('Stress Level (1-10)')

# Physical Activity by Gender
gender_activity = df.groupby('Gender')['Physical Activity Level'].mean()
axes[1, 1].bar(gender_activity.index, gender_activity.values, color=['lightblue', 'lightpink'])
axes[1, 1].set_title('Average Physical Activity by Gender')
axes[1, 1].set_ylabel('Physical Activity Level (1-10)')

plt.tight_layout()
plt.savefig(f'{output_dir}/sleep_patterns_by_gender.png', dpi=300, bbox_inches='tight')
plt.close()

print("All visualizations have been created successfully in the organized subfolder!")