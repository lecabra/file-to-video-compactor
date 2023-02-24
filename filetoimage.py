'''
Get a file, turn it into binary and create a sequence of images with WxH
containing black and white pixels according to the binary.
'''
from PIL import Image
import os



def create_binary(path:str):
    global file_ext
    file_name, file_ext = os.path.splitext(path)
    

    with open(path, 'rb') as file:
        _bin = open("file.bin", "a")
        byte = file.read(1)

        while byte != b"":
            binary = bin(ord(byte))[2:].zfill(8)
            _bin.write(binary)
            byte = file.read(1)
        
        _bin.close()


def binary_to_image():
    try:
        os.mkdir('frames/') #cria a pasta frames
    except:
        pass

    with open("file.bin", "r") as f:
        _var = 0
        _bin = f.read(-1)
        _splitbin = list(_bin)
        _file = 0

        print("Gerando imagens...")
        while not _var == len(_splitbin)-1:
            img = Image.new(mode="RGB", size=(1920, 1080),  color = (255, 0, 0))

            for x in range(1920):
                for y in range(1080):

                    color = (0,0,0)
                    
                    match _splitbin[_var]:
                        case "0":
                            color = (0,0,0)
                        case "1":
                            color = (255,255,255)

                    img.putpixel((x,y), color)
                    if _var == len(_splitbin)-1:
                        break
                    else:
                        _var += 1
            
            
            img.save(f"frames/frame_{_file}.png")
            print(f"Arquivo {_file} renderizado com sucesso.")
            _file += 1

        # ------------------------------------------------ #
        _var = 0
        img = Image.new(mode="RGB", size=(1920, 1080),  color = (255, 0, 0))
        bin_str = ''
        for char in file_ext:
            bin_str += bin(ord(char))[2:].zfill(8)

        for x in range(1920):
            for y in range(1080):

                color = (0,0,0)

                match list(bin_str)[_var]:
                    case "0":
                        color = (0,0,0)
                    case "1":
                        color = (255,255,255)

                img.putpixel((x,y), color)
                if _var == len(list(bin_str))-1:
                    break
                else:
                    _var += 1

        img.save(f"frames/zframe_data.png")
        f.close()
        os.remove("file.bin")

if __name__ == "__main__":
    print("Cannot run this file standalone. Please use main.py .")