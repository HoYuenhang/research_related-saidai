import rosbag2_py

def calculate_topic_sizes(bag_file_path):
    # 初始化 reader
    reader = rosbag2_py.SequentialReader()
    storage_options = rosbag2_py.StorageOptions(uri=bag_file_path, storage_id='sqlite3')
    converter_options = rosbag2_py.ConverterOptions('', '')
    reader.open(storage_options, converter_options)

    # 获取 bag 中所有主题和类型的信息
    topics_info = reader.get_all_topics_and_types()

    # 初始化每个主题的大小计数器
    topic_sizes_bytes = {topic_info.name: 0 for topic_info in topics_info}

    # 使用序列化后的数据大小进行计算
    while reader.has_next():
        (topic_name, msg, timestamp) = reader.read_next()
        # 直接使用消息的字节长度作为大小
        message_size = len(msg)
        topic_sizes_bytes[topic_name] += message_size  # 累加到对应主题的大小

    # 将字节转换为MB
    topic_sizes_mb = {topic: size / (1024 * 1024) for topic, size in topic_sizes_bytes.items()}
    return topic_sizes_mb

# 指定你的 bag 文件路径
bag_file_path = '/home/adlink/1rosbag2_2023_07_04-17_14_26/'
topic_sizes_mb = calculate_topic_sizes(bag_file_path)

for topic, size in topic_sizes_mb.items():
    print(f"Topic: {topic}, Total Size: {size:.2f} MB")
