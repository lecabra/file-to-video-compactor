import filetoimage, imagetofile

def ftv_compactor():

    filetoimage.create_binary('teste.png')
    filetoimage.binary_to_image()

    imagetofile.images_to_binary()
    imagetofile.binary_to_file()

if __name__ == '__main__':
    ftv_compactor()