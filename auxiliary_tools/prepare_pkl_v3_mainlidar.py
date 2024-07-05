import os
import json
import pickle

# 定义文件路径
source_path = '/datasets/driving/stageb_datasets/20230615/11353C/20230615T164503/raw_pcds/'
target_filename = 'MainLidar01.pcd'


def find_files(source_path,target_filename):
    matches = []
    
    for entry in os.listdir(source_path):
        full_path = os.path.join(source_path,entry)
        if os.path.isdir(full_path):
            for file in os.listdir(full_path):
                if target_filename in file:
                    matches.append(os.path.join(full_path,file))
        else:
            print("not find file",full_path)
    return matches

target_path = find_files(source_path, target_filename)

print("ok")

# 读取JSON文件内容
# with open(json_file_path, 'r', encoding='utf-8') as file:
#     data = json.load(file)

# 限制读取的条目数量
max_items = 999
results = []
#'/datasets/driving/stageb_datasets/20230615/11353C/20230615T164503/raw_pcds/20230615T164550_900/20230615164550.900784_MainLidar01.pcd'
# 处理前100个条目
for item in target_path[:max_items]:
    try:
        # 获取 SurCam 的第一个路径
        # sur_cam_path = item['images']['SurCam'][0]
        
        # 获取文件夹路径
        # directory = os.path.dirname(sur_cam_path)
        
        # 定义 selfmerge_pcd.pcd 文件路径
        pcd_file_path = item
        
        # 检查 selfmerge_pcd.pcd 文件是否存在
        if not os.path.exists(pcd_file_path):
            print(f'File not found: {pcd_file_path}')
        
        # 获取所需的 id 和 timestamp
        # car_type = item['info']['car_type']
        # timestamp = item['info']['timestamp']
        
        # 生成 lidar_idx
        lidar_idx = pcd_file_path.split('/')[-1].split('_MainLidar')[0]
        
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
print(len(results))

output_path = '/workspace/ixf1szh/intern_liumingxing/point-transformer/Pointcept-1.5.1/3dfreespace/MainLidar.pkl'
with open(output_path,'wb') as f:
    pickle.dump(results,f)
    
print("ok!!!!!!!!!!")
