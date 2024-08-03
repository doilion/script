# 导入额外的库用于三维绘图
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 设置模拟参数
initial_pm = 100  # 初始雄性数量
initial_pf = 100  # 初始雌性数量
initial_S = 1000  # 其他物种的初始数量
initial_F = 10000  # 初始食物资源量
resource_decay = 0.01  # 资源衰减率
carrying_capacity_base = 2000  # 基础环境承载力
time = np.linspace(0, 100, 1000)  # 时间范围和点数

# 资源量随时间变化
resources = initial_F * np.exp(-resource_decay * time)

# 环境承载力作为资源量的函数
carrying_capacity = carrying_capacity_base * (resources / initial_F)
# 定义性别决定函数 S(F)
def S(F, S_max, k, F_critical):
    return S_max / (1 + np.exp(k * (F - F_critical)))

# 模拟参数
S_max = 0.8  # 最大雄性比例
k_values = np.linspace(-1, -0.01, 100)  # 形状参数k的范围
F_critical = 500  # 食物供应的临界点

# 创建食物供应量的数组，用于绘图
F_values = np.linspace(0, 1000, 100)

# 初始化寄生虫种群动态模型的参数
alpha = 0.01  # 寄生虫的繁殖率
D_parasite = 0.005  # 寄生虫的死亡率
initial_P_parasite = 100  # 寄生虫的初始种群数量
P_parasite = initial_P_parasite * np.ones(len(time))

# 数值仿真初始化
Pm = initial_pm * np.ones(len(time))
Pf = initial_pf * np.ones(len(time))

# 使用相同的时间步长进行数值仿真
for t in range(1, len(time)):
    # 更新寄生虫种群数量
    dP_parasitedt = alpha * (Pm[t-1] + Pf[t-1]) - D_parasite * P_parasite[t-1]
    P_parasite[t] = P_parasite[t-1] + dP_parasitedt * (time[t] - time[t-1])

# 绘制图表
fig = plt.figure(figsize=(12, 12))

# 1. 雄性七鳃鳗与 k 的关系
ax1 = fig.add_subplot(2, 2, 1, projection='3d')
for k in k_values:
    male_ratio = S(F_values, S_max, k, F_critical)
    ax1.plot(F_values, k * np.ones_like(F_values), male_ratio, label=f'k={k:.2f}')
ax1.set_xlabel('Food Supply (F)')
ax1.set_ylabel('Shape Parameter (k)')
ax1.set_zlabel('Male Ratio')
ax1.set_title('Male Lamprey Ratio vs. Food Supply and k')

# 2. 雌性七鳃鳗与 k 的关系（雌性比例是1减去雄性比例）
ax2 = fig.add_subplot(2, 2, 2, projection='3d')
for k in k_values:
    female_ratio = 1 - S(F_values, S_max, k, F_critical)
    ax2.plot(F_values, k * np.ones_like(F_values), female_ratio, label=f'k={k:.2f}')
ax2.set_xlabel('Food Supply (F)')
ax2.set_ylabel('Shape Parameter (k)')
ax2.set_zlabel('Female Ratio')
ax2.set_title('Female Lamprey Ratio vs. Food Supply and k')

# 3. 七鳃鳗总数与 k 的关系（假设总数不变）
ax3 = fig.add_subplot(2, 2, 3, projection='3d')
total_lamprey = initial_pm + initial_pf
ax3.plot(F_values, k_values, total_lamprey * np.ones_like(F_values), label='Total Lamprey')
ax3.set_xlabel('Food Supply (F)')
ax3.set_ylabel('Shape Parameter (k)')
ax3.set_zlabel('Total Lamprey')
ax3.set_title('Total Lamprey vs. Food Supply and k')

# 4. 其他物种与k 的关系（假设直接受k影响）
ax4 = fig.add_subplot(2, 2, 4, projection='3d')
for k in k_values:
    other_species = S(F_values, S_max, k, F_critical) * initial_S  # 假设与雄性比例成比例
    ax4.plot(F_values, k * np.ones_like(F_values), other_species, label=f'k={k:.2f}')
ax4.set_xlabel('Food Supply (F)')
ax4.set_ylabel('Shape Parameter (k)')
ax4.set_zlabel('Other Species')
ax4.set_title('Other Species vs. k')  # 添加标题

# 保存图像
plt.savefig('total.png')