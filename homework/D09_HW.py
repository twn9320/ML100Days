# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 08:15:35 2021

@author: Jordan
"""
import pandas as pd

#讀取資料夾中 boston.csv 讀取其欄位 CHAS、NOX、RM，輸出成 .xlsx 檔案
c_data = pd.read_csv('boston.csv',usecols=['CHAS','NOX','RM'])
print(c_data)
print("=====================")
c_data.to_excel('boston.xlsx',sheet_name='boston')
x_data = pd.read_excel('boston.xlsx')
print(x_data)