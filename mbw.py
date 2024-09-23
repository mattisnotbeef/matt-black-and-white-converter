#note - update program to ignore files already converted

from PIL import Image
from PIL import ImageFilter
import os

router = os.getcwd()
specfile = ''

folder = os.listdir(router)

#b&w converter jpg full folder
def bwer_copy_jpg_full():
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

#bw converter jpg picture by picture
def bwer_copy_jpg_ind():
    length = len(folder)
    indexer = 0
    name = folder[indexer]
    while indexer < length:
        name = folder[indexer]
        if name == 'mbw.py' or name[-4:].lower() != specfile:
            indexer += 1
        if name != 'mbw.py' and name[-4:].lower() == specfile:
            print(name)
            inputter = str(input('y or n to convert\n'))
            if inputter == 'y':
                im = Image.open(name)
                imbw = im.convert('L')
                splitter = name.split('.')
                newname = splitter[0] + '-bw'
                imbw.save(newname + specfile)
                indexer += 1
            elif inputter == 'n':
                    indexer += 1
            else:
                print('Invalid input!')
                
#b&w converter png full folder
def bwer_copy_png_full():
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

#bw converter png picture by picture
def bwer_copy_png_ind():
    length = len(folder)
    indexer = 0
    name = folder[indexer]
    while indexer < length:
        name = folder[indexer]
        if name == 'mbw.py' or name[-4:].lower() != specfile:
            indexer += 1
        if name != 'mbw.py' and name[-4:].lower() == specfile:
            print(name)
            inputter = str(input('y or n to convert\n'))
            if inputter == 'y':
                im = Image.open(name)
                imbw = im.convert('L')
                splitter = name.split('.')
                newname = splitter[0] + '-bw'
                imbw.save(newname + specfile)
                indexer += 1
            elif inputter == 'n':
                    indexer += 1
            else:
                print('Invalid input!')

#program home
while True:
    prompt = int(input('Welcome to matts black and white converter. Please choose one of the following to get started:\n1 to convert jpg\n2 to convert png\n0 to quit\n'))
    
    #quit program
    if prompt == 0:
        print('Goodbye')
        break
    
    #jpgs
    elif prompt == 1:
        specfile = '.jpg'
        prompt = int(input('Choose one of the following:\n1 to create a b&w copy of each jpg in a folder\n2 to go file by file and decide whether to make it b&w\n3 to only make a specific picture b&w\n'))
        #bw name copier (L)
        if prompt == 1:
            bwer_copy_jpg_full()
            print('Job completed!')
        elif prompt == 2:
            bwer_copy_jpg_ind()
            print('No more files to convert!')
        elif prompt == 3:
            photo = input('Please copy the name of your image:\n')
            im = Image.open(photo)
            imbw = im.convert('L')
            splitter = photo.split('.')
            newname = splitter[0] + '-bw'
            imbw.save(newname + specfile)
            print('Job completed!')
    
    #pngs
    elif prompt == 2:
        specfile = '.png'
        prompt = int(input('Choose one of the following:\n1 to create a b&w copy of each png in a folder\n2 to go file by file and decide whether to make it b&w\n3 to only make a specific picture b&w\n'))
        if prompt == 1:
            bwer_copy_png_full()
            print('Job completed!')
        elif prompt == 2:
            bwer_copy_png_ind()
            print('No more files to convert!')
        elif prompt == 3:
            photo = input('Please copy the name of your image:\n')
            im = Image.open(photo)
            imbw = im.convert('L')
            splitter = photo.split('.')
            newname = splitter[0] + '-bw'
            imbw.save(newname + specfile)
            print('Job completed!')
