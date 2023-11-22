from PIL import Image
from PIL import ImageFilter
import cv2
import numpy as np

def flou(imgname):
    """
    Cette fonction floutte une image.

    :param int imgname: nom et type de l'immage à modifier ex: "image.png"
    :return: ne retourne rien, mais range l'immage modifier dans le dossier "immages-changed"
    """
    img=Image.open (f'immages-test/{imgname}') #image à changer
    imgchanged=img.filter(ImageFilter.BLUR)  #image apprès changement
    imgchanged.save(f'./images-changed/{imgname}-flouté.png','png')

def monochrome(imgname):
    """
    Cette fonction passe une image en monochrome

    :param imgname: nom et type de l'immage à modifier ex: "image.png"
    :return: ne retourne rien, mais range l'immage modifier dans le dossier "immages-changed"
    """
    img=Image.open (f'immages-test/{imgname}') # image à changer
    imgchanged=img.convert('L') # image apprès changement
    imgchanged.save(f'./images-changed/{imgname}-flouté.png','png')

def dilatation(imgname):
    """
    Cette fonction dilate une image

    :param imgname: nom et type de l'immage à modifier ex: "image.png"
    :return: ne retourne rien, mais range l'immage modifier dans le dossier "immages-changed"
    """
    img = cv2.imread(f'immages-test/{imgname}') # image à changer
    kernel = np.ones((5,5), np.uint8) # propriétée de la dilatation
    imgchanged=cv2.dilate(img, kernel, iterations=1) # image apprès changement
    cv2.imwrite(f'./images-changed/{imgname}-dilatée.png',imgchanged)

def rotate(imgname,angle):
    """
    Cette fonction provoque la rotation d'une image

    :param imgname: nom et type de l'immage à modifier ex: "image.png"
    :param angle: angle de rotation voulue de l'image ex: 180
    :return: ne retourne rien, mais range l'immage modifier dans le dossier "immages-changed"
    """
    img=Image.open (f'immages-test/{imgname}') # image à changer
    imgchanged= img.rotate(angle) # image apprès changement
    imgchanged.save(f'./images-changed/{imgname}-totate-{angle}°.png','png')

def text(imgname,text):
    """
    Cette fonction ajoute du text sur une image

    :param imgname: nom et type de l'immage à modifier ex: image.png
    :param text: text à ajouter sur l'image ex: "ceci est un text"
    :return: ne retourne rien, mais range l'immage modifier dans le dossier "immages-changed"
    """
    img = cv2.imread(f'immages-test/{imgname}') # image à changer
    org = (50, 50) # position du text par rapport au coin superieur gauche
    font = 3 # police d'écriture
    fontScale = 1 # taille du text
    color = (0,0,0) # couleur
    thickness = 2 # épaisseur du trait
    imgchanged= cv2.putText(img, text, org, font,  
                fontScale, color, thickness, cv2.LINE_AA) # image apprès changement
    cv2.imwrite(f'./images-changed/{imgname}-dilatée.png',imgchanged)