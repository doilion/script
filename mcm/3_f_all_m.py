import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 定义模拟参数
initial_pm = 1000  # 初始雄性数量
initial_pf = 1000  # 初始雌性数量
growth_rate_pm = 0.05  # 雄性增长率
growth_rate_pf = 0.04  # 雌性增长率
time = np.linspace(0, 50, 500)  # 时间范围和点数

# 计算雄性和雌性七鳃鳗的数量
pm = initial_pm * (1 + growth_rate_pm * time)  # 雄性数量随时间变化
pf = initial_pf * (1 + growth_rate_pf * time)  # 雌性数量随时间变化
total_population = pm + pf  # 总种群数量

# 创建3D图形
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# 绘制参数曲线
ax.plot3D(pm, pf, total_population, 'red')

# 设置轴标签
ax.set_xlabel('Male Lampreys')
ax.set_ylabel('Female Lampreys')
ax.set_zlabel('Total Population')

# 设置标题
ax.set_title('Lamprey Population Dynamics')

plt.show()
