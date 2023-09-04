import random
import glob
import os
import librosa
from tqdm.auto import tqdm

random.seed(1234)

shortest_duration = 1 # 1 second

wav_path = '/home/stud_vantuan/share_with_150/data_CD/train_CD92/wav'
all_wavs = os.listdir(wav_path)

wavs = []

for wav in tqdm(all_wavs, desc="Checking wavs..."):
    w, sr = librosa.load(wav, sr=None)
    if w.shape[0] / sr >= shortest_duration:
        wavs.append(wav)

print("Keep {}%".format(len(wavs) / len(all_wavs)))

random.shuffle(wavs)

train_ratio = 0.95
train_len = round(len(wavs) * train_ratio)

train_wavs = wavs[:train_len]
valid_wavs = wavs[train_len:]



train_name = [i.rsplit('.', 1)[0] + '|' for i in train_wavs]
valid_name = [i.rsplit('.', 1)[0] + '|' for i in valid_wavs]

with open('CD92/training.txt', 'w') as f:
    f.write('\n'.join(train_name))

with open('CD92/validation.txt', 'w') as f:
    f.write('\n'.join(valid_name))