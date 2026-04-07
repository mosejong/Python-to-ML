import pandas as pd
from PIL import Image
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import tensorflow as tf
from tqdm import tqdm
#from tensorflow.keras import Sequential, Input
#from tensorflow.keras.layers import Conv2D, MaxPool2D, Dropout, Dense, GlobalAveragePooling2D

train_df = pd.read_csv("train.csv")
test_df = pd.read_csv("test.csv")
'''     파일 읽어보기
print(train_df.head())
print(test_df.head())
print(train_df.shape, test_df.shape)        (15834, 3) (6786, 2)
print(train_df["label"].nunique())          25

train_img = Image.open("./train/TRAIN_00000.jpg")
test_img = Image.open("./test/TEST_00000.jpg")

print("train size:", train_img.size)        train size: (64, 64)
print("test size:", test_img.size)          test size: (64, 64)
'''
#전처리
le = LabelEncoder()
train_df["label_idx"] = le.fit_transform(train_df["label"])
num_classes = train_df["label_idx"].nunique()

X = train_df['img_path']
y = train_df['label_idx']
test_X = test_df['img_path']

train_data, val_data = train_test_split(train_df, test_size=0.2, random_state=42)



class BirdDataset(Dataset):
    def __init__(self, df, transform=None, is_test=False):
        self.df = df.reset_index(drop=True)
        self.transform = transform
        self.is_test = is_test

    def __len__(self):
        return len(self.df)

    def __getitem__(self, idx):
        img_path = self.df.loc[idx, "img_path"]
        image = Image.open(img_path).convert("RGB")

        if self.transform:
            image = self.transform(image)

        if self.is_test:
            return image

        label = self.df.loc[idx, "label_idx"]
        return image, label
    
train_transform = transforms.Compose([
    transforms.RandomHorizontalFlip(),
    transforms.ToTensor()
])

val_transform = transforms.Compose([
    transforms.ToTensor()
])
train_dataset = BirdDataset(train_data, transform=train_transform)
val_dataset = BirdDataset(val_data, transform=val_transform)
test_dataset = BirdDataset(test_df, transform=val_transform, is_test=True)
''' 잘 됬나 체크
img, label = train_dataset[0]
print(img.shape)        torch.Size([3, 64, 64])
print(label)            13

img = test_dataset[0]
print(img.shape)        torch.Size([3, 64, 64])
'''

train_loader = DataLoader(dataset=train_dataset,batch_size=32,shuffle=True)
val_loader = DataLoader(val_dataset,32,False)
test_loader = DataLoader(test_dataset,32,False)

''' 모델 만들기 CNN배운 것 '''

class CNNModel(nn.Module):
    def __init__(self, num_classes):
        super().__init__()
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=32, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(32, 64, 3, padding=1)
        self.conv3 = nn.Conv2d(64, 128, 3, padding=1)
        self.conv4 = nn.Conv2d(128, 128, 3, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        
        
        self.fc1 = nn.Linear(128 * 16 * 16, 128)
        self.dropout = nn.Dropout(0.3)
        self.fc2 = nn.Linear(128, num_classes)
        
    def forward(self, x):
        x = torch.relu(self.conv1(x))
        x = self.pool(torch.relu(self.conv2(x)))
        
        x = torch.relu(self.conv3(x))
        x = self.pool(torch.relu(self.conv4(x)))
        
        x = torch.flatten(x,1)
        
        x = torch.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.fc2(x)
        
        return x

model = CNNModel(num_classes)

'''
images, labels = next(iter(train_loader))
outputs = model(images)
print(outputs.shape)
'''

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

best_val_loss = float("inf")
patience = 3
counter = 0
epochs = 20

for epoch in range(epochs):
    model.train()
    train_loss = 0.0

    for images, labels in tqdm(train_loader, desc=f"Epoch {epoch+1}/{epochs} [Train]"):
        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        train_loss += loss.item()

    model.eval()
    val_loss = 0.0
    correct = 0
    total = 0

    with torch.no_grad():
        for images, labels in tqdm(val_loader, desc=f"Epoch {epoch+1}/{epochs} [Val]"):
            outputs = model(images)
            loss = criterion(outputs, labels)
            val_loss += loss.item()

            preds = torch.argmax(outputs, dim=1)
            correct += (preds == labels).sum().item()
            total += labels.size(0)

    avg_train_loss = train_loss / len(train_loader)
    avg_val_loss = val_loss / len(val_loader)
    val_acc = correct / total

    print(f"Epoch [{epoch+1}/{epochs}]")
    print(f"Train Loss: {avg_train_loss:.4f}")
    print(f"Val Loss: {avg_val_loss:.4f}")
    print(f"Val Acc: {val_acc:.4f}")

    if avg_val_loss < best_val_loss:
        best_val_loss = avg_val_loss
        counter = 0
        torch.save(model.state_dict(), "best_model.pt")
        print("best model 저장!")
    else:
        counter += 1
        print(f"early stopping counter: {counter}/{patience}")

    if counter >= patience:
        print("Early stopping!")
        break