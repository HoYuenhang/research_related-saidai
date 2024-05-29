# 假设数据存储在名为 "times.txt" 的文本文件中
file_name = "/home/aadp/Desktop/controller_node_execution_time.txt"

def parse_execution_times(file_name):
    times = []

    with open(file_name, 'r') as file:
        for line in file:
            # 分割每行并提取毫秒数
            parts = line.strip().split()
            if parts:
                # 将时间转换为浮点数并添加到列表中
                times.append(float(parts[2]))

    # 计算最小值、最大值和平均值
    min_time = min(times)
    max_time = max(times)
    avg_time = sum(times) / len(times)

    return min_time, max_time, avg_time

# 调用函数并打印结果
min_time, max_time, avg_time = parse_execution_times(file_name)
print(f"Minimum Execution Time: {min_time} ms")
print(f"Average Execution Time: {avg_time} ms")
print(f"Maximum Execution Time: {max_time} ms")
