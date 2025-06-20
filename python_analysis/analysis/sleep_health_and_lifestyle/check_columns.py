import pandas as pd

df = pd.read_csv('../../data/Sleep_health_and_lifestyle_dataset.csv')
print("All columns in the dataset:")
print(df.columns.tolist())
print(f"\nDataset shape: {df.shape}")
print(f"\nFirst few rows:")
print(df.head()) 