from colorama import *
import logger
from PIL import Image, ImageFilter
import cv2
import sys
import numpy as np
import os

args = sys.argv[1:]
filters = sys.args[1:]
input_folder = 'immages-test/'
output_folder = './images-changed/'

def commandLine(filters,input_folder,output_folder):

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

    if len(args) > 2:
        print('Invalid number of arguments')

    if len(args) == 1:

        if args[0] == '-log':
            logger.display_log()
        else:
            print("La commande que vous venez d'effectuer n'existe pas \n Utilisez la commande -help")

        if args[0] == '--help':
            input(f"{Fore.GREEN}Voici le support d'aide pour l'image editor. \n Sur quelle categorie veux tu être aider ? \n - Filtres \n {Style.RESET_ALL} ")
        else:
            print("La commande que vous venez d'effectuer n'existe pas \n Utilisez la commande -help")
            
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
    
