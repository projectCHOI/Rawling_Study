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

# 사전 학습된 모델 중 EfficientNet B4 모델 사용하기
model = models.efficientnet_b4(weights='IMAGENET1K_V1').to(device)
print(model)

# 학습
optimizer = optim.Adam(model.classifier.parameters(), lr=0.001)

epochs = 10

for epoch in range(epochs):
    for phase in ['train', 'validation']:
        if phase == 'train':
            model.train()
        else:
            model.eval()

        sum_losses = 0
        sum_accs = 0

        for x_batch, y_batch in dataloaders[phase]:
            x_batch = x_batch.to(device)
            y_batch = y_batch.to(device)

            y_pred = model(x_batch)

            loss = nn.CrossEntropyLoss()(y_pred, y_batch)

            if phase == 'train':
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()

            sum_losses = sum_losses + loss.item()

            y_prob = nn.Softmax(1)(y_pred)
            y_pred_index = torch.argmax(y_prob, axis=1)
            acc = (y_batch == y_pred_index).float().sum() / len(y_batch) * 100

            sum_accs = sum_accs + acc.item()

        avg_loss = sum_losses / len(dataloaders[phase])
        avg_acc = sum_accs / len(dataloaders[phase])

        print(f'{phase:10s}: Epoch {epoch+1:4d}/{epochs}, Loss:{avg_loss:.4f}, Accuracy:{avg_acc:.2f}%')

torch.save(model.state_dict(), 'model.h5')

model = models.efficientnet_b4().to(device)

model.classifier = nn.Sequential(
    nn.Linear(1792, 512),
    nn.ReLU(),
    nn.Linear(512, 149)
).to(device)

model.load_state_dict(torch.load('model.h5'))
model.eval()

# 테스트
from PIL import Image

img1 = Image.open('validation/Charmander/0.jpg')
img2 = Image.open('validation/Squirtle/0.jpg')

fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].imshow(img1)
axes[0].axis('off')
axes[1].imshow(img2)
axes[1].axis('off')
plt.show()

img1_input = data_transforms['validation'](img1)
img2_input = data_transforms['validation'](img2)
print(img1_input.shape)
print(img2_input.shape)

test_batch = torch.stack([img1_input, img2_input])
test_batch = test_batch.to(device)
test_batch.shape

y_pred = model(test_batch)
y_pred

y_prob = nn.Softmax(1)(y_pred)
y_prob

probs, indices = torch.topk(y_prob, k=3, axis=-1)       # k = 3 : 3등까지 불러오기 / axis = 1 or -1 무관

probs = probs.cpu().data.numpy()        # 확률
indices = indices.cpu().data.numpy()    # 인덱스

print(probs)
print(indices)

9.9966812e-01
9.9713159e-01

fig, axes = plt.subplots(1, 2, figsize=(12, 6))

axes[0].set_title('{:.2f}% {}, {:.2f}% {}, {:.2f}% {}'.format(
    probs[0, 0] * 100, image_datasets['validation'].classes[indices[0, 0]],
    probs[0, 1] * 100, image_datasets['validation'].classes[indices[0, 1]],
    probs[0, 2] * 100, image_datasets['validation'].classes[indices[0, 2]]
))
axes[0].imshow(img1)
axes[0].axis('off')

axes[1].set_title('{:.2f}% {}, {:.2f}% {}, {:.2f}% {}'.format(
    probs[1, 0] * 100, image_datasets['validation'].classes[indices[1, 0]],
    probs[1, 1] * 100, image_datasets['validation'].classes[indices[1, 1]],
    probs[1, 2] * 100, image_datasets['validation'].classes[indices[1, 2]]
))
axes[1].imshow(img2)
axes[1].axis('off')

plt.show()