from PIL import Image
from PIL import ImageFilter
imgname='téléchargement.jpeg'
img=Image.open (f'immages-test/{imgname}')
imgchanged=img.convert('L')
imgchanged.save(f'./images-changed/{imgname}-flouté.png','png')
img.show()
imgchanged.show()