import os
import json
import pickle

# 定义文件路径
# json_file_path = '/workspace/per1-3dfreespace/data_json/src_json/picked/spcar_240402/val_spcar_20240402_renew.json'
pcd_path = '/shared/to_boyang/lidaeseg_part/20240604_picked_pcd.txt'

results = []

# for filename in os.listdir(pcd_path):
with open(pcd_path,'r') as file:
    for line in file:
        pcd_file_path = line.strip()
        lidar_idx = pcd_file_path.split('/')[-3]+'_'+pcd_file_path.split('/')[-2]

        # 生成新的 info 列表项
        info_item = {
            'point_cloud': {
                'num_features': 3,
                'lidar_idx': lidar_idx
            },
            'pts_path': pcd_file_path
        }
        
        # 添加到结果列表
        results.append(info_item)

# 输出生成的 info 列表
# print(results)

output_path = '/workspace/ixf1szh/intern_liumingxing/point-transformer/Pointcept-1.5.1/3dfreespace/816samples_.pkl'
with open(output_path,'wb') as f:
    pickle.dump(results,f)
    
print("ok!!!!!!!!!!")
