# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 19:51:23 2021

@author: Jordan
"""
import numpy as np
name_list = ['小明','小華','小菁','小美','小張','John','Mark','Tom']
sex_list = ['boy','boy','girl','girl','boy','boy','boy','boy']
weight_list = [67.5,75.3,50.1,45.5,80.8,90.4,78.4,70.7]
rank_list = [8,1,5,4,7,6,2,3]
myopia_list = [True,True,False,False,True,True,False,False]

#1.將上列 list 依照['name', 'sex', 'weight', 'rank', 'myopia']順序擺入 array，並且資料型態順序擺入[Unicode,Unicode,float,int,boolean]
dt = np.dtype({'names':('name', 'sex', 'weight', 'rank','myopia'), 'formats':('U5', 'U4', float,int, '?')})
new_arr = np.zeros(8, dtype=dt)
print(new_arr.dtype)
new_arr['name'] = name_list
new_arr['sex'] = sex_list
new_arr['weight'] = weight_list
new_arr['rank'] = rank_list
new_arr['myopia'] = myopia_list
print(new_arr)

#2.呈上題，將 array 中體重(weight)數據集取出算出全部平均體重
print(np.mean(new_arr['weight']))
#3.呈上題，進一步算出男生(sex 欄位是 boy)平均體重、女生(sex 欄位是 girl)平均體重
print(new_arr[new_arr['sex']=='boy']['weight'].mean())