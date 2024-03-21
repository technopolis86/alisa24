from PIL import Image, ImageFilter


def motion_blur(n):
    im = Image.open("image.jpg")
    im1 = im.transpose(4).filter(ImageFilter.GaussianBlur(radius=n))
    im1.save('res.jpg')

