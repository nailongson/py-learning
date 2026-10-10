import numpy as np
A = np.array([[1,2],[2,1]])
u = np.array([3,3])
v = np.array([2,8])
z = u+v
print(A@z)
print(A@u+A@v)
