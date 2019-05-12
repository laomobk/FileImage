from PIL import Image

def decode(img, size, length):
    data = []
    ind = 0
    
    for i in range(size):
        for j in range(size):
            d = int(img.getpixel((j, i)))
            
            if ind < length: 
                data.append(d)
            ind += 1

    print('Successfully read data from image...')
    return data


def createFile(path, bl):
    #print(bl)
    print('data size = ', len(bl))
    print('Creating file...')

    with open(path, 'wb') as f:

        print('Success!')
        print('Writing file!')
        
        for b in bl:
            f.write(bytes([b]))

    print('Success!')

def getTargetName(path):
    import os.path

    res = ''
    _, fname = os.path.split(path)

    try:
        ftype = fname.split('.')[-2]
        fname = ''.join(fname.split('.')[0])
        res = fname + '(IMG).' + ftype

    except IndexError:
        res = '(NONAME)' + fname
    
    return res


def main(path, filesize):
    try:
        filesize = int(filesize)

    except:
        print('You should enter a integer!')
        return

    try:
        im = Image.open(open(path, 'rb'))
        im = im.convert('L')
        h = im.height

    except OSError as e:
        print ('Not a image file :', path)
        return
    
    except Exception as e:
        print ('Error :', str(e))    
        return
    
    if h*h < filesize:
        print('File size is too large!!')
        return
    
    d = decode(im, h, filesize)

    createFile(getTargetName(path),d)


if __name__ == "__main__":
    print('==========File Image Decoder==========')
    main(input('Image Path:'), input('File size:'))
    input("Done! PRESS ENTER TO EXIT")
