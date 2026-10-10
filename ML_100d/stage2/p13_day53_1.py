import numpy as np
import matplotlib.pyplot as plt
x, y = np.meshgrid(np.linspace(-2, 2, 30), np.linspace(-2, 2, 30))
z = x*x+y*y
fig = plt.figure(figsize=(9, 4))
ax3 = fig.add_subplot(121, projection="3d")
# 调整 3D 视角以兼顾立体感与底部形态
ax3.view_init(elev=25, azim=-45)

ax3.plot_surface(x, y, z, cmap="viridis")

ax3.set(xlabel="x", ylabel="y", zlabel="z")
ax2 = fig.add_subplot(122)
ax2.contour(x, y, z)

# 在二维等高线图中增加层数并加上数值标签，更清晰展现曲率梯度
cs = ax2.contour(x, y, z, levels=10, cmap="viridis")

ax2.clabel(cs, inline=True, fontsize=8)
ax2.set(xlabel="x", ylabel="y", aspect="equal")
fig.savefig("day53_example.png", dpi=150, bbox_inches="tight")
print("Saved: day53_example.png")
plt.close(fig)