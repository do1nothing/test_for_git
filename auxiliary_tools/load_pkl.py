import pickle
from pypcd import pypcd
import numpy as np

# pkl_path = '/workspace/ixf1szh/intern_liumingxing/point-transformer/Pointcept-1.5.1/3dfreespace/816samples_.pkl'
pkl_path = '/workspace/ixf1szh/intern_liumingxing/point-transformer/Pointcept-1.5.1/3dfreespace/12049C_12553C_11142C_11139C_9940C_12257C_10074C_11238C_11173C_11143C_11811C_12275C_11180C_12040C_12247C_11956C_12324C_v2_pickSome.pkl'

with open(pkl_path, 'rb') as f:
    data_list = pickle.load(f)
print('gggg')
#/workspace/per1-3dfreespace/dataset/base_data/20240604_picked/11143C/20230824130251/selfmerge_pcd.pcd
search_string = '20230526095151'
matching_indices = [i for i, item in enumerate(data_list) if search_string in item['pts_path']]

lidar_path = data_list[matching_indices[0]]['pts_path']
import pdb;pdb.set_trace()
points = pypcd.PointCloud.from_path(lidar_path)
points_np = np.vstack((points.pc_data['x'],points.pc_data['y'],points.pc_data['z'],points.pc_data['intensity'])).T
points_np = points_np[~np.isnan(points_np).any(axis=1)]
        
print(matching_indices) 


#'/workspace/per1-3dfreespace/dataset/base_data/20240604_picked/10074C/20230505104920/selfmerge_pcd.pcd'