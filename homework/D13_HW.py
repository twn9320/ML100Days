# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 19:22:26 2021

@author: Jordan
"""
import pandas as pd

#對以下成績資料做分析
score_df = pd.DataFrame([[1,56,66,70], 
              [2,90,45,34],
              [3,45,32,55],
              [4,70,77,89],
              [5,56,80,70],
              [6,60,54,55],
              [7,45,70,79],
              [8,34,77,76],
              [9,25,87,60],
              [10,88,40,43]],columns=['student_id','math_score','english_score','chinese_score'])
#score_df = score_df.set_index('student_id')

#1.6 號學生(student_id=6) 3 科平均分數為何？
print(score_df.loc[score_df['student_id']==6].mean(axis=1))

#2.6 號學生 3 科平均分數是否有贏過班上一半的同學？
print("平均中位數",score_df.mean(axis=1).median())
#3.由於班上同學成績不好，所以學校統一加分，加分方式為開根號乘以十，請問 6 號同學 3 科成績分別是？
score_df = score_df.apply(lambda x :x **0.5 *10)
print(score_df)
#4.承上題，加分後各科班平均變多少？
print(score_df.mean())


