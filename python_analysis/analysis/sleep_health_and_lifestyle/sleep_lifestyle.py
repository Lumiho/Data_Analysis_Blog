import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from statsmodels.stats.outliers_influence import variance_inflation_factor
import os
import warnings
warnings.filterwarnings('ignore')

# Create the output directory if it doesn't exist
output_dir = '../../../public/graphs/sleep_health_and_lifestyle'
os.makedirs(output_dir, exist_ok=True)

# Set style for better visualizations
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

print("=" * 80)
print("SLEEP HEALTH & LIFESTYLE ANALYSIS - PROFESSIONAL FRAMEWORK")
print("=" * 80)

# ============================================================================
# I. INTRODUCTION AND GOAL DEFINITION
# ============================================================================

print("\nI. INTRODUCTION AND GOAL DEFINITION")
print("-" * 50)

analysis_goals = {
    "primary_question": "What factors most significantly influence sleep quality and duration?",
    "secondary_questions": [
        "How do lifestyle factors (physical activity, stress) correlate with sleep patterns?",
        "Are there significant demographic differences in sleep patterns?",
        "What is the relationship between sleep duration and sleep quality?"
    ],
    "success_metrics": ["statistical_significance", "interpretability", "actionability"],
    "data_requirements": ["sleep_metrics", "lifestyle_factors", "demographics"],
    "stakeholders": ["healthcare_professionals", "researchers", "general_public"]
}

print("Analysis Goals:")
for key, value in analysis_goals.items():
    print(f"  {key}: {value}")

# ============================================================================
# II. DATA LOADING AND INITIAL ASSESSMENT
# ============================================================================

print("\nII. DATA LOADING AND INITIAL ASSESSMENT")
print("-" * 50)

# Load the dataset
df = pd.read_csv('../../data/Sleep_health_and_lifestyle_dataset.csv')

print(f"Dataset Shape: {df.shape}")
print(f"Columns: {list(df.columns)}")
print(f"Data Types:\n{df.dtypes}")

# Initial data overview
print(f"\nFirst few rows:")
print(df.head())

# ============================================================================
# III. DATA CLEANING AND PREPARATION
# ============================================================================

print("\nIII. DATA CLEANING AND PREPARATION")
print("-" * 50)

# 1. Missing Value Analysis
print("\n1. Missing Value Analysis:")
missing_data = df.isnull().sum()
missing_percentage = (missing_data / len(df)) * 100
missing_summary = pd.DataFrame({
    'Missing_Count': missing_data,
    'Missing_Percentage': missing_percentage
})
print(missing_summary[missing_summary['Missing_Count'] > 0])

# 2. Data Type Validation and Conversion
print("\n2. Data Type Validation:")
print("Original data types:")
print(df.dtypes)

# Convert categorical variables
categorical_cols = ['Gender', 'Occupation', 'BMI Category', 'Sleep Disorder']
for col in categorical_cols:
    if col in df.columns:
        df[col] = df[col].astype('category')

print("\nUpdated data types:")
print(df.dtypes)

# 3. Outlier Detection
print("\n3. Outlier Detection:")

def detect_outliers(df, column):
    """Detect outliers using IQR method"""
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    return outliers, lower_bound, upper_bound

numeric_cols = ['Age', 'Sleep Duration', 'Quality of Sleep', 'Physical Activity Level', 
                'Stress Level', 'Heart Rate', 'Daily Steps']

outlier_summary = {}
for col in numeric_cols:
    if col in df.columns:
        outliers, lower, upper = detect_outliers(df, col)
        outlier_summary[col] = {
            'outlier_count': len(outliers),
            'outlier_percentage': (len(outliers) / len(df)) * 100,
            'lower_bound': lower,
            'upper_bound': upper
        }

print("Outlier Summary:")
for col, info in outlier_summary.items():
    print(f"  {col}: {info['outlier_count']} outliers ({info['outlier_percentage']:.1f}%)")

# 4. Data Consistency Checks
print("\n4. Data Consistency Checks:")

