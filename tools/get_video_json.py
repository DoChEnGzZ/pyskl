'''
Author: dochengzz
Date: 2023-11-08 20:13:58
LastEditTime: 2023-11-08 20:17:50
LastEditors: dochengzz
Description: 
FilePath: /pyskl/tools/get_video_json.py
'''
import os
import cv2
import json
import argparse

# 创建命令行参数解析器
parser = argparse.ArgumentParser(description="Get video information and save it to a JSON file.")
parser.add_argument('video_directory', help="Path to the directory containing video files.")
parser.add_argument('output_json_file', help="Path to the output JSON file.")

# 解析命令行参数
args = parser.parse_args()

video_directory = args.video_directory
output_json_file = args.output_json_file

# 初始化一个字典来存储视频信息
video_info = []

# 遍历目录中的所有文件
for root, dirs, files in os.walk(video_directory):
    for file in files:
        if file.endswith(('.mp4', '.avi', '.mov', '.mkv', '.wmv')):
            video_path = os.path.join(root, file)
            
            # 使用 OpenCV 打开视频文件
            cap = cv2.VideoCapture(video_path)
            
            if not cap.isOpened():
                print(f"Failed to open {video_path}")
                continue
            
            # 获取视频帧总数
            end_frame = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            
            # 视频信息字典
            info = {
                'vid_name': os.path.splitext(file)[0],
                'end_frame': end_frame,
                'start_frame': 0,
                'label': 'unknown'
            }
            
            video_info.append(info)
            cap.release()

# 将视频信息保存为 JSON 文件
with open(output_json_file, 'w') as json_file:
    json.dump(video_info, json_file, indent=4)

print(f"Video information saved to {output_json_file}")
