from PIL import Image

image = Image.open("monro.jpg")
red, green, blue = image.split()

coordinates = (50, 0, red.width, red.height)
cropped = red.crop(coordinates)
coordinates2 = (25, 0, red.width -25, red.height)
cropped2 = red.crop(coordinates2)
red = Image.blend(cropped, cropped2, 0.3)

coordinates3 = (0, 0, blue.width -50, blue.height)
cropped3 = blue.crop(coordinates3)
coordinates4 = (25, 0, blue.width -25, blue.height)
cropped4 = blue.crop(coordinates4)
blue = Image.blend(cropped3, cropped4, 0.6)

coordinates5 = (25, 0, green.width -25, green.height)
green = green.crop(coordinates5)

combined_image = Image.merge("RGB", (red, green, blue))
combined_image.save("combined_image.jpg")

image8 = Image.open("combined_image.jpg")
image8.thumbnail((80, 80))
image8.save("thumbnail.jpg")
