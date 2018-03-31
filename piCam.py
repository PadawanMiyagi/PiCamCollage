from picamera import PiCamera
from time import sleep
from PIL import Image,ImageFilter

x = 256
y = 192
cols = 4
rows = 4

listOfImages = ["0.jpg","1.jpg","2.jpg","3.jpg","4.jpg","5.jpg","6.jpg","7.jpg","8.jpg"
                ,"9.jpg","10.jpg","11.jpg","12.jpg","13.jpg","14.jpg","15.jpg"]
new_im = Image.new("RGB",(1024,768))
new_load = new_im.load
camera = PiCamera()
camera.resolution = (1024,768)

# Takes the image, crops it and puts it into new image
def putImage(column,row):
    left = column*x
    top = row*192

    area = (left,top,left+x,top+y)
    im= Image.open(listOfImages[0])
    cropped_im = im.crop(area)
    new_im.paste(cropped_im,(left,top))
    # Remove the top image from list
    listOfImages.pop(0)


def takePic():
    camera.start_preview()
    sleep(10)
    camera.stop_preview()
    for c in range(0,16):
        camera.capture(str(c)+".jpg")
        sleep(5)
    for i in range(0,cols):
        for j in range(0,rows):
            putImage(i,j)
    new_im.save("Collage.jpg")
    print("Done making collage")

takePic()

