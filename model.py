import torch
import torch.nn.functional as F
from torchvision import transforms
from PIL import Image
from fastai.vision.all import *
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

model = torch.load("./model.pkl",
                   map_location=torch.device('cpu'))


def predict_result(image_path):
    img = mpimg.imread(image_path)
    label, _, probs = model.predict(img)
    return label
