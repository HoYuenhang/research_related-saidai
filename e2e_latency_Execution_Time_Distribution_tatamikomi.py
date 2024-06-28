import numpy as np
import matplotlib.pyplot as plt

def read_execution_times(file_paths):
    execution_times_list = []
    for file_path in file_paths:
        execution_times = []
        # 读取文件
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        # 提取执行时间
        for line in lines:
            # 找到行中冒号与 'ms' 之间的部分，并转换为浮点数
            time_str = line.split(':')[1].strip().split()[0]
            execution_times.append(float(time_str))
        
        execution_times_list.append(execution_times)
    
    # 转置列表，使得每个内部列表包含相同位置的执行时间数据
    return list(map(list, zip(*execution_times_list)))

def convolve_times(execution_times, kernel):
    return np.convolve(execution_times, kernel, mode='valid')

# 定义卷积核（取平均值的卷积核）
kernel = np.ones(3) / 3

# 文件列表
no_paralization_files = [
    'C:/Users/carlo/Downloads/no_paralization/controller_node/controller_node_execution_time.txt', 
    'C:/Users/carlo/Downloads/no_paralization/motion_velocity_smmother/motion_execution_time.txt', 
    'C:/Users/carlo/Downloads/no_paralization/PlanningValidator/onTrajectory.txt', 
    'C:/Users/carlo/Downloads/no_paralization/scenario_selector/onTimer.txt', 
    'C:/Users/carlo/Downloads/no_paralization/ekf_localizer/ekf_execution_time.txt', 
    'C:/Users/carlo/Downloads/no_paralization/ndt_scan_matcher/processing_time.txt', 
    'C:/Users/carlo/Downloads/no_paralization/crop_box_filter_measurement_range/node_processing_time.txt', 
    'C:/Users/carlo/Downloads/no_paralization/crop_box_filter_mirror/node_processing_time.txt', 
    'C:/Users/carlo/Downloads/no_paralization/crop_box_filter_self/node_processing_time.txt', 
    'C:/Users/carlo/Downloads/no_paralization/distortion_corrector/distortion_undistort_pointcloud.txt', 
    'C:/Users/carlo/Downloads/no_paralization/outlier_filter/outlier_filter_processing_time.txt'
]

paralization_files = [
    'C:/Users/carlo/Downloads/paralization/controller_node/controller_node_execution_time.txt', 
    'C:/Users/carlo/Downloads/paralization/motion_velocity_smmother/motion_execution_time.txt', 
    'C:/Users/carlo/Downloads/paralization/PlanningValidator/onTrajectory.txt', 
    'C:/Users/carlo/Downloads/paralization/scenario_selector/onTimer.txt', 
    'C:/Users/carlo/Downloads/paralization/ekf_localizer/ekf_execution_time.txt', 
    'C:/Users/carlo/Downloads/paralization/ndt_scan_matcher/processing_time.txt', 
    'C:/Users/carlo/Downloads/paralization/crop_box_filter_measurement_range/node_processing_time.txt', 
    'C:/Users/carlo/Downloads/paralization/crop_box_filter_mirror/node_processing_time.txt', 
    'C:/Users/carlo/Downloads/paralization/crop_box_filter_self/node_processing_time.txt', 
    'C:/Users/carlo/Downloads/paralization/distortion_corrector/distortion_undistort_pointcloud.txt', 
    'C:/Users/carlo/Downloads/paralization/outlier_filter/outlier_filter_processing_time.txt'
]

# 读取并合计no_paralization文件的执行时间
no_paralization_times_list = read_execution_times(no_paralization_files)
no_paralization_summed_times = [sum(times) for times in no_paralization_times_list]
before_execution_times = convolve_times(no_paralization_summed_times, kernel)

# 读取并合计paralization文件的执行时间
paralization_times_list = read_execution_times(paralization_files)
paralization_summed_times = [sum(times) for times in paralization_times_list]
after_execution_times = convolve_times(paralization_summed_times, kernel)

# 创建图形和轴
fig, ax = plt.subplots(figsize=(10, 6))


# 设置x轴的范围和间隔
bins = np.arange(0, 220, 20)

# 绘制before的分布直方图
ax.hist(before_execution_times, bins=50, color='blue', alpha=0.7, label='Before')

# 绘制after的分布直方图
ax.hist(after_execution_times, bins=50, color='red', alpha=0.7, label='After')

# 设置标题和标签
ax.set_title('Execution Time Distribution Before and After Parallelization')
ax.set_xlabel('Execution Time (ms)')
ax.set_ylabel('Frequency')


# 设置x轴范围
ax.set_xlim(0, 220)

# 添加图例
ax.legend()

# 显示图形
plt.tight_layout()
plt.savefig('C:/Users/carlo/Downloads/e2e_latency_distribution.pdf', bbox_inches='tight')
plt.show()
