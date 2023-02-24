import filetoimage, imagetofile

def ftv_compactor():

    # Convert file to sequence of images
    filetoimage.create_binary('teste.png')
    filetoimage.binary_to_image()

    # Convert sequence of images to file
    imagetofile.images_to_binary()
    imagetofile.binary_to_file()

if __name__ == '__main__':
    ftv_compactor()