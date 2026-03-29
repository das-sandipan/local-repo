import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df = pd.read_excel('EM_Data.xlsx',sheet_name="EMD")
Name = list(df['Name'])[0:5]
print(Name)
MRP = list(df['Price (USD)'])[0:5]
print(MRP)
sns.lineplot(x="Stock Quantity",y="Price (USD)",data=df,hue="Category",style="Category")
plt.show()