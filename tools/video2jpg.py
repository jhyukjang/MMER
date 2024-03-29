from __future__ import print_function, division
import os

import subprocess
import pdb

def class_process(dir_path, dst_dir_path, class_name):
    class_path = os.path.join(dir_path, class_name)
    if not os.path.isdir(class_path):
        return
    dst_class_path = os.path.join(dst_dir_path, class_name)

    if not os.path.exists(dst_dir_path):
        os.makedirs(dst_class_path)
    print(class_path)



    for file_name in os.listdir(class_path):
        if '.mp4' not in file_name:
            continue
        name, ext = os.path.splitext(file_name)

        dst_directory_path = os.path.join(dst_class_path, name)
        video_file_path = os.path.join(class_path, file_name)
        try:
            if os.path.exists(dst_directory_path):
                if not os.path.exists(os.path.join(dst_directory_path, 'image00001.jpg')):
                    subprocess.call('rm -r \"{}\"'.format(dst_directory_path), shell=True)
                    print('remove {}'.format(dst_directory_path))
                    os.makedirs(dst_directory_path)
                else:
                    continue
            else:
                # pdb.set_trace()
                os.makedirs(dst_directory_path)
        except:
            print(dst_directory_path)
            continue
        cmd = 'ffmpeg -i \"{}\" -vf scale=-1:240 \"{}/%06d.jpg\"'.format(video_file_path, dst_directory_path)
        print(cmd)
        subprocess.call(cmd, shell=True)
        print('\n')

if __name__ == "__main__":
    # VE8
    # dir_path = "/mnt/server18_hard0/jhjang/AVER/VAANet/ve8raw"  # avi directory
    # dst_dir_path = "/mnt/server18_hard0/jhjang/AVER/VAANet/data/ve8/ve8--imgs"

    # EK6
    dir_path = "/mnt/server18_hard0/jhjang/AVER/VAANet/raw_ek6"  # avi directory
    dst_dir_path = "/mnt/server18_hard0/jhjang/AVER/VAANet/data/ek6/ek6--imgs"


    # dst_dir_path = "/mnt/server18_hard0/jhjang/AVER/CTEN/data/VideoEmotion"
    # dir_path = sys.argv[1]  # avi directory
    # dst_dir_path = sys.argv[2]  # jpg directory
    # dir_path = "/project/data/ekman6/ekman6--mp4"
    # dst_dir_path = "/project/data/ekman6/ekman6--jpg"
    # class_name = sys.argv[1]
    # class_process(dir_path, dst_dir_path, class_name)

    for class_name in os.listdir(dir_path):
        class_process(dir_path, dst_dir_path, class_name)
