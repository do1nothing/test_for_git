import pickle
#/workspace/per1-3dfreespace/data_json/src_json/picked/spcar_240402/val_spcar_20240402_renew.json

info = [
    {'point_cloud':{'num_features':3,'lidar_idx':'12247C_20240426095919_500'},'pts_path':'/workspace/ixf1szh/intern_liumingxing/point-transformer/Pointcept-1.5.1/3dfreespace/pcd/12247C_20240426095919_500_selfmerge_pcd2.pcd'},
    {'point_cloud':{'num_features':3,'lidar_idx':'12247C_20240426100242_400'},'pts_path':'/workspace/ixf1szh/intern_liumingxing/point-transformer/Pointcept-1.5.1/3dfreespace/pcd/12247C_20240426100242_400_selfmerge_pcd2.pcd'},
    {'point_cloud':{'num_features':3,'lidar_idx':'12247C_20240426100548_500'},'pts_path':'/workspace/ixf1szh/intern_liumingxing/point-transformer/Pointcept-1.5.1/3dfreespace/pcd/12247C_20240426100548_500_selfmerge_pcd2.pcd'},
    {'point_cloud':{'num_features':3,'lidar_idx':'12247C_20240426100730_200'},'pts_path':'/workspace/ixf1szh/intern_liumingxing/point-transformer/Pointcept-1.5.1/3dfreespace/pcd/12247C_20240426100730_200_selfmerge_pcd2.pcd'},
    {'point_cloud':{'num_features':3,'lidar_idx':'12247C_20240426100951_000'},'pts_path':'/workspace/ixf1szh/intern_liumingxing/point-transformer/Pointcept-1.5.1/3dfreespace/pcd/12247C_20240426100951_000_selfmerge_pcd2.pcd'}
    # {'point_cloud':{'num_features':3,'lidar_idx':'1690367310.022347927'},'pts_path':'/workspace/ixf1szh/intern_liumingxing/point-transformer/Pointcept-1.5.1/data/campus/1690367310.022347927.pcd'},
    # {'point_cloud':{'num_features':3,'lidar_idx':'1690367314.122599840'},'pts_path':'/workspace/ixf1szh/intern_liumingxing/point-transformer/Pointcept-1.5.1/data/campus/1690367314.122599840.pcd'},
    # {'point_cloud':{'num_features':3,'lidar_idx':'1690367315.922855854'},'pts_path':'/workspace/ixf1szh/intern_liumingxing/point-transformer/Pointcept-1.5.1/data/campus/1690367315.922855854.pcd'},
    # {'point_cloud':{'num_features':3,'lidar_idx':'1714248080.979881984'},'pts_path':'/workspace/ixf1szh/intern_liumingxing/point-transformer/Pointcept-1.5.1/data/campus/1714248080.979881984.pcd'},
    # {'point_cloud':{'num_features':3,'lidar_idx':'1714248082.780403200'},'pts_path':'/workspace/ixf1szh/intern_liumingxing/point-transformer/Pointcept-1.5.1/data/campus/1714248082.780403200.pcd'},
    # {'point_cloud':{'num_features':3,'lidar_idx':'1714248090.280530432'},'pts_path':'/workspace/ixf1szh/intern_liumingxing/point-transformer/Pointcept-1.5.1/data/campus/1714248090.280530432.pcd'},
    # {'point_cloud':{'num_features':3,'lidar_idx':'1714248097.180360960'},'pts_path':'/workspace/ixf1szh/intern_liumingxing/point-transformer/Pointcept-1.5.1/data/campus/1714248097.180360960.pcd'},
    # {'point_cloud':{'num_features':3,'lidar_idx':'1714248107.180461312'},'pts_path':'/workspace/ixf1szh/intern_liumingxing/point-transformer/Pointcept-1.5.1/data/campus/1714248107.180461312.pcd'},
    # {'point_cloud':{'num_features':3,'lidar_idx':'1714248109.280610816'},'pts_path':'/workspace/ixf1szh/intern_liumingxing/point-transformer/Pointcept-1.5.1/data/campus/1714248109.280610816.pcd'}
]

output_path = '/workspace/ixf1szh/intern_liumingxing/point-transformer/Pointcept-1.5.1/3dfreespace/freespace2.pkl'
# output_path = '/workspace/ixf1szh/intern_liumingxing/point-transformer/Pointcept-1.5.1/3dfreespace/campus.pkl'

with open(output_path,'wb') as f:
    pickle.dump(info, f)
print("ok!!!!!!!!!!")


# [
#     {
#         "info": {
#             "id": 0,
#             "timestamp": "20230909144236",
#             "car_type": "12105C"
#         },
#         "images": {
#             "CylindricalCam": [
#                 "/workspace/per1-3dfreespace/dataset/base_data/20240402_picked/12105C/20230909144236/20230909144236.062172_VirtualCam01.jpeg",
#                 "/workspace/per1-3dfreespace/dataset/base_data/20240402_picked/12105C/20230909144236/20230909144236.062167_VirtualCam02.jpeg",
#                 "/workspace/per1-3dfreespace/dataset/base_data/20240402_picked/12105C/20230909144236/20230909144236.062144_VirtualCam03.jpeg",
#                 "/workspace/per1-3dfreespace/dataset/base_data/20240402_picked/12105C/20230909144236/20230909144236.062157_VirtualCam04.jpeg"
#             ],
#             "SurCam": [
#                 "/workspace/per1-3dfreespace/dataset/base_data/20240402_picked/12105C/20230909144236/20230909144236.062172_SurCam01.jpeg",
#                 "/workspace/per1-3dfreespace/dataset/base_data/20240402_picked/12105C/20230909144236/20230909144236.062167_SurCam02.jpeg",
#                 "/workspace/per1-3dfreespace/dataset/base_data/20240402_picked/12105C/20230909144236/20230909144236.062144_SurCam03.jpeg",
#                 "/workspace/per1-3dfreespace/dataset/base_data/20240402_picked/12105C/20230909144236/20230909144236.062157_SurCam04.jpeg"
#             ],
#             "StandSurCam": [
#                 "/workspace/per1-3dfreespace/dataset/base_data/20240402_picked/12105C/20230909144236/20230909144236.062172_StandSurCam01.jpeg",
#                 "/workspace/per1-3dfreespace/dataset/base_data/20240402_picked/12105C/20230909144236/20230909144236.062167_StandSurCam02.jpeg",
#                 "/workspace/per1-3dfreespace/dataset/base_data/20240402_picked/12105C/20230909144236/20230909144236.062144_StandSurCam03.jpeg",
#                 "/workspace/per1-3dfreespace/dataset/base_data/20240402_picked/12105C/20230909144236/20230909144236.062157_StandSurCam04.jpeg"
#             ],
#             "FrontWideCam": [
#                 "/workspace/per1-3dfreespace/dataset/base_data/20240402_picked/12105C/20230909144236/20230909144236.039278_FrontCam02.jpeg"
#             ],
#             "StandFrontCam": [
#                 "/workspace/per1-3dfreespace/dataset/base_data/20240402_picked/12105C/20230909144236/20230909144236.039278_StandFrontCam02.jpeg"
#             ]
#         }
#     }
# ]