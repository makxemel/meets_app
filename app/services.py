from PIL import Image


def watermark_avatar_service(image_path, watermark_image_path='media/watermark.png'):
    base_image = Image.open(image_path)
    watermark = Image.open(watermark_image_path)

    base_image.paste(watermark, (0, 0))
    base_image.show()
    base_image.save(image_path)