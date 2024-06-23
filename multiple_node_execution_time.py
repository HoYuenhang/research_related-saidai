import matplotlib.pyplot as plt
from matplotlib import rcParams

# txtファイルのフォーマット例
# Execution time: 0.834 ms
# Execution time: 0.765 ms
# ･･･

rcParams['pdf.fonttype'] = 42  # PDFフォントタイプを設定
rcParams['ps.fonttype'] = 42  # PSフォントタイプを設定
rcParams['font.family'] = 'MS Gothic'  # フォントファミリーを設定

# データを格納するリスト
execution_times = []

# ファイル名のリスト
file_names = [
    'C:/Users/12578/Downloads/crop_box_filter系/node_execution_time_20240616/crop_box_filter_measurement_range/node_processing_time.txt', 
    'C:/Users/12578/Downloads/crop_box_filter系/crop_2_execution_time_20240616/crop_box_filter_measurement_range/node_processing_time.txt', 
    'C:/Users/12578/Downloads/crop_box_filter系/crop_4_execution_time_20240616/crop_box_filter_measurement_range/node_processing_time.txt', 
    'C:/Users/12578/Downloads/crop_box_filter系/crop_8_execution_time_20240616/crop_box_filter_measurement_range/node_processing_time.txt', 
    'C:/Users/12578/Downloads/crop_box_filter系/crop_14_6_10_execution_time_20240617/crop_box_filter_measurement_range/node_processing_time.txt', 
    'C:/Users/12578/Downloads/crop_box_filter系/crop_15_6_11_execution_time_20240617/crop_box_filter_measurement_range/node_processing_time.txt', 
    'C:/Users/12578/Downloads/crop_box_filter系/crop_16_6_12_execution_time_20240617/crop_box_filter_measurement_range/node_processing_time.txt', 
    'C:/Users/12578/Downloads/crop_box_filter系/crop_16_execution_time_20240616/crop_box_filter_measurement_range/node_processing_time.txt', 
    'C:/Users/12578/Downloads/crop_box_filter系/crop_17_5_17_execution_time_20240617/crop_box_filter_measurement_range/node_processing_time.txt', 
    'C:/Users/12578/Downloads/crop_box_filter系/crop_18_6_18_execution_time_20240617/crop_box_filter_measurement_range/node_processing_time.txt', 
    'C:/Users/12578/Downloads/crop_box_filter系/crop_19_7_19_execution_time_20240617/crop_box_filter_measurement_range/node_processing_time.txt', 
    'C:/Users/12578/Downloads/crop_box_filter系/crop_20_9_20_execution_time_20240617/crop_box_filter_measurement_range/node_processing_time.txt', 
    'C:/Users/12578/Downloads/crop_box_filter系/crop_32_execution_time_20240616/crop_box_filter_measurement_range/node_processing_time.txt', 
]

x_label = [
    '1',
    '2',
    '4',
    '8',
    '10',
    '11',
    '12',
    '16',
    '17',
    '18',
    '19',
    '20',
    '32'
]

# 各ファイルを読み込んでデータを抽出
for file_name in file_names:
    execution_time = []
    with open(f'{file_name}', 'r') as file:
        lines = file.readlines()
        for line in lines:
            time_str = line.split(':')[1].strip().split()[0]
            execution_time.append(float(time_str))
    execution_times.append(execution_time)

# 箱ひげ図の作成
plt.figure(figsize=(14, 8))  # 図のサイズを設定
plt.boxplot(execution_times, 
            labels=x_label,  # ラベルを設定
            sym='o',  # 外れ値のマークを設定
            boxprops=dict(linewidth=2),  # 箱の線幅を設定
            whiskerprops=dict(linewidth=2),  # ヒゲの線幅を設定
            capprops=dict(linewidth=2),  # ヒゲの端線の線幅を設定
            medianprops=dict(color='red', linewidth=2))  # 中央値線の設定
plt.xticks(fontsize=20)  # 设置x轴刻度的字体大小
# plt.xlabel('cores', fontsize=20)
plt.ylabel('execution time (ms)', fontsize=20)  # 设置y轴的标签
plt.grid(True)  # 显示网格
plt.ylim(bottom=0)
plt.tight_layout()

plt.savefig('C:/Users/12578/Downloads/crop_box_filter_measurement_range_execution_time.pdf', bbox_inches='tight')
plt.show() 
