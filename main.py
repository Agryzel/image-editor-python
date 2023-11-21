from PIL import Image
from PIL import ImageFilter
import cv2
import numpy as np

imgname='téléchargement.jpeg'
img = cv2.imread(f'immages-test/{imgname}')
kernel = np.ones((5,5), np.uint8)
imgchanged=cv2.dilate(img, kernel, iterations=1)
cv2.imwrite('./images-changed/',imgchanged)