import numpy as np

# 1. 生成相关的二维数据 (X_0 和 X_1 强正相关，带非零均值)
np.random.seed(42)
n_samples = 500
x0 = np.random.normal(loc=10.0, scale=2.0, size=n_samples)
x1 = 1.5 * x0 + np.random.normal(loc=0.0, scale=1.0, size=n_samples) + 5.0
X = np.column_stack([x0, x1])

# 2. 中心化 (Zero-centering: 减去各列均值)
X_mean = np.mean(X, axis=0)
X_centered = X - X_mean

# 3. 计算样本协方差矩阵 Sigma = (X_c^T @ X_c) / (n - 1)
cov_mat = (X_centered.T @ X_centered) / (n_samples - 1)

# 4. 使用 eigh 求解实对称矩阵的特征值与特征向量
# 注：eigh 输出的特征值默认按升序排列
eigenvalues, eigenvectors = np.linalg.eigh(cov_mat)

pc1_val = eigenvalues[-1]       # 最大特征值（最大方差）
pc1_vec = eigenvectors[:, -1]   # 第一主成分方向（单位向量）
pc2_val = eigenvalues[-2]       # 次大特征值
pc2_vec = eigenvectors[:, -2]   # 第二主成分方向

print(f"协方差矩阵:\n{cov_mat}\n")
print(f"第一主方向 (PC1, 对应方差 {pc1_val:.4f}): {pc1_vec}")
print(f"第二主方向 (PC2, 对应方差 {pc2_val:.4f}): {pc2_vec}")