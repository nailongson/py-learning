import numpy as np
A = np.array([[2., 1.], [1., 2.]])
values, vectors = np.linalg.eigh(A)
order = np.argsort(values)[::-1]
values, vectors = values[order], vectors[:, order]
print(values, vectors)
print(np.allclose(A@vectors, vectors*values))