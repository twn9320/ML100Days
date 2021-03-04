# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 15:21:52 2021

@author: Jordan
"""
import numpy as np
import seaborn as sns

sns.set(style='whitegrid')

rs = np.random.RandomState(7)
x = rs.normal(2, 1, 75)
y = 2 + 1.5 * x + rs.normal(0, 2, 75)

sns.residplot(x, y, lowess=True, color="g")