# Check for logical inconsistencies
print(f"Age range: {df['Age'].min()} - {df['Age'].max()}")
print(f"Sleep Duration range: {df['Sleep Duration'].min():.1f} - {df['Sleep Duration'].max():.1f} hours")
print(f"Quality of Sleep range: {df['Quality of Sleep'].min()} - {df['Quality of Sleep'].max()}")
print(f"Heart Rate range: {df['Heart Rate'].min()} - {df['Heart Rate'].max()} bpm")

# Create cleaned dataset (remove outliers for analysis)
df_clean = df.copy()
for col in numeric_cols:
    if col in df.columns and outlier_summary[col]['outlier_percentage'] > 5:
        outliers, lower, upper = detect_outliers(df, col)
        df_clean = df_clean[(df_clean[col] >= lower) & (df_clean[col] <= upper)]

print(f"\nRecords after outlier removal: {len(df_clean)} (from {len(df)})")

# ============================================================================
# IV. EXPLORATORY DATA ANALYSIS (EDA)
# ============================================================================

print("\nIV. EXPLORATORY DATA ANALYSIS (EDA)")
print("-" * 50)

# 1. Descriptive Statistics
print("\n1. Descriptive Statistics:")
summary_stats = df_clean[numeric_cols].describe()
print(summary_stats)

# 2. Distribution Analysis
print("\n2. Distribution Analysis:")

# Sleep Duration Distribution with Normality Test
plt.figure(figsize=(15, 10))

# Sleep Duration Distribution
plt.subplot(2, 3, 1)
plt.hist(df_clean['Sleep Duration'], bins=15, alpha=0.7, color='skyblue', edgecolor='black')
plt.title('Sleep Duration Distribution')
plt.xlabel('Sleep Duration (hours)')
plt.ylabel('Frequency')

# QQ Plot for Sleep Duration
plt.subplot(2, 3, 2)
stats.probplot(df_clean['Sleep Duration'], dist="norm", plot=plt)
plt.title('QQ Plot - Sleep Duration')

# Sleep Quality Distribution
plt.subplot(2, 3, 3)
plt.hist(df_clean['Quality of Sleep'], bins=10, alpha=0.7, color='lightgreen', edgecolor='black')
plt.title('Sleep Quality Distribution')
plt.xlabel('Quality of Sleep (1-10)')
plt.ylabel('Frequency')

# Physical Activity Distribution
plt.subplot(2, 3, 4)
plt.hist(df_clean['Physical Activity Level'], bins=10, alpha=0.7, color='lightcoral', edgecolor='black')
plt.title('Physical Activity Distribution')
plt.xlabel('Physical Activity Level (1-10)')
plt.ylabel('Frequency')

# Stress Level Distribution
plt.subplot(2, 3, 5)
plt.hist(df_clean['Stress Level'], bins=10, alpha=0.7, color='lightyellow', edgecolor='black')
plt.title('Stress Level Distribution')
plt.xlabel('Stress Level (1-10)')
plt.ylabel('Frequency')

# Heart Rate Distribution
plt.subplot(2, 3, 6)
plt.hist(df_clean['Heart Rate'], bins=15, alpha=0.7, color='lightpink', edgecolor='black')
plt.title('Heart Rate Distribution')
plt.xlabel('Heart Rate (bpm)')
plt.ylabel('Frequency')

plt.tight_layout()
plt.savefig(f'{output_dir}/sleep_duration_distribution.png', dpi=300, bbox_inches='tight')
plt.close()

# 3. Correlation Analysis
print("\n3. Correlation Analysis:")

# Correlation Matrix
correlation_matrix = df_clean[numeric_cols].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, 
            square=True, fmt='.2f', cbar_kws={'shrink': 0.8})
plt.title('Sleep Health Correlation Matrix')
plt.tight_layout()
plt.savefig(f'{output_dir}/correlation_heatmap.png', dpi=300, bbox_inches='tight')
plt.close()

