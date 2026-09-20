from PIL import Image


image = Image.open("monro.jpg")
red, green, blue = image.split()


red_left = red.crop((200, 0, red.width, red.height))
red_middle = red.crop((100, 0, red.width - 100, red.height))
red_shifted = Image.blend(red_left, red_middle, 0.5)


blue_right = blue.crop((0, 0, blue.width - 200, blue.height))
blue_middle = blue.crop((100, 0, blue.width - 100, blue.height))
blue_shifted = Image.blend(blue_right, blue_middle, 0.5)


green_cropped = green.crop((100, 0, green.width - 100, green.height))


final = Image.merge("RGB", (red_shifted, green_cropped, blue_shifted))
final.save("final.jpg")


final.thumbnail((80, 80))
final.save("avatar.jpg")
