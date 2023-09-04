python train.py --config config_v2.json \
    --input_wavs_dir /home/stud_vantuan/share_with_150/data_CD/train_CD92/wav \
    --input_training_file CD92/training.txt \
    --input_validation_file CD92/validation.txt \
    --checkpoint_path cp_cd92_hifigan \
    --training_epochs 3200 