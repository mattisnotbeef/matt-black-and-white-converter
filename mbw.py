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
        if name == 'mbw.py' or name[-4:].lower() != specfile:
            indexer += 1
        if name != 'mbw.py' and name[-4:].lower() == specfile:
            im = Image.open(name)
            imbw = im.convert('L')
            splitter = name.split('.')
            newname = splitter[0] + '-bw'
            imbw.save(newname + specfile)
            indexer += 1

#program home
while True:
    prompt = int(input('Welcome to matts black and white converter. Please choose one of the following to get started:\n1 to convert jpg(s)\n2to convert png(s)\n3 to convert ORF(s)\n4 to convert CR2(s)\n0 to quit'))
    
    if prompt == 0:
        print('Goodbye')
        break
    
    #jpgs
    elif prompt == 1:
        specfile = '.jpg'
        prompt = int(input('Choose one of the following:\n1 to create a b&w copy of each jpg in a folder\n2 to'))
        #bw name copier (L)
        if prompt == 1:
            bwer_copy()
            print('Job completed!')
