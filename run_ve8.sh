CUDA_VISIBLE_DEVICES=0 python main.py --video_path='data/ve8/ve8--imgs' --expr_name=ve8 --annotation_path='tools/annotations/ve8/ve8_01.json' --audio_path='data/ve8/ve8--mp3' --n_classes=8 --debug
CUDA_VISIBLE_DEVICES=5 python main.py --video_path='data/ve8/ve8--imgs' --expr_name=ve8 --annotation_path='tools/annotations/ve8/ve8_01.json' --audio_path='data/ve8/ve8--mp3' --n_classes=8 --debug


