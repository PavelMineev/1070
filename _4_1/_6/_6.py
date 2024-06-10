# Import the Images module from pillow
from PIL import Image

# Open the image by specifying the image path.
image_path = "img.png"
image = Image.open(image_path)

resize_coefficient = 0.5
new_width = int(image.width * resize_coefficient)
new_height = int(image.height * resize_coefficient)
image_1 = image.resize((new_width, new_height))
image_1.save("img_1.png")

image.thumbnail((100, 100))
image.save("img_2.png")
