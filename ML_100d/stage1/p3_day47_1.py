import numpy as np
#学习argpartition
a = np.array([90, 10, 50, 40, 20, 80, 30])
k = 3

# kth 传入 k（即索引 3），划分出前 3 个小元素 1:10,4:20,6:30
idx = np.argpartition(a, k)

# 前 k 个元素的索引（注意：这 3 个元素内部是乱序的！）
top_k_small_idx = idx[:k]
print("前 3 小的索引:", top_k_small_idx)
print("前 3 小的数值:", a[top_k_small_idx])