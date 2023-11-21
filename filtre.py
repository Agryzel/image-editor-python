from PIL import Image
from PIL import ImageFilter
def flou(imgname):
    img=Image.open (f'immages-test/{imgname}')
    imgchanged=img.filter(ImageFilter.BLUR)
    imgchanged.save(f'./images-changed/{imgname}-flouté.png','png')

def monochrome(imgname):
    img=Image.open (f'immages-test/{imgname}')
    imgchanged=img.convert('L')
    imgchanged.save(f'./images-changed/{imgname}-flouté.png','png')