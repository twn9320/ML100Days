# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 15:32:16 2021

@author: Jordan
"""
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

# 取得資料集
plt.figure(0)
df = sns.load_dataset('titanic')
ax = sns.barplot(x="sex", y="survived",hue = "class", data=df)

plt.figure(1)
df2 = sns.load_dataset('tips')
print(df2.info())
sns.boxplot(x='day', y='tip', data=df2)
sns.stripplot(x='day', y='tip', data=df, jitter=True)
plt.show()
