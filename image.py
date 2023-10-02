from PIL import Image, ImageFilter

f40 = Image.open("./IMAGES/F40_Ferrari.jpg")
f1 = Image.open("./IMAGES/mclaren_f1.jpeg")
rs7 = Image.open("./IMAGES/RS7.jpg")
svj = Image.open("./IMAGES/SVJ.jpg")

im1 = f40.filter(ImageFilter.BLUR)
im2 = f1.convert('L')
im3 = rs7.filter(ImageFilter.SHARPEN)
im4 = svj.filter(ImageFilter.DETAIL)

im5 = im1.resize((400,400))
im6 = im4.rotate(180)

box= (100,100,400,400)
im7 = im2.crop(box)

im8 = svj
im8.thumbnail((500,500))

im5.show()
im7.show()
im8.show()

im1.save("blur.png", 'png')
im2.save("b&w.png", 'png')
im3.save("sharpen.png", 'png')
im4.save("detail.png", 'png')

