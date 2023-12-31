from PIL import Image
from os import listdir
from os.path import splitext

target_directory = 'input_folder'
des_path = 'output_folder'
target = '.jpg'

for file in listdir(target_directory):
    filename, extension = splitext(file)
    try:
        if extension not in ['.py', target]:
            im = Image.open(filename + extension)
            im.save(filename , 'png')
    except OSError:
        print('Cannot convert %s' % file)




