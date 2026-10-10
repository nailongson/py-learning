# 🚀 Python & Machine Learning Learning Journey

> **"Learning by doing."** —— 从 Python 工程实操到机器学习数学基础的学习记录。

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![NumPy](https://img.shields.io/badge/NumPy-array-013243?logo=numpy)
![Pandas](https://img.shields.io/badge/Pandas-dataframe-150458?logo=pandas)
![Matplotlib](https://img.shields.io/badge/Matplotlib-plot-11557c)
![PyTorch](https://img.shields.io/badge/PyTorch-MLP-EE4C2C?logo=pytorch)

---

## 📌 项目简介

本仓库包含两条并行的学习路径：

| 路径 | 内容 | 状态 |
| --- | --- | --- |
| [`py_28d/`](./py_28d) | 28 天 Python & 深度学习实操：从 Python 基础到 MNIST 训练、YOLO 推理的端到端链路 | ✅ 已完成 |
| [`ML_100d/`](./ML_100d) | 100 天机器学习路线：数据处理三件套 + 线性代数 / 微积分预备 | 🚧 进行中 |

---

## 📂 目录结构

```text
py_learning/
├── py_28d/                   # 28 天 Python & 深度学习实操
│   ├── stage1/               # Day 02–07：Python 基础演练
│   ├── stage2/               # Day 08–14：进阶编程与脚本实战
│   ├── stage3/               # Day 16–21：API 调用（DeepSeek 多轮对话）
│   ├── stage4_B/             # Day 22–27：PyTorch 实战（MLP / MNIST、YOLOv8）
│   ├── data/                 # 数据集（MNIST 等）
│   ├── runs/                 # 训练与推理输出
│   ├── mnist_model.pth       # MNIST 模型权重
│   ├── yolov8n.pt            # YOLOv8n 预训练权重
│   └── requirements.txt      # 依赖列表
│
└── ML_100d/                  # 100 天机器学习路线
    ├── stage1/               # 数组、表格与绘图（P1–P8）
    └── stage2/               # 线代与微积分预备（P9–P13）
```

---

## 🧭 Part 1 · 28 天 Python & 深度学习实操

在 AI 辅助下完成全流程代码实操，能够逐行理解代码逻辑；神经网络与机器学习的理论课程仍在同步学习中。

### 🛠 工程能力

- **Python 基础**：变量、容器、函数定义与调用，`class` 的使用，类型标注（type hints）
- **环境管理**：`pip` 依赖安装，`conda` / `venv` 虚拟环境
- **API 调用**：终端脚本调用 DeepSeek 实现多轮对话，使用 JSON 持久化对话记录
- **深度学习**：搭建两层 MLP，在 MNIST 上完成训练与手写数字识别
- **计算机视觉**：使用 YOLOv8 对真实照片进行目标检测
- **版本控制**：Git 关联本地仓库与 GitHub，`pull` / `push` 双向同步

### 🧠 理论理解

**神经网络发展**

- 单层网络存在结构性缺陷，无法处理线性不可分等复杂问题，由此推动了多层网络的发展；但单层网络在许多场景下依然有效。
- 许多想法并非错误，只是出现得过早，受限于当时的算力与数据。
- 模型选择应从**数据**与**任务**出发，而非盲目堆叠层数；过深的网络容易过拟合，学到无关紧要的细节特征。

**训练流程**

```text
输入 → 线性加权 → 激活函数（非线性） → 下一层 → 输出得分 → 与阈值比较
                                                        ↓
                    权重更新 ← 反向传播（backward） ← 损失函数
```

- **前向传播**：逐层进行线性变换与非线性激活，得到预测结果。
- **损失函数**：量化预测与真实标签之间的差距。
- **反向传播**：从输出层向前逐层回溯，计算梯度并调整权重。
- **泛化问题**：多轮训练可提升训练集准确率，但模型可能在真实数据上表现下降，需要针对性调整。

---

## 📊 Part 2 · 100 天机器学习路线

### Stage 1 · 数组、表格与绘图

| # | Day | 主题 | 关键知识点 |
| --- | --- | --- | --- |
| P1 | 45 | NumPy 基础 | `default_rng` · `integers` / `normal` · `dtype` / `astype` · ufunc · `axis` · `shape` · `nbytes` |
| P2 | 46 | 广播与布尔筛选 | 广播规则 · 比较运算与 `&` `\|` `~` · `keepdims` |
| P3 | 47 | 索引与排序 | 切片 · `reshape` · 视图 vs 拷贝 · 花式索引 · `argsort` / `argpartition` · 结构化数组 |
| P4 | 48 | Pandas 选取与合并 | `loc` / `iloc` · Copy-on-Write · `concat` · `isna` |
| P5 | 49 | 表连接与聚合 | `merge(validate, indicator)` · `pivot` vs `pivot_table` · `groupby(observed, dropna)` |
| P6 | 50 | 字符串与时间序列 | `.str` 向量化 · `resample` · `shift` 防数据泄露 · 时区处理 |
| P7 | 51 | 绘图规范 | 线图排序 · 误差条语义 · `plt.subplots` |
| P8 | 52 | Matplotlib 直方图 | `zip` · `bins` · 导出 SVG / PNG |

<details>
<summary><b>📝 展开详细笔记</b></summary>

#### P1 · NumPy 基础
- 使用 `np.random.default_rng()` 生成随机数组：`integers` 生成随机整数，`normal` 生成正态分布浮点数。
- `dtype` 在创建时指定或查询数据类型，`astype()` 转换已有数组类型。
- `np.square()` 等 ufunc 逐元素运算；`axis` 指定沿哪个维度聚合。
- `shape` 查看形状，`nbytes` 查看内存占用。
- ⚠️ 注意整数类型的溢出问题。

#### P2 · 广播与布尔筛选
- **广播规则**：从右往左逐维比较形状，每一维需相等或其中之一为 1，满足条件后虚拟扩展对齐。
- 通过比较运算生成布尔数组，用 `&`、`|`、`~` 组合条件筛选数据。
- 聚合时设置 `keepdims=True` 保留维度，便于后续广播。

#### P3 · 索引与排序
- `.T` 转置、基础切片返回**视图**，修改会影响原数组；`.copy()` 创建独立副本。
- 花式索引 `a[[i, j]]` 与布尔掩码 `a[a > 4]` 返回副本。
- `np.argsort(a)` 返回排序索引；`np.argpartition(a, k-1)[:k]` 返回最小 k 个元素的索引（不保证有序，效率更高）。
- 通过复合 `dtype` 定义结构化数组。

#### P4 · Pandas 选取与合并
- `.loc` 按标签选取，`.iloc` 按位置选取。
- 引入 Copy-on-Write 后链式赋值不再修改原表，赋值统一使用 `.loc`。
- `pd.concat(..., ignore_index=True)` 合并行并重建索引；`.isna()` 定位缺失值。

#### P5 · 表连接与聚合
- `merge` 使用 `validate="many_to_one"` 校验键关系，`indicator=True` 查看匹配来源。
- `pivot` 仅做重塑，存在重复键时报错；`pivot_table` 通过 `aggfunc`（mean、sum 等）聚合重复项。
- `groupby` 应显式设置 `observed` 与 `dropna`，避免分类变量产生笛卡尔积。

#### P6 · 字符串与时间序列
- `.str` 批量处理字符串列：`.strip()` 去除空白字符，`.upper()` 统一大小写。
- `resample` 按时间频率分组，比 `groupby` 更适合时序数据。
- `shift(1)` 确保特征只使用过去的数据，防止"偷看未来"造成的数据泄露。
- `pd.to_datetime(..., utc=True)` 明确时区。

#### P7 · 绘图规范
- 绘制线图前先按 x 排序，避免连线误导。
- 误差条可表示测量误差、标准差或置信区间，图中须明确说明。
- 使用面向对象接口 `fig, ax = plt.subplots()`。

#### P8 · Matplotlib 直方图
- 借助 VS Code 参数提示与类型注释理解函数签名。
- `zip` 将多个序列按位置一一配对，配合 `for` 循环解包。
- 完成频率分布直方图：画布、坐标轴、标签、导出，理解 `bins` 对分布形态的影响。
- SVG 为矢量图，可无损缩放；PNG 为位图，受分辨率（dpi）限制。

</details>

### Stage 2 · 线代与微积分预备

| # | Day | 主题 | 关键知识点 |
| --- | --- | --- | --- |
| P9 | 26 | 矩阵乘法 | 矩阵即线性变换（旋转、缩放） |
| P10 | 27 | 线性方程组 | 可逆性 · `np.linalg.solve` · 残差与最小二乘 · 零空间 · 条件数 |
| P11 | 28 | 点积、叉积与特征值 | `Av = λv` 的几何意义 |
| P12 | 29 | PCA 入门 | 中心化 · 协方差矩阵 · 最大方差方向 |
| P13 | 53 | 3D 可视化 | `ax.view_init(elev, azim)` |

<details>
<summary><b>📝 展开详细笔记</b></summary>

#### P9 · 矩阵乘法
- 矩阵乘法的几何本质是线性变换：对空间进行旋转、缩放等操作。

#### P10 · 线性方程组
- 降维变换不可逆。
- 求解 `Ax = b`：寻找经变换 A 后映射到 b 的向量 x，优先使用 `np.linalg.solve`。
- 零空间 `Ax = 0`：所有被变换 A 压缩到原点的向量集合。
- 数值稳定性：残差接近零只是数值检验，还需结合尺度与条件数 `np.linalg.cond(A)` 判断；病态系统即使残差很小，也可能对输入扰动高度敏感。
- 📚 参考：3Blue1Brown《线性代数的本质》

#### P11 · 点积、叉积与特征值
- `Av = λv (v ≠ 0)`：变换后 v 仍落在自身张成的直线上。
  - λ > 0：方向保持；λ < 0：方向反转；λ = 0：映射为零向量。

#### P12 · PCA 入门
- PCA 通过寻找最大方差方向实现降维。
- 实践：生成相关二维数据 → 中心化 → 计算协方差矩阵 → 求主方向。

#### P13 · 3D 可视化
- Matplotlib 3D 子图通过 `ax.view_init(elev=..., azim=...)` 控制视角，`elev` 为仰角，`azim` 为方位角。

</details>

---

## 🎯 待深入

- [ ] 条件数与病态矩阵
- [ ] 神经网络与机器学习理论课程
- [ ] 微积分预备（梯度、链式法则）

---

## 🔗 链接

- GitHub：<https://github.com/nailongson/py-learning>
