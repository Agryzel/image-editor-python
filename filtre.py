from PIL import Image
from PIL import ImageFilter
import cv2
import numpy as np
import logger
import os
import matplotlib.pyplot as plt

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
        logger.log(f"Un effect de flou a été appliquer à {imgname}")

    except Exception as e:
        # En cas d'erreur
        print(f"Une erreur s'est produite lors de l'application du filtre 'flou' à {imgname} : {e}")
        logger.log(f"Une erreur s'est produite lors de l'application du filtre 'flou' à {imgname} : {e}")

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
        logger.log(f"{imgname} à été mise en noir et blanc")

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
        logger.log(f"Un effect de dilatation a été appliquer à {imgname}")

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
        logger.log(f"Une rotation de {angle}° a été appliquer à {imgname}")

    except Exception as e:
        print(f"Une erreur s'est produite lors de l'application du filtre 'rotate' à {imgname} : {e}")
        logger.log(f"Une erreur s'est produite lors de l'application du filtre 'rotate' à {imgname} : {e}")


def redimension(imgname,size):
    try:
        # Essayer d'ouvrir l'image et de redimensionner selon les dimensions spécifiées
        img = Image.open(f'immages-test/{imgname}')
        height = img.height
        width = img.width
        new_width = width * size
        new_height = height * size
        imgchanged = img.resize((new_width, new_height))
        imgchanged.save(f'./images-changed/{imgname}', 'png')
        logger.log(f"Un aggrandissement X{size} a été appliquer à {imgname}")


    except Exception as e:
        print(f"Une erreur s'est produite lors de l'application du filtre 'redimension' à {imgname} : {e}")
        logger.log(f"Une erreur s'est produite lors de l'application du filtre 'redimension' à {imgname} : {e}")

def multiFiltre():
    """
        :param imgname: nom et type de l'immage à modifier ex: "image.png"
    """
    try:
        # Initialisation d'une liste pour stocker les noms d'images sélectionnées
        tabPic = []
        
        # Demander à l'utilisateur quel filtre il veut appliquer
        askFiltre = input("Quel filtre veux-tu appliquer à tes images ? \n flou \n monochrome \n dilatation \n rotate \n redimension \n")
    
        # Vérifier si le filtre choisi est valide
        if askFiltre in ["flou", "monochrome", "dilatation", "rotate", "redimension"]:
            # Demander à l'utilisateur les noms des images à traiter
            askPic = input("Donne moi le nom avec le format de l'image que tu veux cibler \n Si tu as fini de sélectionner toutes tes images, envoie rien \n ")
        
            # Continuer à demander les noms des images tant que l'utilisateur en fournit
            while askPic != "":
                tabPic.append(askPic)
                askPic = input("Donne moi le nom avec le format de l'image que tu veux cibler \n Si tu as fini de sélectionner toutes tes images, envoie rien \n ")
        
            # Parcourir la liste des images sélectionnées
            for i in range(len(tabPic)):
                # Appliquer le filtre choisi à chaque image
                if askFiltre == "flou":
                    flou(tabPic[i])
                
                elif askFiltre == "monochrome":
                    monochrome(tabPic[i])
                
                elif askFiltre == "dilatation":
                    dilatation(tabPic[i])
                
                elif askFiltre == "rotate":
                    # Demander à l'utilisateur l'angle de rotation
                    angle = int(input("Quel angle de rotation veux-tu pour les images ? "))
                    rotate(tabPic[i], angle)
                
                elif askFiltre == "redimension":
                    redimension(tabPic[i])
    except Exception as e:
        logger.log(f"Une erreur s'est produite lors de l'application du filtre {askFiltre} à la liste d'images : {tabPic} : {e}")
        print(f"Une erreur s'est produite lors de l'application du filtre {askFiltre} à la liste d'images : {tabPic} : {e}")


def text(imgname,text):
    """
    Cette fonction ajoute du text sur une image

    :param imgname: nom et type de l'immage à modifier ex: image.png
    :param text: text à ajouter sur l'image ex: "ceci est un text"
    :return: ne retourne rien, mais range l'immage modifier dans le dossier "immages-changed"
    """
    try:
        img = cv2.imread(f'immages-test/{imgname}') # image à changer
        org = (50, 50) # position du text par rapport au coin superieur gauche
        font = 3 # police d'écriture
        fontScale = 1 # taille du text
        color = (0,0,0) # couleur
        thickness = 2 # épaisseur du trait
        imgchanged= cv2.putText(img, text, org, font, fontScale, color, thickness, cv2.LINE_AA) # image apprès changement
        cv2.imwrite(f'./images-changed/{imgname}',imgchanged)
    except Exception as e:
        logger.log(f"Une erreur s'est produite lors de l'ajout de texte à l'image {imgname} : {e}")
        print(f"Une erreur s'est produite lors de l'ajout de texte à l'image {imgname} : {e}")

def gif(doc):
    """
    :param doc est le chemin du dossier qui contient les images a assembler
    """
    try:
        images = []

        # Lire chaque fichier dans le dossier spécifié
        for filename in os.listdir(doc):
            img_path = os.path.join(doc, filename)
            images.append(Image.open(str(img_path)))

        # Sauvegarder les images en tant que GIF
        images[0].save('images-changed/paysage.gif', save_all=True, append_images=images[1:], duration=500, loop=0)

        logger.log(f"Le gif a bien été crée avec les images : {images}")


    except Exception as e:
        # En cas d'erreur, enregistrer le message d'erreur
        logger.log(f"Une erreur s'est produite lors de l'execution du programme de gif : {e}")
        print(f"Une erreur s'est produite lors de l'execution du programme de gif : {e}")

def faceDetector(imgname):
    try:
        # Chargement de l'image depuis le fichier spécifié
        img = cv2.imread(imgname)

        # Conversion de l'image en niveaux de gris
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Chargement du classificateur en cascade pour la détection de visages
        face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

        # Détection des visages dans l'image en niveaux de gris
        face = face_classifier.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40))

        # Dessine des rectangles autour des visages détectés dans l'image originale
        for (x, y, w, h) in face:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 4)

        # Conversion de l'image de l'espace de couleur BGR à RGB pour l'affichage avec matplotlib
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Affichage de l'image résultante avec les rectangles entourant les visages
        plt.figure(figsize=(20,10))
        plt.imshow(img_rgb)
        plt.axis('off')
        plt.show()

    except Exception as e:
        # Gestion des exceptions, affichage de l'erreur
        print(f"Une erreur s'est produite lors de la detection du visage : {e}")

def aquarelle(imgname):
    imgname="téléchargement (1).jpeg"
    img = cv2.imread(f'immages-test/{imgname}')
    kernel = np.ones((5, 5), np.uint8)
    imgchanged = cv2.stylization(img)
    cv2.imwrite(f'./images-changed/{imgname}', imgchanged)

