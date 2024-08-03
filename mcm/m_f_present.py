import numpy as np
import matplotlib.pyplot as plt

# 模拟参数
initial_pm = 100  # 初始雄性数量
initial_pf = 100  # 初始雌性数量
initial_resources = 10000  # 初始资源量
resource_decay = 0.01  # 资源衰减率
carrying_capacity_base = 2000  # 基础环境承载力
time = np.linspace(0, 1, 1000)  # 时间范围和点数

# 资源量随时间变化
resources = initial_resources * np.exp(-resource_decay * time)

# 环境承载力作为资源量的函数
carrying_capacity = carrying_capacity_base * (resources / initial_resources)

# 逻辑生长函数
def logistic_growth(population, carrying_capacity, growth_rate):
    return population + growth_rate * population * (1 - population / carrying_capacity)

# 数值仿真
pm = np.zeros(len(time))
pf = np.zeros(len(time))
pm[0] = initial_pm
pf[0] = initial_pf

for t in range(1, len(time)):
    pm[t] = logistic_growth(pm[t-1], carrying_capacity[t], growth_rate=0.03)
    pf[t] = logistic_growth(pf[t-1], carrying_capacity[t], growth_rate=0.02)

total_population = pm + pf

# 绘图
plt.figure(figsize=(14, 9))

# 保存资源量动态图
plt.subplot(2, 2, 1)
plt.plot(time, resources, label="Resources")
plt.xlabel("Time")
plt.ylabel("Resources")
plt.title("Resource Dynamics")
plt.legend()
plt.savefig("resources_dynamic.png")  # 保存资源量动态图

# 保存总种群动态图
plt.subplot(2, 2, 2)
plt.plot(time, total_population, label="Total Population")
plt.plot(time, pm, label="Male Lampreys", linestyle='--')
plt.plot(time, pf, label="Female Lampreys", linestyle='--')
plt.xlabel("Time")
plt.ylabel("Population")
plt.title("Lamprey Population Dynamics")
plt.legend()
plt.savefig("population_dynamic.png")  # 保存总种群动态图

# 保存雄性与雌性的关系图
plt.subplot(2, 2, 3)
plt.plot(pm, pf, '-o', markersize=2)
plt.xlabel("Male Lampreys")
plt.ylabel("Female Lampreys")
plt.title("Relation between Male and Female Lampreys")
plt.grid(True)
plt.savefig("male_female_relation.png")  # 保存雄性与雌性的关系图


plt.tight_layout()
plt.show()
