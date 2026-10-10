import numpy as np
rng = np.random.default_rng(0)
a = rng.integers(0,10,size=(3, 2)).astype(np.int8)
print(a.shape, a.dtype, a.nbytes)
print(np.square(a))
print(a.mean(axis=0))