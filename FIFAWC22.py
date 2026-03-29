import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
fwc = pd.read_excel('FIFA_WC_22.xlsx',sheet_name='FWC22')
sns.pairplot(fwc,hue="Club")
plt.show()
