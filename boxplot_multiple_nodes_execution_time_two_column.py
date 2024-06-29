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
    'C:/Users/carlo/Downloads/crop_box_filter_self/node_processing_time1.txt', 
    'C:/Users/carlo/Downloads/crop_box_filter_self/node_processing_time2.txt', 
    'C:/Users/carlo/Downloads/crop_box_filter_self/node_processing_time3.txt', 
    'C:/Users/carlo/Downloads/crop_box_filter_self/node_processing_time4.txt', 
    'C:/Users/carlo/Downloads/crop_box_filter_self/node_processing_time5.txt', 
    'C:/Users/carlo/Downloads/crop_box_filter_self/node_processing_time6.txt', 
    'C:/Users/carlo/Downloads/crop_box_filter_self/node_processing_time7.txt', 
    'C:/Users/carlo/Downloads/crop_box_filter_self/node_processing_time8.txt', 
    'C:/Users/carlo/Downloads/crop_box_filter_self/node_processing_time9.txt', 
    'C:/Users/carlo/Downloads/crop_box_filter_self/node_processing_time10.txt', 
    'C:/Users/carlo/Downloads/crop_box_filter_self/node_processing_time11.txt', 
    'C:/Users/carlo/Downloads/crop_box_filter_self/node_processing_time12.txt', 
    'C:/Users/carlo/Downloads/crop_box_filter_self/node_processing_time13.txt', 
    'C:/Users/carlo/Downloads/crop_box_filter_self/node_processing_time14.txt', 
    'C:/Users/carlo/Downloads/crop_box_filter_self/node_processing_time15.txt', 
    'C:/Users/carlo/Downloads/crop_box_filter_self/node_processing_time16.txt', 
]

x_label = [
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '10',
    '11',
    '12',
    '13',
    '14',
    '15',
    '16'
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
plt.yticks(fontsize=20)  # 设置y轴刻度的字体大小
plt.xlabel('cores', fontsize=28)
plt.ylabel('execution time (ms)', fontsize=28)  # 设置y轴的标签
plt.grid(True)  # 显示网格
plt.ylim(bottom=0)
plt.tight_layout()

plt.savefig('C:/Users/carlo/Downloads/crop_box_filter_self_execution_time.pdf', bbox_inches='tight')
plt.show() 
