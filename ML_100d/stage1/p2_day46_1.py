import numpy as np
X = np.array([[1., 10.], [2., 20.], [3., 30.]])
centered = X-X.mean(axis=0, keepdims=True)
mask = (X[:, 0] >= 2) & (X[:, 1] < 30)
print(centered, X[mask])