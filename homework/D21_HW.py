# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 15:32:16 2021

@author: Jordan
"""
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

# 取得資料集
df = sns.load_dataset('titanic')
ax = sns.barplot(x="sex", y="survived",hue = "class", data=df)


df2 = sns.load_dataset('tips')
print(df2)
#sns.boxplot(x=, y=, data=)
#sns.stripplot(x=, y=, data=, jitter=)
#plt.show()