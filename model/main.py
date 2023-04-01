import torch
import torch.nn.functional as F
from torchvision import transforms
from PIL import Image

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

for i in range(0,20):
  #Load random image
  randomIndex = random.randint(0, len(get_image_files(imagePath))-1)
  img = mpimg.imread(get_image_files(imagePath)[randomIndex])
  #Put into Model
  label,_,probs = learn.predict(img)

  #Create Figure using Matplotlib
  fig = plt.figure()
  ax = fig.add_subplot() #Add Subplot (For multiple images)
  imgplot = plt.imshow(img) #Add Image into Plot
  ax.set_title(label) #Set Headline to predicted label

  #Hide numbers on axes
  plt.gca().axes.get_yaxis().set_visible(False)
  plt.gca().axes.get_xaxis().set_visible(False)