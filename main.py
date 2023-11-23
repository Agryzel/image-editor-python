import sys
from colorama import *
import logger


args = sys.argv[1:]
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