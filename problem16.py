import numpy as np
import matplotlib.pyplot as plt

# 环境温度
T_env = 60  

# 初始条件
T0 = 90  

# 已知条件：10分钟后温度
T10 = 88  

# Newton's Law of Cooling 解的一般形式：
# T(t) = T_env + (T0 - T_env) * exp(k * t)

# 用已知条件解 k
# 88 = 60 + (90 - 60) * exp(k * 10)
k = np.log((T10 - T_env) / (T0 - T_env)) / 10

# 定义温度函数
def T(t):
    return T_env + (T0 - T_env) * np.exp(k * t)

# 计算20分钟后的温度
T20 = T(20)

# 计算冷却到65°F所需时间
# 65 = 60 + (90 - 60) * exp(k * t)
t_65 = np.log((65 - T_env) / (T0 - T_env)) / k

print(f"冷却常数 k = {k:.5f}")
print(f"20分钟后的温度: {T20:.2f} °F")
print(f"冷却到 65°F 所需时间: {t_65:.2f} 分钟")

# 可视化
time = np.linspace(0, 60, 200)  # 模拟1小时
temperature = T(time)

plt.figure(figsize=(8,5))
plt.plot(time, temperature, label="Temperature curve")
plt.scatter([0, 10, 20, t_65], [T0, T10, T20, 65], color='red', zorder=5)
plt.axhline(y=T_env, color='gray', linestyle="--", label="Environment Temperature")
plt.title("Newton's Law of Cooling")
plt.xlabel("Time (minutes)")
plt.ylabel("Temperature (°F)")
plt.legend()
plt.grid(True)
plt.show()
