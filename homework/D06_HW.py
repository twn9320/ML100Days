# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 18:03:29 2021

@author: Jordan
"""
import numpy as np
#
#1.將下兩列 array 存成 npz 檔 array1 = np.array(range(30))array2 = np.array([2,3,5])
array1 = np.array(range(30))
array2 = np.array([2,3,5])
with open('multi_array.npz', 'wb') as f:
    np.savez(f, array1, array2)

#2.讀取剛剛的 npz 檔，加入下列 array 一起存成新的 npz 檔
array3 = np.array([[4,5,6], [1,2,3]])
npzfile = np.load('multi_array.npz')
with open('new_array.npz','wb') as f:
  np.savez(f,npzfile['arr_0'],npzfile['arr_1'],array3)
