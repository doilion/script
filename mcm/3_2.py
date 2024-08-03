import numpy as np
import matplotlib.pyplot as plt
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

# 食物资源量随时间的变化函数
def E(F):
    return np.maximum(0, 1 - np.exp(-F / initial_F))

# 其他物种动态变化函数
def Births(S):
    return 0.1 * S

def Deaths(S):
    return 0.05 * S

def Interaction(S, Pm, Pf, F):
    return -0.01 * S * (Pm + Pf) + 0.01 * F

# 生态系统稳定性函数
def Diversity(Pm, Pf, S):
    # 计算每个时间点的多样性
    diversity = np.zeros(len(time))
    for t in range(len(time)):
        diversity[t] = -np.var([Pm[t], Pf[t], S[t]])
    return diversity

def ResourceDistribution(F):
    return -np.std(F)

# 数值仿真初始化
S = np.zeros(len(time))
pm = np.zeros(len(time))
pf = np.zeros(len(time))
S[0] = initial_S
pm[0] = initial_pm
pf[0] = initial_pf

# 使用相同的时间步长进行数值仿真
for t in range(1, len(time)):
    # 更新其他物种的数量
    dSdt = Births(S[t-1]) - Deaths(S[t-1]) + Interaction(S[t-1], pm[t-1], pf[t-1], resources[t-1])
    S[t] = S[t-1] + dSdt * (time[t] - time[t-1])
    # 更新雄性和雌性数量
    pm[t] = pm[t-1] + 0.03 * pm[t-1] * (1 - pm[t-1] / carrying_capacity[t-1])
    pf[t] = pf[t-1] + 0.02 * pf[t-1] * (1 - pf[t-1] / carrying_capacity[t-1])

# 计算生态系统稳定性
E_stability = Diversity(pm, pf, S) + ResourceDistribution(resources)

# 绘制三维曲面图并保存
fig = plt.figure(figsize=(14, 7))

# 第一个图：其他生物总量与性别比例的关系
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
gender_ratio = pm / (pm + pf)
surf1 = ax1.plot_trisurf(pm, gender_ratio, S, cmap='viridis')
ax1.set_xlabel('Male Lampreys')
ax1.set_ylabel('Gender Ratio')
ax1.set_zlabel('Other Species Population')
ax1.set_title('Other Species Population vs Gender Ratio')
fig.colorbar(surf1, ax=ax1, shrink=0.5, aspect=10)  # 添加颜色条

# 第二个图：生态系统稳定性和性别比例的关系
ax2 = fig.add_subplot(1, 2, 2, projection='3d')
surf2 = ax2.plot_trisurf(pm, gender_ratio, E_stability, cmap='plasma')
ax2.set_xlabel('Male Lampreys')
ax2.set_ylabel('Gender Ratio')
ax2.set_zlabel('Ecosystem Stability')
ax2.set_title('Ecosystem Stability vs Gender Ratio')
fig.colorbar(surf2, ax=ax2, shrink=0.5, aspect=10)  # 添加颜色条

# # 设置子图的标题
# ax1.text2D(0.5, 0.95, 'Other Species Population vs Gender Ratio', transform=ax1.transAxes, fontsize=12, ha='center')
# ax2.text2D(0.5, 0.95, 'Ecosystem Stability vs Gender Ratio', transform=ax2.transAxes, fontsize=12, ha='center')

# 显示图形
plt.tight_layout()

# 保存图像到当前工作目录
other_species_vs_gender_ratio_path = 'other_species_vs_gender_ratio.png'
ecosystem_stability_vs_gender_ratio_path = 'ecosystem_stability_vs_gender_ratio.png'
plt.savefig(other_species_vs_gender_ratio_path, bbox_inches='tight')
plt.savefig(ecosystem_stability_vs_gender_ratio_path, bbox_inches='tight')
