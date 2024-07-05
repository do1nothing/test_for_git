import pickle
from pypcd import pypcd
import numpy as np

# 定义文件路径
pkl_path = '/workspace/ixf1szh/intern_liumingxing/point-transformer/Pointcept-1.5.1/3dfreespace/816samples_.pkl'
a_txt_path = '/workspace/ixf1szh/intern_liumingxing/point-transformer/Pointcept-1.5.1/ptv3_eval/analyse_two_noaug_sort_1.txt'
b_txt_path = '/workspace/ixf1szh/intern_liumingxing/point-transformer/Pointcept-1.5.1/ptv3_eval/analyse_two_noaug_sort_2.txt'
output_path = '/workspace/ixf1szh/intern_liumingxing/point-transformer/Pointcept-1.5.1/3dfreespace/816samples_pickSome.pkl'

# 读取前10行并提取日期字符串的函数
def read_and_extract_dates(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()[:10]
    dates = [line.split('_')[1].split('.')[0] for line in lines]
    return dates

# 从a.txt和b.txt中提取日期字符串
# search_strings = read_and_extract_dates(a_txt_path) + read_and_extract_dates(b_txt_path)
search_strings = list(set(read_and_extract_dates(a_txt_path) + read_and_extract_dates(b_txt_path)))
# 读取pkl文件
with open(pkl_path, 'rb') as f:
    data_list = pickle.load(f)

# 搜索匹配项并收集结果
results = []
for search_string in search_strings:
    matching_indices = [i for i, item in enumerate(data_list) if search_string in item['pts_path']]
    for idx in matching_indices:
        pcd_file_path = data_list[idx]['pts_path']
        lidar_idx = pcd_file_path.split('/')[-3] + '_' + pcd_file_path.split('/')[-2]
        
        info_item = {
            'point_cloud': {
                'num_features': 3,
                'lidar_idx': lidar_idx
            },
            'pts_path': pcd_file_path
        }
        results.append(info_item)

# 保存结果到新的pkl文件
with open(output_path, 'wb') as f:
    pickle.dump(results, f)

print("ok!!!!!!!!!!")
