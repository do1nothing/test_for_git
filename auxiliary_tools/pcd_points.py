from pypcd import pypcd
import numpy as np


bosch_pcd_path1 = '/workspace/ixf1szh/intern_liumingxing/point-transformer/Pointcept-1.5.1/3dfreespace/pcd/12247C_20240426095919_500_selfmerge_pcd2.pcd'
bosch_pcd_path2 = '/workspace/ixf1szh/intern_liumingxing/point-transformer/Pointcept-1.5.1/3dfreespace/pcd/12247C_20240426095919_500_selfmerge_pcd.pcd'

campus_pcd_path_16 = '/workspace/ixf1szh/intern_liumingxing/point-transformer/Pointcept-1.5.1/data/campus/1690367315.922855854.pcd'
campus_pcd_path_64 = '/workspace/ixf1szh/intern_liumingxing/point-transformer/Pointcept-1.5.1/data/campus/1714248080.979881984.pcd'

# def pcd_points(path):
points = pypcd.PointCloud.from_path(campus_pcd_path_64)
points = np.vstack((points.pc_data['x'],points.pc_data['y'],points.pc_data['z'],points.pc_data['intensity'])).T
points = points[~np.isnan(points).any(axis=1)]
    # return points

coord = points[:, :3]
strength = points[:, 3].reshape([-1, 1]) / 255  # scale strength to [0, 1]

