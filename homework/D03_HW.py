# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 09:05:28 2021

@author: Jordan
"""
import numpy as np
#Gdb  = 20*log10(V1/V0) [V1為測量值、V0為聲壓標準值] 
#1.正常的談話的聲壓為 20000 微巴斯卡，請問多少分貝?
G = 20 *np.log10(20000/20)
print(G)
#2.30 分貝的聲壓會是 50 分貝的幾倍?

x = 20 * np.power(10,30/20) #30分貝轉換聲壓
y = 20 * np.power(10,50/20)
print(x/y)