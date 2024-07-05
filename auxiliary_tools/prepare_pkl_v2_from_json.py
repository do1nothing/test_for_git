import os
import json
import pickle

# 定义文件路径
json_file_path = '/workspace/per1-3dfreespace/data_json/src_json/picked/spcar_240402/val_spcar_20240402_renew.json'

# 读取JSON文件内容
with open(json_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# 限制读取的条目数量
max_items = 4328
results = []

# 处理前100个条目
for item in data[:max_items]:
    try:
        # 获取 SurCam 的第一个路径
        sur_cam_path = item['images']['SurCam'][0]
        
        # 获取文件夹路径
        directory = os.path.dirname(sur_cam_path)
        
        # 定义 selfmerge_pcd.pcd 文件路径
        pcd_file_path = os.path.join(directory, 'selfmerge_pcd.pcd')
        
        # 检查 selfmerge_pcd.pcd 文件是否存在
        if not os.path.exists(pcd_file_path):
            print(f'File not found: {pcd_file_path}')
        
        # 获取所需的 id 和 timestamp
        car_type = item['info']['car_type']
        timestamp = item['info']['timestamp']
        
        # 生成 lidar_idx
        lidar_idx = f'{car_type}_{timestamp}'
        
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
    
    except KeyError as e:
        print(f'Missing expected key: {e} in item {item}')

# 输出生成的 info 列表
# print(results)

output_path = '/workspace/ixf1szh/intern_liumingxing/point-transformer/Pointcept-1.5.1/3dfreespace/freespace_all.pkl'
with open(output_path,'wb') as f:
    pickle.dump(results,f)
    
print("ok!!!!!!!!!!")
