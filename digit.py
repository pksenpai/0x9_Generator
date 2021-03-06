from torchvision import models, transforms
import torch
from PIL import Image
import torch.nn as nn
import matplotlib
import matplotlib.pyplot as plt
import streamlit as st

def denorm(x):
      out = (x + 1) / 2
      return out.clamp(0, 1)

latent_size = 64
batch_size = 100

def new():
  G = torch.load("w1.pth", map_location = "cpu")
  G.eval()	
  device = torch.device('cpu')
  G.to(device);
  y = G(torch.randn(1, latent_size))
  gen_imgs = denorm(y.reshape((-1, 32,32)).detach())

  plt.imshow(gen_imgs[0], cmap='plasma');
  plt.savefig("temp.png")

new()

def newex():
  Gex = torch.load("w2.pth", map_location = "cpu")
  Gex.eval()	
  deviceex = torch.device('cpu')
  Gex.to(deviceex);
  yex = Gex(torch.randn(1, latent_size))
  gen_imgex = denorm(yex.reshape((-1, 32,32)).detach())
  plt.imshow(gen_imgex[0], cmap='jet');
  plt.savefig("tempex.png")

newex()

st.title("0x9 Generator")
st.write("This is a generative adversarial network based app, trained on the MNIST dataset for 400 epochs")
st.write("In case no digit pops up, please reload the app")
st.image(["temp.png","tempex.png"], width = 300)

st.write("")
st.subheader("Progress Grid:")
st.write("")
st.write("After 10 epochs: ")
st.markdown("![10](https://user-images.githubusercontent.com/52780573/102694930-38a0af80-424a-11eb-9031-ab9da9602d81.png)")
st.write("After 100 epochs: ")
st.markdown("![fake_images-0100](https://user-images.githubusercontent.com/52780573/102694936-40f8ea80-424a-11eb-8e05-0308be7a9d0e.png)")
st.write("After 200 epochs: ")
st.markdown("![fake_images-0200](https://user-images.githubusercontent.com/52780573/102694938-46563500-424a-11eb-83db-a1cd21a57c39.png)")
st.write("After 300 epochs: ")
st.markdown("![300](https://user-images.githubusercontent.com/52780573/102694939-49512580-424a-11eb-9902-52ab7547a704.png)")
st.write("After 399 epochs: ")
st.markdown("![400](https://user-images.githubusercontent.com/52780573/102694943-4bb37f80-424a-11eb-9b5b-214d07ffb7c5.png)")



