CUDA_VISIBLE_DEVICES=5 python main.py --video_path='data/ek6/ek6--imgs' --expr_name=ek6 --annotation_path='tools/annotations/ek6/ek6_01.json' --audio_path='data/ek6/ek6--mp3' --n_classes=6 --debug
CUDA_VISIBLE_DEVICES=0 python main.py --video_path='data/ek6/ek6--imgs' --expr_name=ek6 --annotation_path='tools/annotations/ek6/ek6_01.json' --audio_path='data/ek6/ek6--mp3' --n_classes=6 --debug


