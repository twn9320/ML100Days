# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 13:26:01 2021

@author: Jordan
"""
import pandas as pd
import matplotlib.pyplot as plt
#題目 : 將資料夾中 boston.csv 讀進來，並用圖表分析欄位。
#1.畫出箱型圖，並判斷哪個欄位的中位數在 300~400 之間？
df = pd.read_csv('boston.csv')
print(df)
box = df.boxplot()
box.plot()
plt.show()

#2.畫出散佈圖 x='NOX', y='DIS' ，並說明這兩欄位有什麼關係？
scatter = df.plot.scatter(x='NOX',y='DIS')
scatter.plot()
plt.show()
#NOX值越小 DIS越大

