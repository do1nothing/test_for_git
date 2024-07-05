import os

def count_bin_files(directory):
    # 检查路径是否存在
    if not os.path.exists(directory):
        print(f"路径 {directory} 不存在。")
        return 0
    
    # 获取目录下的所有文件和文件夹
    files_and_dirs = os.listdir(directory)
    
    # 过滤出 .bin 文件
    bin_files = [f for f in files_and_dirs if f.endswith('.bin')]
    
    # 返回 .bin 文件的数量
    return len(bin_files)

# 示例：指定路径
directory_path = '/media/user/data1/STAR/semantic_segment/Pointcept-1.5.1/data/nuscenes/raw/samples/LIDAR_TOP'
directory_path = '/media/user/data1/STAR/semantic_segment/Pointcept-1.5.1/data/nuscenes/raw/sweeps/LIDAR_TOP'
# directory_path = '/media/user/data1/XRY/bevfusion/data/nuScenes/samples/LIDAR_TOP'
directory_path = '/media/user/data1/Datasets/nuscenes/raw/sweeps/LIDAR_TOP'
bin_file_count = count_bin_files(directory_path)

print(f"路径 {directory_path} 下共有 {bin_file_count} 个 .bin 文件。")
