# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 10:00:30 2021

@author: Jordan
"""
import numpy as np 

#english_score = np.array([55,89,76,65,48,70])
#math_score = np.array([60,85,60,68,55,60])
#chinese_score = np.array([65,90,82,72,66,77])
#上 3 列共六位同學的英文、數學、國文成績，第一個元素代表第一位同學，
#舉例第一位同學英文 55 分、數學 60 分、國文 65 分，運用上列數據回答下列問題。

english_score = np.array([55,89,76,65,48,70])
math_score = np.array([60,85,60,68,55,60])
chinese_score = np.array([65,90,82,72,66,77])

#1有多少學生英文成績比數學成績高？
greater_arr = np.greater(english_score,math_score)
print(sum(greater_arr))


#2是否全班同學最高分都是國文？
greater_en = np.greater(chinese_score,english_score)
greater_ma = np.greater(chinese_score,math_score)
print(np.logical_and(greater_en,greater_ma).all())

