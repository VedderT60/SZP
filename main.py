import numpy as np
import pandas as pd

# a = np.array([20, 30, 40, 50])
# b = np.arange(4)
#
# c= a + b
# print(c)
#
# d = np.sqrt(b)
# print(d)
# e = d + c
#
# print(e)

a = np.arange(12).reshape((3,4))
print(a)
print(a.sum())
print(a.sum(axis=0))
print(a.sum(axis=1))
print(a.cumsum(axis=0))
print(a.cumsum(axis=1))
