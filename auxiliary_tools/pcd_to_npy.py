import open3d as o3d
import numpy as np
import os

# 定义输入和输出目录
input_dir = "/home/star/mot/OpenPCDet/data/campus/dynamic_people/pcd"
output_dir = "/home/star/mot/OpenPCDet/data/campus/dynamic_people/npy"

# 确保输出目录存在
os.makedirs(output_dir, exist_ok=True)

# 遍历输入目录中的所有 .pcd 文件
for filename in os.listdir(input_dir):
    if filename.endswith(".pcd"):
        # 构建完整的文件路径
        input_filepath = os.path.join(input_dir, filename)
        
        # 读取PCD点云文件
        pcd = o3d.io.read_point_cloud(input_filepath)

        # 获取点的坐标
        points = np.asarray(pcd.points)

        # 如果有强度信息，则读取强度信息
        intensity = None
        if pcd.has_colors():  # 假设颜色信息存储在 colors 中，可用于替代强度
            intensity = np.asarray(pcd.colors)[:, 0]  # 假设强度为颜色中的第一个通道
        else:
            print(f"点云中不包含强度信息: {filename}")

        # 打包数据，准备保存为 npy 文件
        data = np.hstack((points, np.zeros((points.shape[0], 1))))

        # 构建输出文件路径
        output_filepath = os.path.join(output_dir, filename.replace(".pcd", ".npy"))

        # 保存为 npy 文件
        np.save(output_filepath, data)
        print(f"点云数据已保存为: {output_filepath}")
