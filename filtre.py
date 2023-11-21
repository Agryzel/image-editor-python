from PIL import Image
from PIL import ImageFilter
import cv2
import numpy as np

def flou(imgname):
    img=Image.open (f'immages-test/{imgname}')
    imgchanged=img.filter(ImageFilter.BLUR)
    imgchanged.save(f'./images-changed/{imgname}-flouté.png','png')

def monochrome(imgname):
    img=Image.open (f'immages-test/{imgname}')
    imgchanged=img.convert('L')
    imgchanged.save(f'./images-changed/{imgname}-flouté.png','png')

def dilatation(imgname):
    imgname='téléchargement.jpeg'
    img = cv2.imread(f'immages-test/{imgname}')
    kernel = np.ones((5,5), np.uint8)
    imgchanged=cv2.dilate(img, kernel, iterations=1)
    cv2.imwrite(f'./images-changed/{imgname}-dilatée.png',imgchanged)