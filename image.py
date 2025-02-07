from PIL import Image

image = Image.open("monro.jpg")
r, g, b = image.split()
r.save("red_channel.jpg")
g.save("green_channel.jpg")
b.save("blue_channel.jpg")

image1 = Image.open("red_channel.jpg")
coordinates = (50, 0, image1.width, image1.height)
cropped = image1.crop(coordinates)
image2 = Image.open("red_channel2.jpg")
coordinates2 = (25, 0, image2.width -25, image2.height)
cropped2 = image2.crop(coordinates2)
image3 = Image.blend(cropped, cropped2, 0.3)
image3.save("blender.jpg")

image4 = Image.open("blue_channel.jpg")
coordinates4 = (0, 0, image4.width -50, image4.height)
cropped4 = image4.crop(coordinates4)
image5 = Image.open("blue_channel2.jpg")
coordinates5 = (25, 0, image5.width -25, image5.height)
cropped5 = image5.crop(coordinates5)
image6 = Image.blend(cropped4, cropped5, 0.5)
image6.save("blender2.jpg")

image7 = Image.open("green_channel.jpg")
coordinates7 = (25, 0, image7.width -25, image7.height)
cropped7 = image7.crop(coordinates7)
cropped7.save("blender3.jpg")


combined_image = Image.merge("RGB", (image3, cropped7, image6))
combined_image.save("combined_image.jpg")

image8 = Image.open("combined_image.jpg")
image8.thumbnail((80, 80))
image8.save("thumbnail.jpg")