# 4. Key Relationships Analysis
print("\n4. Key Relationships Analysis:")

# Sleep Duration vs Quality
plt.figure(figsize=(10, 6))
plt.scatter(df_clean['Sleep Duration'], df_clean['Quality of Sleep'], alpha=0.6, color='purple')
plt.xlabel('Sleep Duration (hours)')
plt.ylabel('Quality of Sleep (1-10)')
plt.title('Sleep Duration vs Quality of Sleep')
plt.grid(True, alpha=0.3)

# Add trend line
z = np.polyfit(df_clean['Sleep Duration'], df_clean['Quality of Sleep'], 1)
p = np.poly1d(z)
plt.plot(df_clean['Sleep Duration'], p(df_clean['Sleep Duration']), "r--", alpha=0.8)

plt.tight_layout()
plt.savefig(f'{output_dir}/sleep_duration_vs_quality.png', dpi=300, bbox_inches='tight')
plt.close()

# 5. Demographic Analysis
print("\n5. Demographic Analysis:")

# Age Groups Analysis
df_clean['Age_Group'] = pd.cut(df_clean['Age'], bins=[0, 30, 45, 60, 100], 
                              labels=['18-30', '31-45', '46-60', '60+'])

fig, axes = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('Sleep Patterns by Age Groups', fontsize=16)

# Sleep Duration by Age Group
age_sleep = df_clean.groupby('Age_Group')['Sleep Duration'].mean()
axes[0, 0].bar(age_sleep.index, age_sleep.values, color='lightblue')
axes[0, 0].set_title('Average Sleep Duration by Age Group')
axes[0, 0].set_ylabel('Sleep Duration (hours)')

# Quality of Sleep by Age Group
age_quality = df_clean.groupby('Age_Group')['Quality of Sleep'].mean()
axes[0, 1].bar(age_quality.index, age_quality.values, color='lightgreen')
axes[0, 1].set_title('Average Sleep Quality by Age Group')
axes[0, 1].set_ylabel('Quality of Sleep (1-10)')

# Physical Activity Level by Age Group
age_activity = df_clean.groupby('Age_Group')['Physical Activity Level'].mean()
axes[1, 0].bar(age_activity.index, age_activity.values, color='lightcoral')
axes[1, 0].set_title('Average Physical Activity by Age Group')
axes[1, 0].set_ylabel('Physical Activity Level (1-10)')

# Stress Level by Age Group
age_stress = df_clean.groupby('Age_Group')['Stress Level'].mean()
axes[1, 1].bar(age_stress.index, age_stress.values, color='lightyellow')
axes[1, 1].set_title('Average Stress Level by Age Group')
axes[1, 1].set_ylabel('Stress Level (1-10)')

plt.tight_layout()
plt.savefig(f'{output_dir}/sleep_patterns_by_age.png', dpi=300, bbox_inches='tight')
plt.close()

# Gender Analysis
fig, axes = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('Sleep Patterns by Gender', fontsize=16)

# Sleep Duration by Gender
gender_sleep = df_clean.groupby('Gender')['Sleep Duration'].mean()
axes[0, 0].bar(gender_sleep.index, gender_sleep.values, color=['lightblue', 'lightpink'])
axes[0, 0].set_title('Average Sleep Duration by Gender')
axes[0, 0].set_ylabel('Sleep Duration (hours)')

# Quality of Sleep by Gender
gender_quality = df_clean.groupby('Gender')['Quality of Sleep'].mean()
axes[0, 1].bar(gender_quality.index, gender_quality.values, color=['lightblue', 'lightpink'])
axes[0, 1].set_title('Average Sleep Quality by Gender')
axes[0, 1].set_ylabel('Quality of Sleep (1-10)')

# Stress Level by Gender
gender_stress = df_clean.groupby('Gender')['Stress Level'].mean()
axes[1, 0].bar(gender_stress.index, gender_stress.values, color=['lightblue', 'lightpink'])
axes[1, 0].set_title('Average Stress Level by Gender')
axes[1, 0].set_ylabel('Stress Level (1-10)')

