
import numpy as np
A = np.array([[2., 1.], [1., 3.]])
b = np.array([1., 2.])
x = np.linalg.solve(A, b)
print(x, "residual", np.linalg.norm(A@x-b))
print("determinant", np.linalg.det(A), "condition", np.linalg.cond(A))