# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 09:09:48 2021

@author: Jordan
"""
import pandas as pd
#讀取 STOCK_DAY_0050_202009.csv 串聯 STOCK_DAY_0050_202010.csv，
#並且找出 open 小於 close 的資料

data09 = pd.read_csv('STOCK_DAY_0050_202009.csv')
data10 = pd.read_csv('STOCK_DAY_0050_202010.csv')
new_dt = pd.concat([data09,data10]) 
print(new_dt.loc[new_dt.open<new_dt.close])