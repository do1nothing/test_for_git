import os
import json
import pickle

# 定义文件路径
# json_file_path = '/workspace/per1-3dfreespace/data_json/src_json/picked/spcar_240402/val_spcar_20240402_renew.json'
pcd_path = '/media/user/data1/STAR/semantic_segment/Pointcept-1.5.1/data/bosch/fusion'

# 读取JSON文件内容
# with open(json_file_path, 'r', encoding='utf-8') as file:
#     data = json.load(file)

# pcd_files = [f for f in os.listdir(pcd_path) if f.endswith('.pcd')]

# 限制读取的条目数量
# max_items = 4328
results = []

# 处理前100个条目
for filename in os.listdir(pcd_path):
    try:
        if filename.endswith('.pcd'):
            lidar_idx = os.path.splitext(filename)[0]
            pcd_file_path = os.path.join(pcd_path,filename)
        
        # 检查 selfmerge_pcd.pcd 文件是否存在
        if not os.path.exists(pcd_file_path):
            print(f'File not found: {pcd_file_path}')
        
        
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

output_path = '/media/user/data1/STAR/semantic_segment/Pointcept-1.5.1/data/bosch/fusion.pkl'
with open(output_path,'wb') as f:
    pickle.dump(results,f)
    
print("ok!!!!!!!!!!")
