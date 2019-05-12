from PIL import Image

def getImageObject(size):
    return Image.new('L', (size, size), 'black')

def getByteList(fp):
    bl = []
    while 1:
        b = fp.read(1)
        if b == b'':
            break
        bl.append(b)
    
    return [ord(x) for x in bl]

def drawImage(size, byteslist):
    im = getImageObject(size)

    ind = 0

    #print(byteslist)

    try:
        for i in range(size):
            for j in range(size):
                im.putpixel((j, i), (byteslist[ind]))
                ind += 1

    except IndexError:
        print('done! size = '+str(len(byteslist)))

    return im

def showImage(img):
    img.show()

def getSize(path):
    import os.path
    import math

    size = os.path.getsize(path)

    return int(math.sqrt(size) + 1)   

def saveImage(path, image):
    import os.path
    fn = os.path.split(path)[1]
    image.save(fn+'.png', quality=1000)

def run(path, save=False):
    
    with open(path, 'rb') as f:
        bl = getByteList(f)
        size = getSize(path)
        img = drawImage(size, bl)

        if input('show image ? (Y/n)') in ('Y', 'y'):
            showImage(img)

        if save:
            saveImage(path, img)

        input('PRESS ENTER TO EXIT')

if __name__ == "__main__":
    print('==========File Image=========')
    run(input("File Path:"), True)

if __name__ == "1__main__":
    import sys

    if sys.argv[1] == '-s':
        run(sys.argv[2], True)

    elif sys.argv[1] == '-r':
        run(''.join(sys.argv[2:]))

    elif sys.argv[1] == '-rs':
        run(''.join(sys.argv[2:]), True)
    else:
        run(sys.argv[1])
