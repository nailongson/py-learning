import numpy as np
rng = np.random.default_rng(0)
a = rng.normal(size=(3, 2)).astype(np.float32)
print(a.shape, a.dtype, a.nbytes)
print(np.square(a))
print(a.mean(axis=0))