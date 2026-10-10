import numpy as np
import matplotlib.pyplot as plt

# 构造打乱顺序的横坐标
np.random.seed(42)
x_shuffled = np.array([3, 1, 4, 0, 2])
y = x_shuffled ** 2  # 理想物理曲线 y = x^2

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 4), constrained_layout=True)

# 1. ax.plot
ax1.plot(x_shuffled, y, "o-", color="#1f77b4")
ax1.set_title("ax.plot() (Shuffled X)")

# 2. ax.scatter
ax2.scatter(x_shuffled, y, color="#e74c3c", s=50)
ax2.set_title("ax.scatter() (Shuffled X)")

plt.show()