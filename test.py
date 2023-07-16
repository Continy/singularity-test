import cv2
import glob
import numpy as np
import os
import sys
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision
import torchvision.transforms as transforms
from PIL import Image
from torch.autograd import Variable
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, utils
from torchvision.utils import save_image

if os.path.exists('result') is False:
    os.mkdir('result')
if os.path.exists('datasets') is False:
    flag = False
    print('Please put the data in the data folder')

# read the image
path = 'datasets/abandonedfactory/Easy/P001/image_left/'
files = glob.glob(path + '*.png')
files.sort()
for idx, file in enumerate(files):
    #torch加高斯噪声，标准差为0.1，保存
    img = cv2.imread(file)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = torch.from_numpy(img)
    img = img.permute(2, 0, 1)
    img = img.unsqueeze(0)
    noise = torch.randn(img.size()) * 0.1
    noisy_img = img + noise
    noisy_img = noisy_img.squeeze(0)
    noisy_img = noisy_img.permute(1, 2, 0)
    noisy_img = noisy_img.numpy()
    noisy_img = cv2.cvtColor(noisy_img, cv2.COLOR_RGB2BGR)
    cv2.imwrite('result/noisy_img' + str(idx) + '.png', noisy_img)