import torch
import torch.nn.functional as F
from torchvision import transforms
from PIL import Image
from fastai.vision.all import *
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

model = torch.load("C:\\Users\\matas\\OneDrive\\Stalinis kompiuteris\\Flask_Image_Recognition\\model.pkl", map_location=torch.device('cpu'))

def predict_result(img_path):
    # # Load image
    # img = mpimg.imread(img_path)

    # # Load model
    # learn = load_learner('model')

    # # Make prediction
    # label,_,probs = learn.predict(img)

    # # Create figure using Matplotlib
    # fig = plt.figure()
    # ax = fig.add_subplot() # Add subplot (For multiple images)
    # imgplot = plt.imshow(img) # Add image into plot
    # ax.set_title(label) # Set headline to predicted label

    # # Hide numbers on axes
    # plt.gca().axes.get_yaxis().set_visible(False)
    # plt.gca().axes.get_xaxis().set_visible(False)

    # # Return predicted label and probability
    # return label, probs[label]