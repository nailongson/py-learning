import numpy as np
A = np.array([[2., 1.], [0., 1.]])
v = np.array([1., 2.])
print(f"{A}\n")
print(A @ v)
X = np.array([[1., 0.], [0., 1.], [1., 2.]])
print(X @ A.T)