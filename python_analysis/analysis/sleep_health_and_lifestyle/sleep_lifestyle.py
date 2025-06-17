import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
# pip install dependencies, virtual env recommended

df = pd.read_csv('../../data/Sleep_health_and_lifestyle_dataset.csv') # import dataset with pandas

sleep_dur = df['Sleep Duration'].dropna() # focus on Sleep Duration for now. Drop null/missing values

stats.probplot(sleep_dur, dist="norm", plot=plt) # Creates a QQ plot, checking for normalized distribution
plt.title("QQ Plot - Sleep Duration") # Adds title
plt.savefig('figures/qq_sleep_duration.png')  # or any relative path you want
plt.close()  # good practice to clear the figure