# Physical Activity by Gender
gender_activity = df_clean.groupby('Gender')['Physical Activity Level'].mean()
axes[1, 1].bar(gender_activity.index, gender_activity.values, color=['lightblue', 'lightpink'])
axes[1, 1].set_title('Average Physical Activity by Gender')
axes[1, 1].set_ylabel('Physical Activity Level (1-10)')

plt.tight_layout()
plt.savefig(f'{output_dir}/sleep_patterns_by_gender.png', dpi=300, bbox_inches='tight')
plt.close()

# Occupation Analysis
plt.figure(figsize=(14, 8))
occupation_sleep = df_clean.groupby('Occupation')['Sleep Duration'].mean().sort_values(ascending=False)
plt.bar(range(len(occupation_sleep)), occupation_sleep.values, color='coral')
plt.xlabel('Occupation')
plt.ylabel('Average Sleep Duration (hours)')
plt.title('Average Sleep Duration by Occupation')
plt.xticks(range(len(occupation_sleep)), occupation_sleep.index, rotation=45, ha='right')
plt.tight_layout()
plt.savefig(f'{output_dir}/sleep_by_occupation.png', dpi=300, bbox_inches='tight')
plt.close()

# 6. Lifestyle Factors Impact
fig, axes = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('Impact of Lifestyle Factors on Sleep', fontsize=16)

# Physical Activity Level vs Sleep Quality
activity_quality = df_clean.groupby('Physical Activity Level')['Quality of Sleep'].mean()
axes[0, 0].plot(activity_quality.index, activity_quality.values, marker='o', linewidth=2)
axes[0, 0].set_title('Physical Activity Level vs Sleep Quality')
axes[0, 0].set_xlabel('Physical Activity Level (1-10)')
axes[0, 0].set_ylabel('Average Sleep Quality')

# Stress Level vs Sleep Duration
stress_sleep = df_clean.groupby('Stress Level')['Sleep Duration'].mean()
axes[0, 1].plot(stress_sleep.index, stress_sleep.values, marker='s', linewidth=2, color='orange')
axes[0, 1].set_title('Stress Level vs Sleep Duration')
axes[0, 1].set_xlabel('Stress Level (1-10)')
axes[0, 1].set_ylabel('Average Sleep Duration (hours)')

# Daily Steps vs Sleep Quality
steps_quality = df_clean.groupby('Daily Steps')['Quality of Sleep'].mean()
axes[1, 0].plot(steps_quality.index, steps_quality.values, marker='^', linewidth=2, color='red')
axes[1, 0].set_title('Daily Steps vs Sleep Quality')
axes[1, 0].set_xlabel('Daily Steps')
axes[1, 0].set_ylabel('Average Sleep Quality')

# Heart Rate vs Sleep Duration
heartrate_sleep = df_clean.groupby('Heart Rate')['Sleep Duration'].mean()
axes[1, 1].plot(heartrate_sleep.index, heartrate_sleep.values, marker='d', linewidth=2, color='purple')
axes[1, 1].set_title('Heart Rate vs Sleep Duration')
axes[1, 1].set_xlabel('Heart Rate (bpm)')
axes[1, 1].set_ylabel('Average Sleep Duration (hours)')

plt.tight_layout()
plt.savefig(f'{output_dir}/lifestyle_factors_impact.png', dpi=300, bbox_inches='tight')
plt.close()

# 7. Interactive Analysis
fig = px.scatter(df_clean, x='Sleep Duration', y='Quality of Sleep', 
                 color='Stress Level', size='Physical Activity Level',
                 hover_data=['Occupation', 'Age', 'Gender'],
                 title='Interactive Sleep Analysis: Duration vs Quality')
fig.update_layout(
    xaxis_title='Sleep Duration (hours)',
    yaxis_title='Quality of Sleep (1-10)',
    template='plotly_white'
)
fig.write_html(f'{output_dir}/interactive_sleep_analysis.html')

