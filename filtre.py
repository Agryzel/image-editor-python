from PIL import Image
from PIL import ImageFilter
import cv2
import numpy as np

def flou(imgname):
    """
    Cette fonction floutte une image.

    :param imgname: nom et type de l'immage à modifier ex: image.png
    :return: ne retourne rien, mais range l'immage modifier dans le dossier "immages-changed"
    """
    img=Image.open (f'immages-test/{imgname}')
    imgchanged=img.filter(ImageFilter.BLUR)
    imgchanged.save(f'./images-changed/{imgname}-flouté.png','png')

def monochrome(imgname):
    """
    Cette fonction passe une image en monochrome

    :param imgname: nom et type de l'immage à modifier ex: image.png
    :return: ne retourne rien, mais range l'immage modifier dans le dossier "immages-changed"
    """
    img=Image.open (f'immages-test/{imgname}')
    imgchanged=img.convert('L')
    imgchanged.save(f'./images-changed/{imgname}-flouté.png','png')

def dilatation(imgname):
    """
    Cette fonction dilate une image

    :param imgname: nom et type de l'immage à modifier ex: image.png
    :return: ne retourne rien, mais range l'immage modifier dans le dossier "immages-changed"
    """
    img = cv2.imread(f'immages-test/{imgname}')
    kernel = np.ones((5,5), np.uint8)
    imgchanged=cv2.dilate(img, kernel, iterations=1)
    cv2.imwrite(f'./images-changed/{imgname}-dilatée.png',imgchanged)

def rotate(imgname,angle):
    """
    Cette fonction provoque la rotation d'une image

    :param imgname: nom et type de l'immage à modifier ex: image.png
    :param angle: angle de rotation voulue de l'image ex: 180
    :return: ne retourne rien, mais range l'immage modifier dans le dossier "immages-changed"
    """
    img=Image.open (f'immages-test/{imgname}')
    imgchanged= img.rotate(angle)
    imgchanged.save(f'./images-changed/{imgname}-totate-{angle}°.png','png')

def text(imgname,text):
    """
    Cette fonction ajoute du text sur une image

    :param imgname: nom et type de l'immage à modifier ex: image.png
    :param text: text à ajouter sur l'image ex: "ceci est un text"
    :return: ne retourne rien, mais range l'immage modifier dans le dossier "immages-changed"
    """
    img = cv2.imread(f'immages-test/{imgname}')
    org = (50, 50) 
    font = 3
    fontScale = 1
    color = (0,0,0) 
    thickness = 2
    imgchanged = cv2.putText(img, text, org, font,  
                   fontScale, color, thickness, cv2.LINE_AA) 
    cv2.imwrite(f'./images-changed/{imgname}-dilatée.png',imgchanged)