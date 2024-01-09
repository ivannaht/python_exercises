from PIL import Image

image_1 = Image.open('cat_1.jpeg')
image_2 = Image.open('dog_1.jpeg')
image_1.show()
size_1 = image_1.size
image_2 = image_2.resize(size_1)
image_2.show()
image_2.putalpha(150)
image_1.paste(image_2, (0,0), image_2)
image_1.show()
image_1.close()
image_2.close()