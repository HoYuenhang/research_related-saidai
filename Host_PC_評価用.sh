source ~/autoware/install/setup.bash
# Kraken側autoware起動開始
#sleep 90
# autoware起動完了, rosbag再生開始
ros2 bag play ~/autoware_map/sample-rosbag/sample.db3 -s sqlite3 &
# ros2 bag play ~/1rosbag2_2023_07_04-17_14_26/rosbag2_2023_07_04-17_14_26_0.db3 -s sqlite3 &
sleep 30
# rosbag初期化完了, goal pose設置
ros2 topic pub /planning/mission_planning/goal geometry_msgs/PoseStamped '{header: {frame_id: "map"}, pose: {position: {x: 89555.2, y: 42369.7}, orientation: {z: 0.853417, w: 0.521229}}'} --once
# goal pose設置完了
echo "Host PC側のコマンドは実行完了しました."
