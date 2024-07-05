import open3d as o3d
import numpy as np

def load_pcd(file_path):
    """读取PCD文件"""
    pcd = o3d.io.read_point_cloud(file_path)
    return pcd

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
    file_path = "/home/star/Downloads/1714248080.979881984.pcd"
    pcd = load_pcd(file_path)
    
    # 假设标签在文件中，我们需要加载它们
    # 这里假设标签已经在一个numpy数组labels中
    labels = np.load("/home/star/Downloads/1714248080.979881984_pred.npy")
    assert len(pcd.points) == len(labels)
    # 定义12种自定义颜色 (B, G, R)
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
        11: [127, 0, 127]
    }

    visualize_point_cloud_with_labels(pcd, labels, class_colors)

if __name__ == "__main__":
    main()
