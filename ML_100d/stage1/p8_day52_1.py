import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
x = rng.normal(size=200)

fig, axes = plt.subplots(1, 2, sharey=True, constrained_layout=True)

for ax, bins in zip(axes, [8, 25]):
    # 1. 用 counts 接住柱高，用 bin_edges 接住边界点数组
    counts, bin_edges, _ =ax.hist(x, bins=bins, density=True)
    ax.set(xlabel="Value", ylabel="Density", title=f"bins={bins}")

    # 2. 对边界点做差分，得到每个柱子的宽度数组
    widths = np.diff(bin_edges)

    # 3. 柱高 (counts) × 柱宽 (widths) 之和
    total_area = np.sum(counts * widths)
    print(f"bins={bins} 柱高与宽度乘积之和 (总面积): {total_area:.6f}")

# fig.savefig("day52_example.png", dpi=150, bbox_inches="tight")
# 紧凑导出两类格式
fig.savefig("distribution_150dpi.png", dpi=150, bbox_inches="tight")
fig.savefig("distribution_vector.svg", bbox_inches="tight")
# print("Saved: day52_example.png")
print("Saved:distribution_150dpi.png ")
print("Saved:distribution_vector.svg ")
plt.close(fig)