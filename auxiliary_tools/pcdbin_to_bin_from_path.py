import os
import numpy as np

def read_pcd_bin(file_path):
    points = np.fromfile(file_path, dtype=np.float32).reshape([-1, 5])
    return points

def convert_coords(points):
    # .pcd.bin: 右x, 前y, 上z
    # .bin: 前x, 左y, 上z
    # .pcd.bin (x_pcd, y_pcd, z_pcd) -> .bin (x_bin, y_bin, z_bin)
    # x_bin = y_pcd
    # y_bin = -x_pcd
    # z_bin = z_pcd
    x_pcd, y_pcd, z_pcd = points[:, 0], points[:, 1], points[:, 2]
    x_bin = y_pcd
    y_bin = -x_pcd
    z_bin = z_pcd
    converted_points = np.stack((x_bin, y_bin, z_bin), axis=-1)
    return converted_points

def save_bin(file_path, points, strength):
    # Combine coordinates and strength
    data_to_save = np.hstack((points, strength))
    data_to_save.astype(np.float32).tofile(file_path)

def convert_directory(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith('.pcd.bin'):
            input_file_path = os.path.join(input_dir, filename)
            output_file_path = os.path.join(output_dir, filename.replace('.pcd.bin', '.bin'))

            points = read_pcd_bin(input_file_path)
            coord = points[:, :3]
            strength = points[:, 3].reshape([-1, 1]) / 255  # scale strength to [0, 1]

            converted_coords = convert_coords(coord)

            # Save as .bin file
            save_bin(output_file_path, converted_coords, strength)
            print(f"Converted {filename} to {output_file_path}")

def main():
    input_dir = "/home/star/mot/OpenPCDet/data/nuscenes_some"  # 输入.pcd.bin文件的目录
    output_dir = "/home/star/mot/OpenPCDet/data/nuscenes_bin"  # 输出.bin文件的目录

    convert_directory(input_dir, output_dir)

if __name__ == "__main__":
    main()
