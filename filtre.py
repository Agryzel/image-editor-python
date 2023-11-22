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

def rotate(imgname,angle):
    img=Image.open (f'immages-test/{imgname}')
    imgchanged= img.rotate(angle)
    imgchanged.save(f'./images-changed/{imgname}-totate-{angle}°.png','png')

def redimention(imgname):
    img = Image.open (f'immages-test/{imgname}')
    imgchanged = img.resize((256, 256))
    imgchanged.save(f'./images-changed/{imgname}-flouté.png','png')

def multiFiltre():
    tabPic = []
    askFiltre = input("Quel filtre veux-tu appliquer à tes images ? \n flou \n monochrome \n dilatation \n rotate \n redimension \n")
    
    if askFiltre in ["flou", "monochrome", "dilatation", "rotate", "redimension"]:
        askPic = input("Donne moi le nom avec le format de l'image que tu veux cibler \n Si tu as fini de sélectionner toutes tes images, envoie rien \n ")
        
        while askPic != "":
            tabPic.append(askPic)
            askPic = input("Donne moi le nom avec le format de l'image que tu veux cibler \n Si tu as fini de sélectionner toutes tes images, envoie rien \n ")
        
        for i in range(len(tabPic)):
            if askFiltre == "flou":
                flou(tabPic[i])
                
            elif askFiltre == "monochrome":
                monochrome(tabPic[i])
                
            elif askFiltre == "dilatation":
                dilatation(tabPic[i])
                
            elif askFiltre == "rotate":
                angle = int(input("Quel angle de rotation veux-tu pour les images ? "))
                rotate(tabPic[i], angle)
                
            elif askFiltre == "redimension":
                redimention(tabPic[i])

multiFiltre()
