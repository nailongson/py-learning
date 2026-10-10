import numpy as np
from scipy.linalg import null_space

A = np.array([
    [1.0, 2.0],
    [2.0, 4.0]
])

# null_space 返回一组单位化的零空间正交基底
v = null_space(A)

print("非零零空间向量:\n", v)
print("验证 A @ v:\n", np.round(A @ v, 6))