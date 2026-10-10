import numpy as np
a = np.arange(6)
view = a[1:4]
copy = a[[1, 2, 3]]
view[0] = 99
print(a, copy)
values = np.array([5., 2., 8., 1.])
print(np.argsort(values), np.argpartition(values, 1)[:2])