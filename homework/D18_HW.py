# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 21:50:50 2021

@author: Jordan
"""
import matplotlib.pyplot as plt
import numpy as np

#畫出完整的 cos 圖形
x = np.arange(-2*np.pi,2*np.pi,0.1)
y = np.cos(x)
plt.plot(x,y)
plt.show()
#plt.savefig("cosimage.png",dpi=300,format="png")
#   給定散點圖顏色
X = np.random.normal(0, 1, 100)
Y = np.random.normal(0, 1, 100)
c = np.random.rand(100)
plt.scatter(X, Y,c=c)
plt.title("Scatter plot")
plt.show()