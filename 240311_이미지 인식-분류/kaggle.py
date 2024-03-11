import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
from torchvision import datasets, models, transforms
from torch.utils.data import DataLoader
import os

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Kaggle API 인증 정보 설정
os.environ['KAGGLE_USERNAME'] = 'yoonsuk93choi' # username
os.environ['KAGGLE_KEY'] = '359365bf6e538ea03289da614cdec80a' # key

# 데이터셋 다운로드
# !pip install kaggle
import kaggle

# pokemon-generation-one 데이터셋 다운로드 및 압축 해제
kaggle.api.authenticate()
kaggle.api.dataset_download_files('thedagger/pokemon-generation-one', unzip=True)

# pokemon-image-dataset 데이터셋 다운로드 및 압축 해제
kaggle.api.dataset_download_files('hlrhegemony/pokemon-image-dataset', unzip=True)

# 디렉토리 이름 변경
os.rename('dataset', 'train')
os.rename('images', 'validation')

# 중복된 dataset 디렉토리 삭제
import shutil
shutil.rmtree('train/dataset')

# 현재 디렉토리의 파일 목록 출력
print(os.listdir())  

# train 디렉토리 내 레이블 수 확인
train_labels = os.listdir('train')
print(len(train_labels))
