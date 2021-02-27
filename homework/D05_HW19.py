# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 11:59:28 2021

@author: Jordan
"""
import numpy as np

english_score = np.array([55,89,76,65,48,70])
math_score = np.array([60,85,60,68,np.nan,60])
chinese_score = np.array([65,90,82,72,66,77])

#1.請計算各科成績平均、最大值、最小值、標準差，其中數學缺一筆資料可忽略？
i=0
n = ['English','math','chinese']
for arr in (english_score,math_score,chinese_score):
  print(n[i])
  i+=1
  print('平均:',np.nanmean(arr))
  print('最大值:',np.nanmax(arr))
  print('最小值:',np.nanmin(arr))
  print('標準差:',np.nanstd(arr))
  print("===========")
  

#2.第五位同學補考數學後成績為 55，請計算補考後數學成績平均、最大值、最小值、標準差？
math_score[4]=55
print("補考後(math):")
print('平均:',np.nanmean(math_score))
print('最大值:',np.nanmax(math_score))
print('最小值:',np.nanmin(math_score))
print('標準差:',np.nanstd(math_score))
  

#3.用補考後資料找出與國文成績相關係數最高的學科？
ch_en = np.concatenate([chinese_score,english_score]).reshape(2,6)
print(np.corrcoef(ch_en))
ch_ma = np.concatenate([chinese_score,math_score]).reshape(2,6)
print(np.corrcoef(ch_ma))
