from __future__ import print_function, division
import os
import sys

def class_process(dir_path, class_name):
    class_path = os.path.join(dir_path, class_name)
    if not os.path.isdir(class_path):
        return
    for file_name in os.listdir(class_path):
        video_dir_path = os.path.join(class_path, file_name)
        if not os.path.isdir(video_dir_path) or 'n_frames' in os.listdir(video_dir_path):
            print('Skip: {}'.format(video_dir_path))
            continue
        image_indices = []
        print('Processing: {}'.format(video_dir_path))
        for image_file_name in os.listdir(video_dir_path):
            if '.jpg' not in image_file_name or image_file_name[0]=='.':
                print(image_file_name)
                os.remove(os.path.join(video_dir_path, image_file_name))
                continue
            image_indices.append(int(image_file_name[:6]))

        # video level
        if len(image_indices) < 16:
            print("Insufficient image files: ", video_dir_path)
            print(len(image_indices))
            n_frames = 0
        else:
            image_indices.sort(reverse=True)
            n_frames = image_indices[0]
            print('N frames: ', n_frames)
        with open(os.path.join(video_dir_path, 'n_frames'), 'w+') as dst_file:
            dst_file.write(str(n_frames))


if __name__ == "__main__":
    # dir_path = "/home/ubuntu/private/project/vaanet/ve8--imgs"
    # class_name = sys.argv[1]
    # class_process(dir_path, class_name)

    # dir_path = "/mnt/server18_hard0/jhjang/AVER/VAANet/data/ve8/ve8--imgs"  # avi directory
    dir_path = "/mnt/server18_hard0/jhjang/AVER/VAANet/data/ek6/ek6--imgs"  # avi directory


    # dst_dir_path = "/mnt/server18_hard0/jhjang/AVER/CTEN/data/VideoEmotion" # jpg directory
    # dir_path = "/project/data/ekman6/ekman6--mp4"
    # dst_dir_path = "/project/data/ekman6/ekman6--jpg"
    # class_name ="Anger"
    # class_process(dir_path, dst_dir_path, class_name)
    for class_name in os.listdir(dir_path):
        # import pdb; pdb.set_trace()
        class_process(dir_path, class_name)
