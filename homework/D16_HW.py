# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 15:45:49 2021

@author: Jordan
"""
import numpy as np
import pandas as pd
index = pd.date_range('1/1/2019', periods=20, freq='D')
series = pd.Series(range(20), index=index)

#1. 將所有轉為周資料
series_week = series.resample('W').mean()
print(series_week)
print("======")

#2. 將周資料的值取平均
print(series_week.mean())