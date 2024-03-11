import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
from torchvision import datasets, models, transforms
from torch.utils.data import DataLoader
import os
import shutil

# Set device for PyTorch
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Define paths for training and validation datasets
TRAIN_DATA_PATH = "train"
VALIDATION_DATA_PATH = "validation"

# Ensure dataset directories exist (you should modify this according to your local setup)
# For example, if your datasets are not already organized, you should manually set them up or write code to do so
assert os.path.exists(TRAIN_DATA_PATH), f"Training data folder {TRAIN_DATA_PATH} does not exist."
assert os.path.exists(VALIDATION_DATA_PATH), f"Validation data folder {VALIDATION_DATA_PATH} does not exist."

# Data transformations
data_transforms = {
    'train': transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.RandomAffine(0, shear=10, scale=(0.8, 1.2)),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
    ]),
    'validation': transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
    ]),
}

# Image datasets
image_datasets = {
    'train': datasets.ImageFolder(TRAIN_DATA_PATH, data_transforms['train']),
    'validation': datasets.ImageFolder(VALIDATION_DATA_PATH, data_transforms['validation']),
}

# Data loaders
dataloaders = {
    'train': DataLoader(image_datasets['train'], batch_size=32, shuffle=True),
    'validation': DataLoader(image_datasets['validation'], batch_size=32, shuffle=False),
}
