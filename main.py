from colorama import *
import logger
from PIL import Image, ImageFilter
import cv2
import sys
import numpy as np
import os

args = sys.argv[1:]
filters = sys.argv[1:]
input_folder = 'immages-test/'
output_folder = './images-changed/'

def commandLine():

    print(sys.argv)

    def flou(imgname):
        img=Image.open (f'immages-test/{imgname}')
        imgchanged=img.filter(ImageFilter.BLUR)
        imgchanged.save(f'./images-changed/{imgname}-flouté.png','png')

    def monochrome(imgname):
        img=Image.open (f'immages-test/{imgname}')
        imgchanged=img.convert('L')
        imgchanged.save(f'./images-changed/{imgname}-black_white.png','png')

    def dilatation(imgname):
        img = cv2.imread(f'immages-test/{imgname}')
        kernel = np.ones((5,5), np.uint8)
        imgchanged=cv2.dilate(img, kernel, iterations=1)
        cv2.imwrite(f'./images-changed/{imgname}-dilatée.png',imgchanged)

    def rotate(imgname,angle):
        img=Image.open (f'immages-test/{imgname}')
        imgchanged= img.rotate(angle)
        imgchanged.save(f'./images-changed/{imgname}-rotate-{angle}°.png','png')

    def text(imgname,text):
        img = cv2.imread(f'immages-test/{imgname}')
        org = (50, 50) 
        font = 3
        fontScale = 1
        color = (0,0,0) 
        thickness = 2
        imgchanged = cv2.putText(img, text, org, font, fontScale, color, thickness, cv2.LINE_AA) 
        cv2.imwrite(f'./images-changed/{imgname}-written.png',imgchanged)

    def redimension(imgname):
        try:
            img = Image.open(f'immages-test/{imgname}')
            askLongueur = input("Saisir la longueur de l'image ")
            askLargeur = input("Saisir la largeur de l'image ")
            imgchanged = img.resize((int(askLongueur), int(askLargeur)))
            imgchanged.save(f'./images-changed/{imgname}-redimensionne.png', 'png')
        except Exception as e:
            print(f"Une erreur s'est produite lors de l'application du filtre 'redimension' à {imgname} : {e}")

    if args[0] == '-log':
                logger.display_log()
                print(args)

    elif "--help" in args:
        if len(args) > 2:
            print('Invalid number of arguments')

        if len(args) == 1:
            input(f"{Fore.GREEN}Voici le support d'aide pour l'image editor. \n Sur quelle categorie veux tu être aider ? \n - Filtres \n {Style.RESET_ALL} ")
        if len(args) == 2:
            if args[1] == 'filtres':
                input(f"Nous proposons plusieurs filtres et effets : \n - Flou \n - Monochrome \n - Dilatation \n - Rotate \n - Redimension \n")
            else:
                print("La commande que vous venez d'effectuer n'existe pas \n Utilisez la commande -help filtre")
        if len(args) == 3:
            if args[2] == 'flou':
                print(f"Le filtre flou applique un effet de flou simple sur l'image choisi")
                
            elif args[2] == 'monochrome':
                print(f"Le filtre monochrome rend l'image choisi en noir et blanc ")
                
            elif args[2] == 'dilatation':
                print(f"Le filtre dilatation applique un effet grossisement et d'étalement sur l'image choisi")
                
            elif args[2] == 'rotate':
                print(f"L'effet rotate est une rotation de l'image avec le degré que vous souhaitez ")
                
            elif args[2] == 'redimension':
                print(f"La redimension permet de modifier la taille de l'image choisi")
                
            else:
                print("La commande que vous venez d'effectuer n'existe pas \n Utilisez la commande -help filtre")
        else:
            print("La commande que vous venez d'effectuer n'existe pas \n Utilisez la commande -help")
        
    elif "--filters" in filters: #vérifie si un filtre veut etre appliqué
        appliedfilters=[] #stocke les filtres donnés en argument
        for elements in filters: #parcoure les arguments
            index_element = filters.index(elements) #stocke l'index de l'argument en cours d'iteration
            if elements == '--filters': #si on est dans les filtres
                filterlist = filters[index_element+1].split('&') #récupère un tableau des filtres donnés après --filters
                for i in filterlist: #boucle sur les filtres
                    filtre = i.split(':') #regarde la partie avant les : si il y en a (pour rotation, redimension,)
                    if filtre[0] == 'flou':
                        appliedfilters.append('flou')
                    if filtre[0] == 'gray':
                        appliedfilters.append('monochrome')
                    if filtre[0] == 'rotate':
                        appliedfilters.append(('rotate',filtre[1]))
                    if filtre[0] == 'dilate':
                        appliedfilters.append('dilatation')
                    if filtre[0] == 'modify_size':
                       appliedfilters.append(('modify_size',filtre[1]))
                    if filtre[0] == 'text':
                        appliedfilters.append('text',filtre[1])
                    if filtre[0] == 'aquarelle':
                        appliedfilters.append('aquarelle')
            if elements == '--i':
                image = filter[index_element+1]
            if elements == '--o':
                output_folder = filter[index_element+1]

        #change image
        for j in appliedfilters:
            if j == 'flou':
                flou(image)
            if j == 'gray':
                monochrome(image)
            if j[0] == 'rotate':
                rotation(image,j[1])
            if j == 'dilate':
                dilatation(image)
            if j[0] == 'modify_size':
                appliedfilters.append(('modify',filtre[1]))
            if j[0] == 'text':
                appliedfilters.append(('text',filtre[1]))
            if j == 'aquarelle':
               aquarelle(image)
    else:
        print("La commande que vous venez d'effectuer n'existe pas \n Utilisez la commande -help")

                
        
commandLine()