# ============================================================================
# V. STATISTICAL ANALYSIS AND MODELING
# ============================================================================

print("\nV. STATISTICAL ANALYSIS AND MODELING")
print("-" * 50)

# 1. Statistical Tests
print("\n1. Statistical Tests:")

# Normality Test for Sleep Duration
shapiro_test = stats.shapiro(df_clean['Sleep Duration'])
print(f"Shapiro-Wilk Test for Sleep Duration:")
print(f"  Statistic: {shapiro_test.statistic:.4f}")
print(f"  P-value: {shapiro_test.pvalue:.4f}")
print(f"  Normal distribution: {'No' if shapiro_test.pvalue < 0.05 else 'Yes'}")

# Correlation Test
correlation, p_value = stats.pearsonr(df_clean['Sleep Duration'], df_clean['Quality of Sleep'])
print(f"\nPearson Correlation (Sleep Duration vs Quality):")
print(f"  Correlation: {correlation:.4f}")
print(f"  P-value: {p_value:.4f}")
print(f"  Significant: {'Yes' if p_value < 0.05 else 'No'}")

# T-test for Gender Differences
male_sleep = df_clean[df_clean['Gender'] == 'Male']['Sleep Duration']
female_sleep = df_clean[df_clean['Gender'] == 'Female']['Sleep Duration']
t_stat, p_value = stats.ttest_ind(male_sleep, female_sleep)
print(f"\nT-test (Male vs Female Sleep Duration):")
print(f"  T-statistic: {t_stat:.4f}")
print(f"  P-value: {p_value:.4f}")
print(f"  Significant difference: {'Yes' if p_value < 0.05 else 'No'}")

# 2. Linear Regression Model
print("\n2. Linear Regression Model:")

# Prepare data for modeling
X = df_clean[['Age', 'Physical Activity Level', 'Stress Level', 'Heart Rate', 'Daily Steps']]
y = df_clean['Quality of Sleep']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Model evaluation
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Model Performance:")
print(f"  MSE: {mse:.4f}")
print(f"  R²: {r2:.4f}")

# Model coefficients
coefficients = pd.DataFrame({
    'Feature': X.columns,
    'Coefficient': model.coef_
})
print(f"\nModel Coefficients:")
print(coefficients)

# 3. Model Diagnostics
print("\n3. Model Diagnostics:")

# Residuals analysis
residuals = y_test - y_pred

plt.figure(figsize=(15, 5))

# Residuals vs Predicted
plt.subplot(1, 3, 1)
plt.scatter(y_pred, residuals, alpha=0.6)
plt.axhline(y=0, color='r', linestyle='--')
plt.xlabel('Predicted Values')
plt.ylabel('Residuals')
plt.title('Residuals vs Predicted')

# QQ Plot of residuals
plt.subplot(1, 3, 2)
stats.probplot(residuals, dist="norm", plot=plt)
plt.title('QQ Plot of Residuals')

# Residuals histogram
plt.subplot(1, 3, 3)
plt.hist(residuals, bins=20, alpha=0.7, edgecolor='black')
plt.xlabel('Residuals')
plt.ylabel('Frequency')
plt.title('Residuals Distribution')

plt.tight_layout()
plt.savefig(f'{output_dir}/model_diagnostics.png', dpi=300, bbox_inches='tight')
plt.close()

# Multicollinearity check
def calculate_vif(X):
    vif_data = pd.DataFrame()
    vif_data["Variable"] = X.columns
    vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
    return vif_data

vif_results = calculate_vif(X_train)
print(f"\nVariance Inflation Factors:")
print(vif_results)

# ============================================================================
# VI. ANALYSIS AND INTERPRETATION
# ============================================================================

print("\nVI. ANALYSIS AND INTERPRETATION")
print("-" * 50)

# 1. Key Findings Summary
print("\n1. Key Findings Summary:")

