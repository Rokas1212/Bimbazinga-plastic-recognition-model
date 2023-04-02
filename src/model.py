import torch
import torch.nn.functional as F
from torchvision import transforms
from PIL import Image
from fastai.vision.all import *
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

model = torch.load("src\model.pkl",
                   map_location=torch.device('cpu'))


def predict_result(file):
    img = mpimg.imread(file)
    label, _, probs = model.predict(img)
    return label

