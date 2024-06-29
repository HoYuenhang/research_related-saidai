import matplotlib.pyplot as plt
from matplotlib import rcParams

# フォントの設定
rcParams['pdf.fonttype'] = 42
rcParams['ps.fonttype'] = 42
rcParams['font.family'] = 'MS Gothic'

# データを格納するリスト
execution_times = []

# ファイル名のリスト
file_names = [
    'C:/Users/carlo/Downloads/no_kotei/crop_box_filter_mirror/node_processing_time1.txt', 
    'C:/Users/carlo/Downloads/kotei/crop_box_filter_mirror/node_processing_time1.txt', 
    'C:/Users/carlo/Downloads/no_kotei/crop_box_filter_mirror/node_processing_time2.txt', 
    'C:/Users/carlo/Downloads/kotei/crop_box_filter_mirror/node_processing_time2.txt', 
    'C:/Users/carlo/Downloads/no_kotei/crop_box_filter_mirror/node_processing_time3.txt', 
    'C:/Users/carlo/Downloads/kotei/crop_box_filter_mirror/node_processing_time3.txt', 
    'C:/Users/carlo/Downloads/no_kotei/crop_box_filter_mirror/node_processing_time4.txt', 
    'C:/Users/carlo/Downloads/kotei/crop_box_filter_mirror/node_processing_time4.txt', 
    'C:/Users/carlo/Downloads/no_kotei/crop_box_filter_mirror/node_processing_time5.txt', 
    'C:/Users/carlo/Downloads/kotei/crop_box_filter_mirror/node_processing_time5.txt', 
    'C:/Users/carlo/Downloads/no_kotei/crop_box_filter_mirror/node_processing_time6.txt', 
    'C:/Users/carlo/Downloads/kotei/crop_box_filter_mirror/node_processing_time6.txt', 
    'C:/Users/carlo/Downloads/no_kotei/crop_box_filter_mirror/node_processing_time7.txt', 
    'C:/Users/carlo/Downloads/kotei/crop_box_filter_mirror/node_processing_time7.txt', 
    'C:/Users/carlo/Downloads/no_kotei/crop_box_filter_mirror/node_processing_time8.txt', 
    'C:/Users/carlo/Downloads/kotei/crop_box_filter_mirror/node_processing_time8.txt', 
    'C:/Users/carlo/Downloads/no_kotei/crop_box_filter_mirror/node_processing_time9.txt', 
    'C:/Users/carlo/Downloads/kotei/crop_box_filter_mirror/node_processing_time9.txt', 
    'C:/Users/carlo/Downloads/no_kotei/crop_box_filter_mirror/node_processing_time10.txt', 
    'C:/Users/carlo/Downloads/kotei/crop_box_filter_mirror/node_processing_time10.txt', 
    'C:/Users/carlo/Downloads/no_kotei/crop_box_filter_mirror/node_processing_time11.txt', 
    'C:/Users/carlo/Downloads/kotei/crop_box_filter_mirror/node_processing_time11.txt', 
    'C:/Users/carlo/Downloads/no_kotei/crop_box_filter_mirror/node_processing_time12.txt', 
    'C:/Users/carlo/Downloads/kotei/crop_box_filter_mirror/node_processing_time12.txt', 
    'C:/Users/carlo/Downloads/no_kotei/crop_box_filter_mirror/node_processing_time13.txt', 
    'C:/Users/carlo/Downloads/kotei/crop_box_filter_mirror/node_processing_time13.txt', 
    'C:/Users/carlo/Downloads/no_kotei/crop_box_filter_mirror/node_processing_time14.txt', 
    'C:/Users/carlo/Downloads/kotei/crop_box_filter_mirror/node_processing_time14.txt', 
    'C:/Users/carlo/Downloads/no_kotei/crop_box_filter_mirror/node_processing_time15.txt', 
    'C:/Users/carlo/Downloads/kotei/crop_box_filter_mirror/node_processing_time15.txt', 
    'C:/Users/carlo/Downloads/no_kotei/crop_box_filter_mirror/node_processing_time16.txt', 
    'C:/Users/carlo/Downloads/kotei/crop_box_filter_mirror/node_processing_time16.txt', 
    
]

# データラベルのリスト
x_label = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']

# 各ファイルを読み込んでデータを抽出
for i in range(0, len(file_names), 2):
    data_group = []
    for j in range(2):
        file_name = file_names[i + j]
        with open(file_name, 'r') as file:
            lines = file.readlines()
            execution_time = [float(line.split(':')[1].strip().split()[0]) for line in lines]
            data_group.append(execution_time)
    execution_times.append(data_group)

# 箱ひげ図の作成
plt.figure(figsize=(14, 8))
positions = []
for idx, _ in enumerate(execution_times):
    positions.append(idx + 1 - 0.2)
    positions.append(idx + 1 + 0.2)

all_data = [data for group in execution_times for data in group]

plt.boxplot(all_data, 
            positions=positions, 
            widths=0.3, 
            sym='o', 
            boxprops=dict(linewidth=2),
            whiskerprops=dict(linewidth=2),
            capprops=dict(linewidth=2),
            medianprops=dict(color='red', linewidth=2))

plt.xticks(range(1, len(x_label) + 1), x_label, fontsize=20)
plt.ylabel('Execution Time (ms)', fontsize=20)
plt.grid(True)
plt.ylim(bottom=0)
plt.tight_layout()

# 図を保存
plt.savefig('C:/Users/carlo/Downloads/crop_box_filter_mirror_execution_time_two_column.pdf', bbox_inches='tight')
plt.show()
