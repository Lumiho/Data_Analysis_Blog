import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency
import warnings
warnings.filterwarnings('ignore')

# Set style
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

# Create output directory
output_dir = '../../../public/graphs/stroke'
os.makedirs(output_dir, exist_ok=True)

# Load data
df = pd.read_csv('python_analysis/data/healthcare-dataset-stroke-data.csv')

# Data preprocessing (same as notebook)
df['bmi'] = df['bmi'].fillna(df['bmi'].median())
df = df.drop(columns=['id'])

# Convert categorical columns
categorical_cols = ['gender', 'ever_married', 'work_type', 'Residence_type', 'smoking_status']
for col in categorical_cols:
    df[col] = df[col].astype('category')

# Binary columns
binary_cols = ['hypertension', 'heart_disease', 'stroke']
for col in binary_cols:
    df[col] = df[col].astype('category')

# EDA Analysis
df_eda = df.copy()

# 1. Missing Values Heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df_eda.isna(), cbar=False)
plt.title("Missing Values Heatmap")
plt.tight_layout()
plt.savefig(f'{output_dir}/missing_values_heatmap.png', dpi=300, bbox_inches='tight')
plt.close()

# 2. Distribution Plots for Numeric Variables
numeric_cols = df_eda.select_dtypes(include=['int64', 'float64']).columns.tolist()

for col in numeric_cols:
    plt.figure(figsize=(8, 5))
    sns.histplot(df_eda[col], kde=True)
    plt.title(f"Distribution of {col} (skew={df_eda[col].skew():.2f})")
    plt.tight_layout()
    plt.savefig(f'{output_dir}/{col}_distribution.png', dpi=300, bbox_inches='tight')
    plt.close()

# 3. Count Plots for Categorical Variables
categorical_cols_plot = df_eda.select_dtypes('category').columns.tolist()

for col in categorical_cols_plot:
    plt.figure(figsize=(8, 5))
    sns.countplot(x=col, data=df_eda)
    plt.title(f"Count Plot of {col}")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f'{output_dir}/{col}_countplot.png', dpi=300, bbox_inches='tight')
    plt.close()

# 4. Box Plots for Numeric vs Target
target = 'stroke'

for col in numeric_cols:
    if col != target:
        plt.figure(figsize=(8, 5))
        sns.boxplot(x=target, y=col, data=df_eda)
        plt.title(f"{col} vs {target}")
        plt.tight_layout()
        plt.savefig(f'{output_dir}/{col}_vs_stroke_boxplot.png', dpi=300, bbox_inches='tight')
        plt.close()

# 5. Categorical vs Target Plots
for col in categorical_cols_plot:
    if col != target:
        plt.figure(figsize=(8, 5))
        sns.countplot(x=col, hue=target, data=df_eda)
        plt.title(f"{col} vs {target}")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(f'{output_dir}/{col}_vs_stroke_countplot.png', dpi=300, bbox_inches='tight')
        plt.close()

# 6. Correlation Heatmap
corr = df_eda.corr(numeric_only=True)
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", center=0)
plt.title("Correlation Matrix (Numeric Variables)")
plt.tight_layout()
plt.savefig(f'{output_dir}/correlation_heatmap.png', dpi=300, bbox_inches='tight')
plt.close()

# 7. ROC Curve (from model results)
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, roc_auc_score
import statsmodels.api as sm

# Prepare data for model
df_encoded = pd.get_dummies(df, drop_first=True, dtype=float)
# Check what columns are available after encoding
print("Available columns after encoding:", df_encoded.columns.tolist())
# Find stroke column (might be encoded)
stroke_cols = [col for col in df_encoded.columns if 'stroke' in col.lower()]
print("Stroke-related columns:", stroke_cols)
X = df_encoded.drop(columns=stroke_cols)
y = df_encoded[stroke_cols[0]] if stroke_cols else df_encoded.iloc[:, -1]
X = sm.add_constant(X)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Fit model
model = sm.Logit(y_train, X_train)
result = model.fit()

# Predictions
y_pred = result.predict(X_test)

# ROC Curve
fpr, tpr, thresholds = roc_curve(y_test, y_pred)
auc = roc_auc_score(y_test, y_pred)

plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, label=f'AUC = {auc:.3f}', linewidth=2)
plt.plot([0, 1], [0, 1], 'k--', label='Random Classifier')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve - Stroke Prediction Model')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(f'{output_dir}/roc_curve.png', dpi=300, bbox_inches='tight')
plt.close()

print("All plots saved successfully!")
print(f"Plots saved to: {output_dir}")
