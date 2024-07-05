import open3d as o3d
import numpy as np

def load_pcd(file_path):
    """读取点云文件"""
    data = np.fromfile(file_path, dtype=np.float32).reshape(-1, 4)  # 读取XYZI点云
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(data[:, :3])  # 仅使用XYZ坐标
    return pcd

def load_labels(file_path):
    """读取标签文件"""
    labels = np.fromfile(file_path, dtype=np.uint8, count = -1)
    return labels

def convert_bgr_to_rgb(bgr_color):
    return [bgr_color[2], bgr_color[1], bgr_color[0]]

def generate_colors(labels, class_colors):
    colors = np.zeros((len(labels), 3))
    unique_labels = np.unique(labels)
    print(f"Unique labels in the data: {unique_labels}")
    for label, color in class_colors.items():
        if label in unique_labels:
            rgb_color = convert_bgr_to_rgb(color)
            colors[labels == label] = np.array(rgb_color) / 255.0  # 将颜色值标准化到 [0, 1]
    return colors

def visualize_point_cloud_with_labels(pcd, labels, class_colors):
    """可视化带标签的点云"""
    colors = generate_colors(labels, class_colors)
    pcd.colors = o3d.utility.Vector3dVector(colors)
    o3d.visualization.draw_geometries([pcd])

def main():
    pcd_file_path = "/home/star/mot/OpenPCDet/data/nuscenes_some/n015-2018-07-18-11-07-57+0800__LIDAR_TOP__1531883530449377.pcd.bin"
    labels_file_path = "/home/star/Downloads/nuscenes_some/3388933b59444c5db71fade0bbfef470_lidarseg.bin"
    pcd = load_pcd(pcd_file_path)
    
    # 加载标签
    labels = load_labels(labels_file_path)
    print(len(pcd.points))
    print(len(labels))
    assert len(pcd.points) == len(labels)
    
    # 定义12种自定义颜色 (R, G, B)
    class_colors = {
        0: [0, 255, 0], 
        1: [127, 127, 127], 
        2: [255, 0, 0], 
        3: [0, 255, 255], 
        4: [255, 0, 255],
        5: [127, 127, 0], 
        6: [255, 255, 0], 
        7: [0, 127, 127], 
        8: [0, 0, 127], 
        9: [0, 63, 63],
        10: [0, 0, 255], 
        11: [127, 0, 127],
        12: [63, 63, 0],
        13: [63, 0, 63],
        14: [0, 63, 127],
        15: [127, 63, 0],
        16: [255, 127, 0],
        17: [0, 127, 255],
        18: [127, 255, 0],
        19: [255, 0, 127],
        20: [0, 127, 63],
        21: [127, 63, 127],
        22: [63, 127, 0],
        23: [255, 63, 0],
        24: [63, 0, 255],
        25: [127, 0, 255],
        26: [0, 255, 127],
        27: [127, 255, 127],
        28: [255, 127, 127],
        29: [0, 255, 63],
        30: [127, 0, 63],
        31: [255, 63, 127]
    }


    visualize_point_cloud_with_labels(pcd, labels, class_colors)

if __name__ == "__main__":
    main()
