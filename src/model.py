import torch
import torch.nn.functional as F
from torchvision import transforms
from PIL import Image
from fastai.vision.all import *
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

model = torch.load("C:\\Users\\matas\\OneDrive\\Stalinis kompiuteris\\modelGUI\\Bimbazinga-plastic-recognition-model\\src\\model.pkl", map_location=torch.device('cpu'))

def predict_result(img_path):
    model.fit(img_path)