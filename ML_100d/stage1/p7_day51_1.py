import numpy as np
import matplotlib.pyplot as plt
x = np.arange(5)
y = x**2
fig, ax = plt.subplots()
ax.errorbar(x, y, yerr=np.ones(5), fmt="o-", label="measurement ±1 unit")
ax.set(xlabel="Time (s)", ylabel="Distance (m)")
ax.legend()
fig.savefig("day51_example.png", dpi=150, bbox_inches="tight")
print("Saved: day51_example.png")
plt.close(fig)
#离散数据点表示各时间节点的实验测量值，
#垂直误差棒表示仪器的绝对测量不确定度（$\pm 1\,\text{m}$，
#置信水平为 $1\sigma$，样本量 $N=5$）。
#连线用于引导视觉趋势。 图注 写在latex的