from glob import glob
from PIL import Image

files = glob('frames/*')
extension = ''

for img in files:
    if img == "frames\zframe_data.png":
        for x in range(1920):
            for y in range(1080):
                _temp = Image.open(img)
                pix = _temp.getpixel((x,y))

                match pix:
                            case (0,0,0): # branco
                                extension += '0'
                            case (255,255,255): # preto
                                extension += '1'
                            case(255,0,0): # vermelho
                                break
            else:
                 continue
            
            break

print(extension)