from __future__ import print_function, division
import os
import sys
import subprocess


def class_process(dir_path, dst_dir_path, class_name):
    src_class_path = os.path.join(dir_path, class_name)
    if not os.path.isdir(src_class_path):
        return
    dst_class_path = os.path.join(dst_dir_path, class_name)
    if not os.path.exists(dst_class_path):
        os.makedirs(dst_class_path)
    for file_name in os.listdir(src_class_path):
        if '.mp4' not in file_name:
            continue
        name, ext = os.path.splitext(file_name)
        music_file_name = name + '.mp3'
        video_file_path = os.path.join(src_class_path, file_name)
        music_file_path = os.path.join(dst_class_path, music_file_name)
        cmd = 'ffmpeg -i \"{}\" \"{}\"'.format(video_file_path, music_file_path)
        print(cmd)
        subprocess.call(cmd, shell=True)
        print('\n')


if __name__ == "__main__":
    # dir_path = sys.argv[1]  # avi directory
    # # dst_dir_path = sys.argv[2]  # jpg directory
    # dir_path = "/project/data/ekman6--mp4"
    # dst_dir_path = "/project/data/ekman6--mp3"

    # class_name = sys.argv[1]

    # # for class_name in os.listdir(dir_path):
    # #     class_process(dir_path, dst_dir_path, class_name)

    # class_process(dir_path, dst_dir_path, class_name)

    # VE8
    # dir_path = "/mnt/server18_hard0/jhjang/AVER/VAANet/ve8raw"  # avi directory
    # dst_dir_path = "/mnt/server18_hard0/jhjang/AVER/VAANet/data/ve8/ve8--mp3"
    
    # EK6
    dir_path = "/mnt/server18_hard0/jhjang/AVER/VAANet/raw_ek6"  # avi directory
    dst_dir_path = "/mnt/server18_hard0/jhjang/AVER/VAANet/data/ek6/ek6--mp3"


    # dir_path = "/mnt/server18_hard0/jhjang/AVER/VAANet/data/VideoEmotion"  # avi directory
    # dst_dir_path = "/mnt/server18_hard0/jhjang/AVER/VAANet/data/VideoEmotion" # jpg directory
    # dir_path = "/project/data/ekman6/ekman6--mp4"
    # dst_dir_path = "/project/data/ekman6/ekman6--jpg"
    # class_name ="Anger"
    # class_process(dir_path, dst_dir_path, class_name)
    for class_name in os.listdir(dir_path):
        class_process(dir_path, dst_dir_path, class_name)

