# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 10:32:30 2021

@author: Jordan
"""
import pandas as pd

q_df = pd.DataFrame([['male', 'teacher'], ['male', 'engineer'], ['female', None], ['female', 'engineer']],columns=['Sex','Profession'])
#將以下問卷資料的職業(Profession) 欄位缺失值填入字串 'others'，
#更進一步將字串做編碼。 此時用什麼方式做編碼比較適合？為什麼？
q_df['Profession'] = q_df['Profession'].fillna('other')
print(q_df)
pf = pd.get_dummies(q_df[['Profession']])
pd = pd.concat([q_df,pf],axis=1)
print(pd)
print("One-hot Encoding, Profession欄位沒有順序性")