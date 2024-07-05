import os
import json
import pickle
from pypcd import pypcd

# PCD文件路径
pcd_path = '/workspace/share-per1/sbo2szh/data_p1/tmp/pcd/12049C_12553C_11142C_11139C_9940C_12257C_10074C_11238C_11173C_11143C_11811C_12275C_11180C_12040C_12247C_11956C_12324C.txt'

results = []
errors = []  # 用于保存出现异常的PCD文件路径和异常信息
num = 0
# 打开PCD文件路径列表文件
with open(pcd_path, 'r') as file:
    for line in file:
        pcd_file_path = line.strip()
        lidar_idx = pcd_file_path.split('/')[-3] + '_' + pcd_file_path.split('/')[-2]
        num += 1
        if num == 7890:
            print(num)
        print(pcd_file_path,"num:",num)
        try:
            # 尝试读取PCD文件
            points = pypcd.PointCloud.from_path(pcd_file_path)
            # 如果成功读取，创建info_item并添加到results中
            info_item = {
                'point_cloud': {
                    'num_features': 3,
                    'lidar_idx': lidar_idx
                },
                'pts_path': pcd_file_path
            }
            results.append(info_item)
        except Exception as e:
            # 如果读取失败，记录异常信息和文件路径
            errors.append({'file_path': pcd_file_path, 'error_message': str(e)})
            continue  # 跳过当前循环，继续处理下一个文件
print("11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111")
print(num)
# 打印出异常信息
for error in errors:
    print(f"Error reading PCD file {error['file_path']}: {error['error_message']}")
print("2222")
# 保存结果到pickle文件
output_path = '/workspace/ixf1szh/intern_liumingxing/point-transformer/Pointcept-1.5.1/3dfreespace/12049C_12553C_11142C_11139C_9940C_12257C_10074C_11238C_11173C_11143C_11811C_12275C_11180C_12040C_12247C_11956C_12324C_v2.pkl'
with open(output_path, 'wb') as f:
    pickle.dump(results, f)

print("ok!!!!!!!!!!")
