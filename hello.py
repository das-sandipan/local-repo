print("hello Sandipan")
print("I am learning AI")
a = 2.5
print(a)

b = 3
c = a + b
print(c)
Name = input ("Enter your Name: ")

import numpy as np
import matplotlib.pyplot as plt
FRP = {"Mango":50,"Orange":35,"Litchi":40 }
name =  list(FRP.keys())
name
Price = list(FRP.values())
Price
plt.bar(name,Price)
plt.show()

import numpy as np
import matplotlib.pyplot as plt
Fruits = ["Mango","Orange","Banana","Litchi"]
Qty = [25,49,15,70]
plt.pie (Qty,labels=Fruits,autopct='%0.2f%%',colors=['green','orange','yellow','red'],radius=1)
plt.pie([1],colors=['white'],radius=.5)
plt.show()

import pandas as pd
import openpyxl
df = pd.read_excel('EM_Data.xlsx',sheet_name="EMD")
print(df)                
