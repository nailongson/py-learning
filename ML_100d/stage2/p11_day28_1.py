import numpy as np
u = np.array([1., 2., 0.])
v = np.array([2., 1., 0.])
print("dot", u@v) # 点积
print("cosine", u@v/(np.linalg.norm(u)*np.linalg.norm(v))) #余弦相似度
print("cross", np.cross(u,v)) #叉积
#验证叉积与两个输入都正交
print(np.cross(u,v)@u)
print(np.cross(u,v)@v)

