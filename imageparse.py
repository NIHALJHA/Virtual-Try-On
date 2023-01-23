import torch
import torchvision
from torchvision.io import read_image
from torchvision.utils import make_grid
import cv2
from PIL import Image


# from skimage import io
 
# img = io.imread(r"C:\Users\8874n\Downloads\HR-VITON-main\BE_Major_Project\HR-VITON-main\data\train\image-parse-v3\00000_00.png")
# io.imshow(img)

class abn:
    def segmap123():
        img = Image.open(r"C:\Users\8874n\Downloads\HR-VITON-main\BE_Major_Project\HR-VITON-main\data\train\image-parse-v3\00000_00.png")
        img.show()
        img1 = Image.open(r"C:\Users\8874n\Downloads\HR-VITON-main\BE_Major_Project\HR-VITON-main\data\train\image-parse-v3\00001_00.png")
        img1.show()
        img2 = Image.open(r"C:\Users\8874n\Downloads\HR-VITON-main\BE_Major_Project\HR-VITON-main\data\train\image-parse-v3\00002_00.png")
        img2.show()
        img3 = Image.open(r"C:\Users\8874n\Downloads\HR-VITON-main\BE_Major_Project\HR-VITON-main\data\train\image-parse-v3\00003_00.png")
        img3.show()
        img4 = Image.open(r"C:\Users\8874n\Downloads\HR-VITON-main\BE_Major_Project\HR-VITON-main\data\train\image-parse-v3\00010_00.png")
        img4.show()
        img5 = Image.open(r"C:\Users\8874n\Downloads\HR-VITON-main\BE_Major_Project\HR-VITON-main\data\train\image-parse-v3\00005_00.png")
        img5.show()
        img6 = Image.open(r"C:\Users\8874n\Downloads\HR-VITON-main\BE_Major_Project\HR-VITON-main\data\train\image-parse-v3\00011_00.png")
        img6.show()
        img7 = Image.open(r"C:\Users\8874n\Downloads\HR-VITON-main\BE_Major_Project\HR-VITON-main\data\train\image-parse-v3\00007_00.png")
        img7.show()
        img8 = Image.open(r"C:\Users\8874n\Downloads\HR-VITON-main\BE_Major_Project\HR-VITON-main\data\train\image-parse-v3\00012_00.png")
        img8.show()
    # a.show()
    # make grid from the input images
    # this grid contain 4 columns and 1 row
    # Grid = make_grid([a, b, c, d,e,f,g,h],nrow=3)
    
    # display result
    # img = torchvision.transforms.ToPILImage()(a)
    # img.show()









# segmap123()
# 


# import required library

  
# read images from computer
