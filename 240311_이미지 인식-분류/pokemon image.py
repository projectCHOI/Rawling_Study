import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
from torchvision import datasets, models, transforms
from torch.utils.data import DataLoader

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

import os

os.environ['KAGGLE_USERNAME'] = 'yoonsuk93choi' # username
os.environ['KAGGLE_KEY'] = '359365bf6e538ea03289da614cdec80a' # key

# !kaggle datasets download -d thedagger/pokemon-generation-one
# !unzip -q pokemon-generation-one.zip

# !kaggle datasets download -d hlrhegemony/pokemon-image-dataset
# !unzip -q pokemon-image-dataset.zip

# # 디렉토리 이름 변경
# !mv dataset train

# !mv images validation

# # 중복된 dataset 디렉토리 삭제
# !rm -rf train/dataset

import os
print(os.listdir())  # 현재 디렉토리의 파일 목록을 출력합니다.

train_labels = os.listdir('train')
len(train_labels)

val_labels = os.listdir('validation')
len(val_labels)

import shutil

for val_label in val_labels:
    if val_label not in train_labels:
        shutil.rmtree(os.path.join('validation', val_label))

val_labels = os.listdir('validation')
len(val_labels)

for train_label in train_labels:
    if train_label not in val_labels:
        print(train_label)
        os.makedirs(os.path.join('validation', train_label), exist_ok=True)

val_labels = os.listdir('validation')
print(len(val_labels))

# 데이터 변환 및 데이터셋 및 DataLoader 생성
data_transforms = {
    'train': transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.RandomAffine(0, shear=10, scale=(0.8, 1.2)),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor()
    ]),
    'validation': transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor()
    ])
}

image_datasets = {
    'train': datasets.ImageFolder('train', data_transforms['train']),
    'validation': datasets.ImageFolder('validation', data_transforms['validation'])
}

dataloaders = {
    'train': DataLoader(
        image_datasets['train'],
        batch_size=32,
        shuffle=True
    ),
    'validation': DataLoader(
        image_datasets['validation'],
        batch_size=32,
        shuffle=False
    )
}

imgs, labels = next(iter(dataloaders['train']))

fig, axes = plt.subplots(4, 8, figsize=(20, 10))

for img, label, ax in zip(imgs, labels, axes.flatten()):
    ax.set_title(label.item())
    ax.imshow(img.permute(1, 2, 0))
    ax.axis('off')

# 클래스 이름 확인하기
print(image_datasets['train'].classes)
print(image_datasets['train'].classes[0])
