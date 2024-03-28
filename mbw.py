from PIL import Image
from PIL import ImageFilter
import os

router = os.getcwd()
specfile = ''

folder = os.listdir(router)

#black and white converter (L) name copier
def bwer_copy():
    length = len(folder)
    indexer = 0
    name = folder[indexer]
    while indexer < length:
        name = folder[indexer]
        if name == 'blackandwhite.py' or name[-4:].lower() != specfile:
            indexer += 1
        if name != 'blackandwhite.py' and name[-4:].lower() == specfile:
            im = Image.open(name)
            imbw = im.convert('L')
            imbw.save(name + '-bw')

#program home
while True:
    prompt = int(input('Welcome to matts black and white converter. Please choose one of the following to get started:\n

