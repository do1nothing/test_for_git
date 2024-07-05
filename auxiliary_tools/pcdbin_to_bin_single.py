import numpy as np
import os

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

def main():
    lidar_path = '/home/star/mot/OpenPCDet/data/nuscenes_some/n015-2018-07-18-11-07-57+0800__LIDAR_TOP__1531883530449377.pcd.bin'
    points = read_pcd_bin(lidar_path)
    coord = points[:, :3]
    strength = points[:, 3].reshape([-1, 1]) / 255  # scale strength to [0, 1]

    converted_coords = convert_coords(coord)

    # Save as .bin file
    output_bin_path = "/home/star/mot/OpenPCDet/data/nuscenes_bin/n015-2018-07-18-11-07-57+0800__LIDAR_TOP__1531883530449377.bin"
    save_bin(output_bin_path, converted_coords, strength)

if __name__ == "__main__":
    main()


