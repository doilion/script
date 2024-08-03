from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np

# 定义性别比例函数
def sex_ratio(F, k, F_critical):
    """定义性别比例与食物供应之间的关系函数"""
    S_max = 1.0  # 当食物供应极低时几乎所有幼虫都发育成为雄性
    return S_max / (1 + np.exp(k * (F - F_critical)))

# 系统动力学方程
def system_dynamics(y, t, R0, T, Dm, Df, Dl, G, alpha, D_parasite, k, F_critical):
    Pm, Pf, Pl, Pparasite, F = y  # 解包当前状态
    # 性别比例
    sex_ratio_val = sex_ratio(F, k, F_critical)

    # 七鳃鳗种群动态方程
    dPm_dt = T * Pl * sex_ratio_val - Dm * Pm
    dPf_dt = T * Pl * (1 - sex_ratio_val) - Df * Pf
    dPl_dt = R0 * Pf - Dl * Pl - T * Pl

    # 寄生虫种群动态方程
    dPparasite_dt = alpha * (Pm + Pf) - D_parasite * Pparasite

    # 食物资源动态方程
    dF_dt = G - (Pm + Pf + Pl) * F

    return [dPm_dt, dPf_dt, dPl_dt, dPparasite_dt, dF_dt]

# 参数设定
R0 = 0.1  # 基础繁殖率
T = 0.05  # 转化率
Dm = 0.02  # 雄性死亡率
Df = 0.02  # 雌性死亡率
Dl = 0.01  # 幼虫死亡率
G = 50  # 食物资源的自然增长率
alpha = 0.01  # 寄生虫繁殖率
D_parasite = 0.05  # 寄生虫的死亡率
k = -0.1  # 形状参数
F_critical = 100  # 食物供应的临界点

# 初始条件
Pm0 = 1000
Pf0 = 1000
Pl0 = 500
Pparasite0 = 100
F0 = 150

# 时间范围
t = np.linspace(0, 100, 100)

# 解常微分方程
solution = odeint(system_dynamics, [Pm0, Pf0, Pl0, Pparasite0, F0], t, args=(R0, T, Dm, Df, Dl, G, alpha, D_parasite, k, F_critical))
Pm, Pf, Pl, Pparasite, F = solution.T

# 绘制结果
plt.figure(figsize=(12, 8))

# 七鳃鳗种群数量变化图
plt.subplot(2, 2, 1)
plt.plot(t, Pm, label='Male Lampreys')
plt.plot(t, Pf, label='Female Lampreys')
plt.plot(t, Pl, label='Larvae')
plt.xlabel('Time')
plt.ylabel('Population')
plt.title('Lamprey Population Dynamics')
plt.legend()

# 食物资源变化图
plt.subplot(2, 2, 2)
plt.plot(t, F, label='Food Supply', color='orange')
plt.xlabel('Time')
plt.ylabel('Food Supply')
plt.title('Food Supply Dynamics')
plt.legend()

# 寄生虫种群变化图
plt.subplot(2, 2, 3)
plt.plot(t, Pparasite, label='Parasites', color='green')
plt.xlabel('Time')
plt.ylabel('Population')
plt.title('Parasite Population Dynamics')
plt.legend()

# 性别比例变化图
plt.subplot(2, 2, 4)
sex_ratio_values = [sex_ratio(f, k, F_critical) for f in F]
plt.plot(t, sex_ratio_values, label='Sex Ratio (Male)', color='red')
plt.xlabel('Time')
plt.show()