# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 19:25:36 2021

@author: Jordan
"""
import numpy as np
array1 = np.array([[10, 8], [3, 5]])
#1.運用上列array計算反矩陣，乘上原矩陣，並觀察是否為單位矩陣?
A = np.linalg.inv(array1)
print(A)
print(np.matmul(array1,A))

#2.運用上列array計算特徵值、特徵向量?
w,v = np.linalg.eig(array1)
print('w',w)
print('v',v)

#3.運用上列array計算SVD?
u,s,vh = np.linalg.svd(array1)
print('u',u)
print('v',s)
print('vh',vh)
