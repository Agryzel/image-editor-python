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