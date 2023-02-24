from PIL import Image
from glob import glob
import os
from numba import njit


def images_to_binary():
    global extension
    extension = ''

    files = glob('frames/*')
    
    with open("file.bin", "a") as f:
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

            else:
                print(f"Lendo imagem >{img}<")
                _bindata = ''

                for x in range(1920):
                    for y in range(1080):
                        _temp = Image.open(img)
                        pix = _temp.getpixel((x,y))

                        match pix:
                            case (0,0,0): # branco
                                _bindata += '0'
                            case (255,255,255): # preto
                                _bindata += '1'
                            case(255,0,0): # vermelho
                                f.write(_bindata)
                                f.close()
                                print("Processo finalizado.")
                                break
                    else:
                        continue
                    break

                f.write(_bindata)
    

def binary_to_file():

    n = int(extension, 2)
    _ext = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()


    with open(f"output_file{_ext}", "wb") as f:
        with open("file.bin", "r") as binary_str:
            _binary = binary_str.read()
            for i in range(0, len(_binary), 8):
                byte = _binary[i:i+8]
                f.write(bytes([int(byte, 2)]))

    os.remove("file.bin")

if __name__ == "__main__":
    print("Cannot run this file standalone. Please use main.py .")