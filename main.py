from PIL import Image
from PIL import ImageFilter
import cv2
import numpy as np

angle=180
imgname='téléchargement.jpeg'
img=Image.open (f'immages-test/{imgname}')
imgchanged= img.rotate(angle)
imgchanged.save(f'./images-changed/{imgname}-totate-{angle}°.png','png')