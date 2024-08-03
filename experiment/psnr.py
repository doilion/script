import matplotlib.pyplot as plt
import re

# 日志文件路径
log_file_path = r'C:\Users\DELL\Desktop\test\val.log'

# 初始化空列表来存储迭代次数和PSNR值
iters = []
psnrs = []

# 更新正则表达式以匹配新的日志格式
pattern = r'epoch: (\d+), iter: *([\d,]+)> psnr: ([\d\.e\+\-]+)'

# 读取日志文件并提取所需数据
with open(log_file_path, 'r') as file:
    for line in file:
        match = re.search(pattern, line)
        if match:
            iter_num = int(match.group(2).replace(',', ''))
            psnr_value = float(match.group(3))
            iters.append(iter_num)
            psnrs.append(psnr_value)

# 检查数据列表是否为空
if not iters or not psnrs:
    print("No data found in the log file.")
else:
    print(f"Loaded {len(iters)} data points. Sorting and plotting the graph...")
    # 对迭代次数和PSNR值进行排序
    sorted_iters_psnrs = sorted(zip(iters, psnrs), key=lambda x: x[0])
    sorted_iters = [x[0] for x in sorted_iters_psnrs]
    sorted_psnrs = [x[1] for x in sorted_iters_psnrs]
    # 绘制PSNR变化曲线
    plt.figure(figsize=(10, 6))
    plt.plot(sorted_iters, sorted_psnrs, marker='o', linestyle='-', color='b')
    plt.title('PSNR Change Over Iterations')
    plt.xlabel('Iteration')
    plt.ylabel('PSNR (dB)')
    plt.grid(True)
    plt.savefig('psnr_plot.png')  # 保存图片
    plt.show()