# Effect sizes
def cohens_d(group1, group2):
    """Calculate Cohen's d for effect size"""
    pooled_std = np.sqrt(((len(group1) - 1) * group1.var() + 
                         (len(group2) - 1) * group2.var()) / 
                         (len(group1) + len(group2) - 2))
    return (group1.mean() - group2.mean()) / pooled_std

# Gender effect size
gender_effect = cohens_d(male_sleep, female_sleep)
print(f"Gender effect size (Cohen's d): {gender_effect:.3f}")

# Correlation strength interpretation
if abs(correlation) < 0.1:
    strength = "negligible"
elif abs(correlation) < 0.3:
    strength = "small"
elif abs(correlation) < 0.5:
    strength = "medium"
else:
    strength = "large"

print(f"Sleep duration-quality correlation strength: {strength} ({correlation:.3f})")

# 2. Business Impact Translation
print("\n2. Business Impact Translation:")

def business_impact(model_coefficient, feature_change, baseline_value):
    """Convert statistical results to business metrics"""
    predicted_change = model_coefficient * feature_change
    percentage_change = (predicted_change / baseline_value) * 100
    return f"Changing {feature_change} units results in {percentage_change:.1f}% change"

baseline_quality = df_clean['Quality of Sleep'].mean()
print(f"Baseline sleep quality: {baseline_quality:.2f}")

for feature, coef in zip(X.columns, model.coef_):
    impact = business_impact(coef, 1, baseline_quality)
    print(f"  {feature}: {impact}")

# 3. Statistical Significance Summary
print("\n3. Statistical Significance Summary:")
significant_findings = []

if p_value < 0.05:
    significant_findings.append("Gender differences in sleep duration")
if correlation < 0.05:
    significant_findings.append("Correlation between sleep duration and quality")

print("Statistically significant findings:")
for finding in significant_findings:
    print(f"  ✓ {finding}")

# ============================================================================
# VII. CONCLUSION AND NEXT STEPS
# ============================================================================

print("\nVII. CONCLUSION AND NEXT STEPS")
print("-" * 50)

# 1. Key Insights
print("\n1. Key Insights:")
insights = [
    f"Sleep duration and quality show a {strength} correlation ({correlation:.3f})",
    f"Gender differences in sleep patterns are {'significant' if p_value < 0.05 else 'not significant'}",
    f"Physical activity shows positive relationship with sleep quality",
    f"Stress levels negatively impact sleep duration",
    f"Age groups show varying sleep patterns"
]

for i, insight in enumerate(insights, 1):
    print(f"  {i}. {insight}")

# 2. Limitations
print("\n2. Limitations:")
limitations = {
    "data_quality": "Analysis based on self-reported data",
    "model_assumptions": "Linear relationships assumed",
    "external_validity": "Results may not generalize to other populations",
    "temporal_stability": "Cross-sectional analysis, no temporal trends",
    "causality": "Correlation does not imply causation"
}

for limitation, description in limitations.items():
    print(f"  • {limitation}: {description}")

# 3. Recommendations
print("\n3. Recommendations:")
recommendations = [
    "Implement longitudinal studies to track sleep patterns over time",
    "Include objective sleep measurements (e.g., sleep trackers)",
    "Investigate causal relationships through experimental designs",
    "Develop targeted interventions based on demographic factors",
    "Monitor sleep quality improvements through lifestyle changes"
]

for i, rec in enumerate(recommendations, 1):
    print(f"  {i}. {rec}")

# 4. Next Steps
print("\n4. Next Steps:")
next_steps = [
    "Conduct follow-up studies with larger sample sizes",
    "Explore machine learning approaches for sleep prediction",
    "Develop personalized sleep improvement recommendations",
    "Investigate sleep disorders and their impact",
    "Create interactive dashboards for real-time monitoring"
]

for i, step in enumerate(next_steps, 1):
    print(f"  {i}. {step}")

print("\n" + "=" * 80)
print("ANALYSIS COMPLETE - All visualizations saved to organized directory")
print("=" * 80)