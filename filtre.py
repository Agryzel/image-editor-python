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
    try:
        # Essayer d'ouvrir l'image et d'appliquer le filtre flou
        img = Image.open(f'immages-test/{imgname}')
        imgchanged = img.filter(ImageFilter.BLUR)
        imgchanged.save(f'./images-changed/{imgname}-floute.png', 'png')
    except Exception as e:
        # En cas d'erreur
        print(f"Une erreur s'est produite lors de l'application du filtre 'flou' à {imgname} : {e}")

def monochrome(imgname):
    """
    Cette fonction passe une image en monochrome

    :param imgname: nom et type de l'immage à modifier ex: "image.png"
    :return: ne retourne rien, mais range l'immage modifier dans le dossier "immages-changed"
    """
    try:
        # Essayer d'ouvrir l'image et de la convertir en monochrome
        img = Image.open(f'immages-test/{imgname}')
        imgchanged = img.convert('L')
        imgchanged.save(f'./images-changed/{imgname}-monochrome.png', 'png')
    except Exception as e:
        print(f"Une erreur s'est produite lors de l'application du filtre 'monochrome' à {imgname} : {e}")

def dilatation(imgname):
    """
    Cette fonction dilate une image

    :param imgname: nom et type de l'immage à modifier ex: "image.png"
    :return: ne retourne rien, mais range l'immage modifier dans le dossier "immages-changed"
    """

    try:
        # Essayer de lire l'image avec OpenCV et d'appliquer la dilatation
        img = cv2.imread(f'immages-test/{imgname}')
        kernel = np.ones((5, 5), np.uint8)
        imgchanged = cv2.dilate(img, kernel, iterations=1)
        cv2.imwrite(f'./images-changed/{imgname}-dilatee.png', imgchanged)
    except Exception as e:
        print(f"Une erreur s'est produite lors de l'application du filtre 'dilatation' à {imgname} : {e}")


def rotate(imgname, angle):
    """
    Cette fonction provoque la rotation d'une image

    :param imgname: nom et type de l'immage à modifier ex: "image.png"
    :param angle: angle de rotation voulue de l'image ex: 180
    :return: ne retourne rien, mais range l'immage modifier dans le dossier "immages-changed"
    """
    try:
        # Essayer d'ouvrir l'image et de la faire tourner selon l'angle spécifié
        img = Image.open(f'immages-test/{imgname}')
        imgchanged = img.rotate(angle)
        imgchanged.save(f'./images-changed/{imgname}-rotate-{angle}°.png', 'png')
    except Exception as e:
        print(f"Une erreur s'est produite lors de l'application du filtre 'rotate' à {imgname} : {e}")


def redimension(imgname):
    try:
        # Essayer d'ouvrir l'image et de redimensionner selon les dimensions spécifiées
        img = Image.open(f'immages-test/{imgname}')
        askLongueur = input("Saisir la longueur de l'image ")
        askLargeur = input("Saisir la largeur de l'image ")
        imgchanged = img.resize((int(askLongueur), int(askLargeur)))
        imgchanged.save(f'./images-changed/{imgname}-redimensionne.png', 'png')
    except Exception as e:
        print(f"Une erreur s'est produite lors de l'application du filtre 'redimension' à {imgname} : {e}")

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
                redimension(tabPic[i])

multiFiltre()

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
