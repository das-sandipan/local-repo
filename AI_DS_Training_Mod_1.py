# Basic of Statistics for Data Science
# code to generate synthetic data
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
np.random.seed(42) # reproducibility of same dataset

n = 1000

data = pd.DataFrame({
    "customers": np.random.poisson(200, n),
    "discount": np.random.uniform(0,0.4,n),
    "marketing_spend": np.random.normal(2000,500,n),
    "store_size": np.random.normal(5000,1000,n)
})

data["sales"] = (
    data["customers"] * np.random.uniform(8,12,n)
    + data["marketing_spend"] * 0.5
    + data["discount"]*500
    + np.random.normal(0,300,n)
)
# Above code to generate synthetic data
# data.head()
# data.tail()
# data.columns
# data["sales"].tail()
# data["sales"].mean()
# data["sales"].median()
# data["discount"].mode()
# data["sales"].var()
# data["sales"].std()
plt.hist(data["sales"], bins=30)
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.show()
# above code to plot hsitogram
np.mean(data["sales"]>3500)
high_discount = data["discount"] > 0.2
high_sales = data["sales"] > 3500
np.mean(high_sales[high_discount])

plt.scatter(data["customers"], data["sales"])
plt.xlabel("customers")
plt.ylabel("sales")
plt.title("Customers Vs Sales")
plt.show()
# Above code to plot scatter chart

data[["customers","sales"]].corr()
data.corr()
data["sales"].skew()
# You are presenting insights to the Business Head Ret. Ops
data["sales"].mean() # << What is the typical daily sales?
data["sales"].std() # << Are sales stable or volatile ?
data[["discount","sales"]].corr() # Do discounts influence sales?
np.mean(data["sales"] > 3000) # What is the probability sales exceed 7K ?
(data["sales"] > 3500).sum() # How many rows are actyally exceed 3K?
# ----- end ------
# ----- new ------
import numpy as np, pandas as pd, seaborn as sns, matplotlib.pyplot as plt
from scipy import stats
import statsmodels.api as sm

#  making charts readable and results reproducible
np.random.seed(7)
sns.set(context="notebook", style="white")
plt.rcParams['figure.figsize'] = (8,5)

# --- Generating a sample, realistic dataset ---
days = 180
dates = pd.date_range("2025-01-01", periods=days, freq="D")

trend = np.linspace(0, 10000, days)      #tiny uptrend over months
season = 30000 * np.sin(np.linspace(0, 6*np.pi, days))      #wavy seasonality
noise_in = np.random.normal(0, 20000, days)
noise_out = np.random.normal(0, 18000, days)

cash_in = 300000 + trend + season + noise_in
cash_out = 270000 + 0.5*season + noise_out
actual_pos = cash_in - cash_out
forecast_pos = actual_pos + np.random.normal(0, 25000, days) + 5000
DSO = np.clip(np.random.normal(45, 8, days), 20, 80)

df = pd.DataFrame({
    'date': dates,
    'cash_in': cash_in,
    'cash_out': cash_out,
    'actual_pos': actual_pos,
    'forecast_pos': forecast_pos,
    'forecast_error': actual_pos - forecast_pos,
    'DSO': DSO
})

print("Rows:",len(df)) # print to see the data
df.head()
df.describe().T # Data sanity snapshot (numbers only)

# Visual Daily Net Position Over The Time
# to observe if sertain months are typically Higher or Lower
sns.lineplot(data=df, x='date', y='actual_pos')
plt.title('Actual Daily Net Position'); plt.xlabel('Date'); plt.ylabel('Amount');
plt.show()

# descriptive Statistics - Typical DAy & Spread

# Number at a glance
mean_fe = df['forecast_error'].mean()
median_fe = df['forecast_error'].median()
std_fe = df['forecast_error'].std(ddof=1)
skew_fe = stats.skew(df['forecast_error'])
print(f"Mean FE: {mean_fe:,.0f} | Median FE: {median_fe:,.0f} | Std: {std_fe:,.0f} | Skew: {skew_fe:,.2f}")

# Visual Distribution and Key Lines
sns.histplot(df['forecast_error'], bins=30, kde=True,color="#f6caf9")
plt.axvline(mean_fe, color='red',linestyle='--',label=f'Mean {mean_fe:,.0f}')
plt.axvline(median_fe, color='green',linestyle='-.', label=f'Meadian {median_fe:,.0f}')
plt.title('Forecast Error - Distribution (Mean vs Median)'); plt.legend();plt.show()

# Friendly interception
if mean_fe > median_fe:
    print("Interpretation: Mean > Median -> right-tailed (a few big positive days pull the mean up).")
elif mean_fe < median_fe:
    print("Interpretation: Mean < Median -> left-tailed (a few big negative days pull the mean down).")
else:
    print("Interpretation: Mean = Median -> roughly symmetric around the center.")

# Percentiles & IQR
# IQR = 75TH percentile - 25th percentile: middle 50% of days
# Use percentiles when the histogram looks skewed or has long tails.

p25, p50, p75 = np.percentile(df['forecast_error'], [25, 50, 75])  
iqr = p75 - p25
p90, p10 = np.percentile(df['forecast_error'], [90, 10])
print(f"25th: {p25:,.0f} | 50th (median): {p50:,.0f} | 75th: {p75:,.0f} | IQR: {iqr:,.0f}")
print(f"10th: {p10:,.0f} | 90th: {p90:,.0f}")

# Outliers change the mean more than the median

sample = df['forecast_error'].copy()
with_outlier = pd.concat([sample, pd.Series([300000])], ignore_index=True)
print('Original -> Mean:', round(sample.mean()), 'Median:', round(sample.median()))
print('With big outlier -> Mean:', round(with_outlier.mean()), 'Median:', round(with_outlier.median()))