from PIL import Image


def add_watermark(image_path):
    image = Image.open(image_path)
    watermark = Image.open('watermark.png')
    position = (image.width - watermark.width, image.height - watermark.height)
    image.paste(watermark, position)
    path_parts = image_path.split(".")
    image.save("".join(path_parts[:-1:] + ['_watermark.'] + path_parts[-1::]))

add_watermark("img.png")
